% Simulates choices and RTs for the specified model, using all combinations
% of a specified set of parameters
% Note: designed to run on a parallel computing cluster to speed up
% simulation
%
% Author: Cendri Hutcherson

fileName = mfilename;
pathtofile = which(fileName, '-ALL');
if length(pathtofile) > 1
    pathtofile = pathtofile{2};
else
    pathtofile = pathtofile{1};
end
path = pathtofile(1:(regexp(pathtofile,'scripts') - 1));

model = regexp(pathtofile,'simResults_(.*)\.m','tokens');
model = model{1}{1};

mkdir(fullfile(path, 'Simulations2', model))

valuepairs = [[20:30; 70:80]';      %simulate reduced set of values (combined value) in .1 increments
              [20:25; 95:100]';
              [45:55; 5:15]';
              [45:50; 95:100]';
              [70:80; 5:15]';
              [70:80; 20:30]';
              [95:100; 5:10]';
              [95:100; 20:25]';
              [95:100; 45:50]'] - 50;

params.inputvals = repmat(valuepairs(:,1),1000,1);
params.inputvals2 = repmat(valuepairs(:,2),1000,1);

params.startvar = 0;
params.nondecvar = 0;
params.driftvar = 0;
params.driftvar2 = 0;
params.MaxRT = 4;
params.RespOptions = {0,1};
params.precision = .001;
params.s = .1;

combo.upper = (4:2:32)/100;   % .04 -> .32 in steps of .02
%don't need weights...just need the values
combo.drift = [-.0045, -.003, -.0015 0 .0015 0.0030  .0045  0.0060 .0075 .009 .0105 .0120 .0135]; %weight on self
combo.drift2 = [-.0045 -.003, -.0015, 0, .0015, .003, .0045, .006 .0075 .009 .0105 .012 .0135]; % weight on other
combo.nondec = .3:.2:1.3;   % do not include in parameters (constant added later)
combo.collapseRate = [0, .00005, .0001, .00025 .0005, .00075, .001, .005]; 
% NEED integrated value, boundary, collapse rate (if collapsing bounds)

% create all combinations of desired variables
comboVars = fieldnames(combo);
parameterCombos = combo.(comboVars{1})';
for v = 2:length(comboVars)
    parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
        sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
end


whichSim = 'simulDDM';

RTBins = [0:.250:4;0:.250:4];

% create separate variables for calling in parfor (for cluster computing (andy lee/adrian nestor))
for v = 1:length(comboVars)
    eval([char((v - 1) + 'a') ' = parameterCombos(:,' num2str(v) ');'])
end


AllSims = cell(size(parameterCombos,1),1);  %setting up cell array that will hold simulations

nLoops = size(parameterCombos,1);

parfor loop = 1:nLoops % same as number of elements in parameterCombos
    AllSims{loop}.simFile = fullfile(path, 'Simulations',model, ...
    ['Loop_' num2str(loop) '.mat']);

    if ~exist(AllSims{loop}.simFile, 'file')     % checking to see if another worker has already created file
        parSave(AllSims{loop}.simFile, loop) 
        
        AllSims{loop}.params = params;

        AllSims{loop}.params.upper = a(loop);
        AllSims{loop}.params.lower = -1 * AllSims{loop}.params.upper; 
        AllSims{loop}.params.drift = b(loop);
        AllSims{loop}.params.drift2 = c(loop);
        AllSims{loop}.params.nondec = d(loop);
        AllSims{loop}.params.collapseRate = e(loop);
    
        AllSims{loop}.results = simulDDM(AllSims{loop}.params);
        AllSims{loop}.results.rt = AllSims{loop}.results.rt + AllSims{loop}.params.nondec;
        
        AllSims{loop}.ProbMat = getProbMat(AllSims{loop}.results, RTBins, params);  % looks at likelihood of response for diffent quantiles
    
        AllSims{loop}.results = [];   % done to save memory (clearing results)
        AllSims{loop}.params = parameterCombos(loop,:);   %store param combos that produce the loop

        parSave(AllSims{loop}.simFile, AllSims{loop})    % save the simulations (loops from parameterCombos)
    end

end
