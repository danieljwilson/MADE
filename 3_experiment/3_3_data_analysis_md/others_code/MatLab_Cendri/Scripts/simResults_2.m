function simResults_2
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

% model = regexp(pathtofile,'simResults_(.*)\.m','tokens');
% model = model{1}{1};
model = '2';
mkdir(fullfile(path, 'Simulations', model))

[Self, Other] = meshgrid(0:20, 0:20);

valuepairs = [Self(:), Other(:)] - 10;

params.startvar = 0;
params.nondecvar = 0;
params.driftvar = 0;
params.driftvar2 = 0;
params.MaxRT = 10;
params.RespOptions = {0,1};
params.precision = .01;
params.s = .1;


combo1.weight1 = -.05:.0025:.05; 
combo1.weight2 = -.05:.0025:.05;
combo1.weight3 = -.05:.0025:.05;

combos = [0,0,0];%create the matrix
% combine the two drift rates
for i = 1:length(combo1.weight1)
    for j = 1:length(combo1.weight2)
        for k = 1:length(combo1.weight3)
            combos(end+1,:) = [combo1.weight1(i) combo1.weight2(j), combo1.weight3(k)];
        end
    end
end
% ? WHY value pairs difference column always negative?
valuepairs = [valuepairs -1 * abs(valuepairs(:,1) - valuepairs(:,2))];
allvals= valuepairs* combos';%all the combinations
allvals = abs(allvals);
combo.inputvals = unique(allvals(:))';%row and column

combo.upper = (2:2:24)/100;
combo.collapseRate = 0:.0001:.001;
combo.startBias = -.3:.1:.3;
% % create all combinations of desired variables
% comboVars = fieldnames(combo);
% parameterCombos = combo.(comboVars{1})';
% for v = 2:length(comboVars)
%     parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
%         sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
% end


whichSim = 'simulDDM';

RTBins = [0:.1:params.MaxRT;0:.1:params.MaxRT];

% % create separate variables for calling in parfor
% for v = 1:length(comboVars)
%     eval([char((v - 1) + 'a') ' = parameterCombos(:,' num2str(v) ');'])
% end


% AllSims = cell(size(parameterCombos,1),1);
% nLoops = size(parameterCombos,1);

AllSims = cell(length(combo.inputvals),1);%create the cell array
nLoops = length(combo.inputvals);%values matters the most

parfor loop = 1:nLoops
    %disp(num2str(loop))
    AllSims{loop}.simFile = fullfile(path, 'Simulations',model, ...
    ['Sim_' num2str(combo.inputvals(loop),'%10.6f') '.mat']);% values_boundary_nondec_collapseRate

%     if exist(fullfile(path, 'kill.txt'), 'file')
%         return;
%     end
    if ~exist(AllSims{loop}.simFile, 'file')
        parSave(AllSims{loop}.simFile, loop)
        
        
        AllSims{loop}.inputvals = combo.inputvals(loop)*ones(15000,1);%simulate for 5000 times--each select one value and then simulate for 5000 times
        AllSims{loop}.results = cell(length(combo.upper), length(combo.collapseRate), length(combo.startBias));
        tic
        for i = 1:length(combo.upper)
            for j = 1:length(combo.collapseRate)
                for k = 1:length(combo.startBias)
                    AllSims{loop}.params{i,j,k} = params;
                    AllSims{loop}.params{i,j,k}.inputvals = AllSims{loop}.inputvals;
                    AllSims{loop}.params{i,j,k}.upper = combo.upper(i); % upper bound adjusted for starting bias
                    AllSims{loop}.params{i,j,k}.collapseRate = combo.collapseRate(j);
                    AllSims{loop}.params{i,j,k}.startBias = combo.startBias(k);

                    AllSims{loop}.results{i,j,k} = simulDDM(AllSims{loop}.params{i,j,k});
                    [temp1, temp2] = ddm_observedprobs(AllSims{loop}.results{i,j,k},RTBins,params.RespOptions);
                    AllSims{loop}.ProbMat{i,j,k} = temp2;

                    AllSims{loop}.results = []; % get rid this to save memory
                    AllSims{loop}.params{i,j,k}.inputvals = AllSims{loop}.inputvals(1);% all values are the same, so just use the first one
                end
            end
        end
        toc
   
        parSave(AllSims{loop}.simFile, AllSims{loop})    
    end

end
params.whichSim = fileread(fullfile(path,[whichSim '.m']));

save(fullfile(path, 'Simulations', ['simInfo_' model '.mat']), 'model',...
    'valuepairs', 'params','combo1','combo','whichSim','RTBins');

save(fullfile(path, 'Simulations', '1',['simInfo_' model '.mat']), 'model',...
    'valuepairs', 'params','combo1','combo','whichSim','RTBins');

% parSave
function parSave(fileName, saveVar)
    SimData = saveVar;
    save(fileName, 'SimData');

