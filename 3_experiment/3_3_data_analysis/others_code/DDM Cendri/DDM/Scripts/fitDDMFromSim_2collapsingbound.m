function [SimNLL, BestParameters] = fitDDMFromSim_2collapsingbound(subject)
% function [SimNLL, BestParameters] = fitDDMFromSim_2collapsingbound(subject)
% Finds the maximum likelihood estimate of the specified model for an 
% individual subject, using simulated probability distributions of choices
% and RTs
%
% Author: Cendri Hutcherson

pathtofile = mfilename('fullpath');
path = pathtofile(1:(regexp(pathtofile,'Scripts') - 1));
model = regexp(pathtofile,'_(\d.*)','tokens');
model = model{1}{1};  % gets the string

simID = '2collapsingbound';   % same as model
load(fullfile(path, 'Simulations',['simResults_' simID '.mat']))
valPairs = sortrows(valPairs);
paramNames = fieldnames(combo);

% line 20-43 getting single subject data
files = dir(fullfile(path, subject, 'Data*mat'));
files = {files(~cellfun(@isempty,regexp({files.name},'Data.*scan.*mat'))).name};

Resp = {};
RT = {};
SelfAmount = {};
OtherAmount = {};
for i = 1:length(files)
    load(fullfile(path, subject, files{i}));
    Resp = [Resp, Data.Resp]; % (~cellfun(@isnan,Data.Resp))
    RT = [RT,Data.RT]; % (~cellfun(@isnan,Data.Resp))
    SelfAmount = [SelfAmount, Data.SelfAmount]; % (~cellfun(@isnan,Data.Resp))
    OtherAmount = [OtherAmount, Data.OtherAmount]; % (~cellfun(@isnan,Data.Resp))
end

clear Data;

Data.resp = cell2mat(Resp);% final Response
Data.resp = Data.resp > 2;
RT(cellfun(@isnan,Resp)) = {NaN};
Data.rt = cell2mat(RT); % final RT

Data.dim1 = cell2mat(SelfAmount)' - 50; % $self
Data.dim2 = cell2mat(OtherAmount)' - 50; % $other

RTBins = [0:.250:4;0:.250:4];

SimNLL = zeros(length(parameterCombos),1);
nLoops = numel(SimNLL);

if exist(fullfile(path,subject, ['DDM_results_m' model '.mat']), 'file')  % create file to save all of the likelihoods for all paramCombos
    load(fullfile(path,subject, ['DDM_results_m' model '.mat']))
end

%save in variable SimNLL (simulated negative log likelihood)
if any(SimNLL(:) == 0) % run simulations if not complete yet

    for loop = 1:nLoops 
    % check to see if a kill command has been issued (allows clean suspension and
    % resumption of job on cluster
    if exist(fullfile(path,['kill' model '.mat']),'file') 
        break;
    end

    if SimNLL(loop) == 0 % if the log likelihood hasn't been found yet
    
        % get negative log likelihood of the data for each combination of
        % parameter values
        SimNLL(loop) = NLLSimData(Data,simLikelihoods{loop}.ProbMat,valPairs,RTBins);
        save(fullfile(path,subject, ['DDM_results_m' model '.mat']),...
            'SimNLL','loop');
    end
    clc;
    fprintf('Loop %d completed: %.1f percent finished\n\n',loop,loop/nLoops * 100)
    end
end

i = find(SimNLL == min(SimNLL));
if length(i) > 1
    i = i(randperm(length(i))); % pick a random set of parameters if more than one fits
    i = i(1);
end

BestParameters = parameterCombos(i, :);

% simulate set of choices on full dataset using best parameters
params.inputvals = repmat(Data.dim1,1000,1); % $self
params.inputvals2 = repmat(Data.dim2,1000,1); % $other

for v = 1:length(paramNames)
    params.(paramNames{v}) = BestParameters(v);
end

params.lower = -1*params.upper;

SimData = eval([whichSim '(params)']);
SimData.rt = SimData.rt + params.nondec;

% save all parameters used in simulations
params.candidate_drift = combo.drift;
params.candidate_drift2 = combo.drift2;
params.candidate_nondec = combo.nondec;
params.candidate_upper = combo.upper;
params.candidate_collapseRate = combo.collapseRate;
params.whichSim = fileread([whichSim '.m']);

save(fullfile(path,subject, ['DDM_results_m' model '.mat']),'SimNLL',...
    'SimData','BestParameters','params');
