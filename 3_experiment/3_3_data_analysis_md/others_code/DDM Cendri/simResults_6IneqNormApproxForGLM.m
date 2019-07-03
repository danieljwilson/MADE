fileName = mfilename;
pathtofile = which(fileName, '-ALL');
if length(pathtofile) > 1
    pathtofile = pathtofile{2};
else
    pathtofile = pathtofile{1};
end
path = pathtofile(1:(regexp(pathtofile,'scripts') - 1));

[Self, Other] = meshgrid(-20:4:20, -20:4:20); % course grid of possible combinations of $Self and $Other
valuepairs = [Self(:), Other(:)];
valuepairs(sign(valuepairs(:,1)) == sign(valuepairs(:,2)),:) = [];
valuepairs(:,3) = -1*abs(valuepairs(:,1) - valuepairs(:,2))/2; % note that we divide inequality by 2 so that it is on same range as others
valuepairs = sortrows(valuepairs);

params.maxRT = 4;
params.simPrecision = .001;
params.summaryPrecision = .001;
params.simsPerDrift = 2000;
params.numSteps = 100;
params.s = .1;
params.nonDec = 0;

% get all unique integrated values
vals.selfW = -.016:.008:.024;
vals.otherW = -.016:.008:.024;
vals.ineqW = -.016:.008:.024;

comboVars = fieldnames(vals);
valCombos = vals.(comboVars{1})';
for v = 2:length(comboVars)
    valCombos = [repmat(valCombos, length(vals.(comboVars{v})), 1), ...
        sort(repmat(vals.(comboVars{v})',size(valCombos,1), 1))];
end

valCombos = valuepairs*valCombos';
uniqueVals = unique(valCombos); % take the average value


barriers.upper = (10:4:34)/100;
barriers.collapseRate = [0, .00025 .0005, .00075, .001, .002];


% create all combinations of desired variables
comboVars = fieldnames(barriers);
barrierCombos = barriers.(comboVars{1})';
for v = 2:length(comboVars)
    barrierCombos = [repmat(barrierCombos, length(barriers.(comboVars{v})), 1), ...
        sort(repmat(barriers.(comboVars{v})',size(barrierCombos,1), 1))];
end

whichSim = 'simulDDM_normApproxSimResps';

% create separate variables for calling in parfor
for v = 1:length(comboVars)
    eval([char((v - 1) + 'a') ' = barrierCombos(:,' num2str(v) ');'])
end


AllSims = cell(size(uniqueVals,1),1);

nLoops = size(uniqueVals,1);

for loop = 1:nLoops
    
    AllSims{loop}.simFile = fullfile(path, 'Simulations','AllValuesForGLM', ...
    ['Val' num2str(uniqueVals(loop)) '.mat']);

    if ~exist(AllSims{loop}.simFile, 'file')
        parSave(AllSims{loop}.simFile, loop)
        
        AllSims{loop}.params = params;
        AllSims{loop}.results = struct('rt',[],'resp',[],'AUC',[]);

        
        AllSims{loop}.params.driftRate = uniqueVals(loop);
        for i = 1:size(barrierCombos,1)
            AllSims{loop}.params.barrier = a(i);
            AllSims{loop}.params.barrierCollapse = b(i);
            temp = simulDDM_normApproxSimResps(AllSims{loop}.params);
            AllSims{loop}.results(i) = rmfield(temp,'probs');
        end

        parSave(AllSims{loop}.simFile, AllSims{loop}.results)    
    end
    clc;
    sprintf('Percent completed: %0.2f%%',loop/nLoops*100)
end

simCode = fileread([whichSim '.m']);

save(fullfile(path,'Simulations','AllValuesForGLM','simInfo.mat'),'vals','uniqueVals',...
    'barriers','barrierCombos','simCode','params','valuepairs');
