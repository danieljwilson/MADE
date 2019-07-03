function [SimNLL, BestParameters] = fitDDMFromSim_6IneqValMethodNormSim(subject)

pathtofile = mfilename('fullpath');
path = pathtofile(1:(regexp(pathtofile,'scripts') - 1));
model = '6IneqValMethod';

simID = 'AllValues';
simInfo = load(fullfile(path, 'Simulations', simID, 'simInfo.mat'));

%% load behavioral data (from subject)
files = dir(fullfile(path, 'BehavioralData',subject, 'Data*mat'));
files = {files(~cellfun(@isempty,regexp({files.name},'Data.*\.\d\.mat'))).name};

Resp = {};
RT = {};
SelfAmount = {};
OtherAmount = {};
TrialType = {};
for i = 1:length(files)
    load(fullfile(path, 'BehavioralData',subject, files{i}));
    Resp = [Resp, Data.Resp]; % (~cellfun(@isnan,Data.Resp))
    RT = [RT,Data.ChoiceRT]; % (~cellfun(@isnan,Data.Resp))
    SelfAmount = [SelfAmount, Data.SelfProposal]; % (~cellfun(@isnan,Data.Resp))
    OtherAmount = [OtherAmount, Data.OtherProposal]; % (~cellfun(@isnan,Data.Resp))
    TrialType = [TrialType, Data.Instruction];
end

clear Data;
NonResp = strcmp(Resp,'NULL');
Resp(NonResp) = {NaN};
RT(NonResp) = {NaN};


Data.resp = cell2mat(Resp);% final Response
Data.resp = +(Data.resp > 2);
Data.resp(NonResp) = NaN;
Data.rt = cell2mat(RT); % final RT

Data.dim1 = cell2mat(SelfAmount)' - 20; % $self
Data.dim2 = cell2mat(OtherAmount)' - 20; % $other
Data.dim3 = -1*abs(Data.dim1 - Data.dim2)/2;

%% coarse grid search for best parameters
combo.selfW = -.016:.008:.04;
combo.otherW = -.016:.008:.04;
combo.ineqW = -.016:.008:.04;
combo.upper = (10:4:34)/100;
combo.collapseRate = [0, .0001, .00025 .0005, .00075, .001, .002];
combo.nonDec = .25:.25:1.25;

% create all combinations of desired variables
comboVars = fieldnames(combo);
parameterCombos = combo.(comboVars{1})';
for v = 2:length(comboVars)
    parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
        sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
end

conds =  {'Nat','Ethics','Partner'};
for c = 1:3
    selectedTrials = cellfun(@(x)(~isempty(regexp(x,conds{c},'once'))), TrialType);
    
    tempData.resp = Data.resp(selectedTrials);
    tempData.rt = Data.rt(selectedTrials);
    tempData.attribVals = [Data.dim1(selectedTrials) ...
                           Data.dim2(selectedTrials) ...
                           Data.dim3(selectedTrials)];

    load(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']))
    
    
    % simulate set of choices on full dataset using best parameters
    params = simInfo.params;
    params.driftRate = tempData.attribVals*BestParameters(1:3)';
    params.simsPerDrift = 1000;
    params.barrier = BestParameters(4);
    params.barrierCollapse = BestParameters(5);
    params.nonDec = BestParameters(6);
    
    
    SimData = simulDDM_normApproxSimResps(params);
    
    SimData.drift = reshape(repmat(tempData.attribVals(:,1),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,1),params.simsPerDrift,1)))';
    SimData.drift2 = reshape(repmat(tempData.attribVals(:,2),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,2),params.simsPerDrift,1)))';
    SimData.drift3 = reshape(repmat(tempData.attribVals(:,3),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,3),params.simsPerDrift,1)))';
    
    % save all parameters used in simulations
    params.candidate_driftSelf = combo.selfW;
    params.candidate_driftOther = combo.otherW;
    params.candidate_driftIneq = combo.ineqW;
    params.candidate_nondec = combo.nonDec;
    params.candidate_barrier = combo.upper;
    params.candidate_barrierCollapse = combo.collapseRate;
    params.simCode = simInfo.simCode;
    
%     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_' conds{c} '.mat']),'SimNLL',...
%         'SimData','BestParameters','params');

    save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model 'NormSim_Coarse' conds{c} '.mat']),'SimNLL',...
        'BestParameters','params','SimData');

end


%% finer simulation around best parameters from coarse grid search

for c = 1:3
    
    selectedTrials = cellfun(@(x)(~isempty(regexp(x,conds{c},'once'))), TrialType);
    
    tempData.resp = Data.resp(selectedTrials);
    tempData.rt = Data.rt(selectedTrials);
    tempData.attribVals = [Data.dim1(selectedTrials) ...
                           Data.dim2(selectedTrials) ...
                           Data.dim3(selectedTrials)];

    % get BestParameters variable from previous simulation
    load(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Fine' conds{c} '.mat']))
    
    % simulate set of choices on full dataset using best parameters
    params = simInfo.params;
    params.driftRate = tempData.attribVals*BestParameters(1:3)';
    params.simsPerDrift = 1000;
    params.barrier = BestParameters(4);
    params.barrierCollapse = BestParameters(5);
    params.nonDec = BestParameters(6);
      
    SimData = simulDDM_normApproxSimResps(params);
    SimData.drift = reshape(repmat(tempData.attribVals(:,1),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,1),params.simsPerDrift,1)))';
    SimData.drift2 = reshape(repmat(tempData.attribVals(:,2),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,2),params.simsPerDrift,1)))';
    SimData.drift3 = reshape(repmat(tempData.attribVals(:,3),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,3),params.simsPerDrift,1)))';
    
    % save all parameters used in simulations
    params.candidate_driftSelf = combo.selfW;
    params.candidate_driftOther = combo.otherW;
    params.candidate_driftIneq = combo.ineqW;
    params.candidate_nondec = combo.nonDec;
    params.candidate_barrier = combo.upper;
    params.candidate_barrierCollapse = combo.collapseRate;
    params.simCode = simInfo.simCode;
    
%     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_' conds{c} '.mat']),'SimNLL',...
%         'SimData','BestParameters','params');

    save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model 'NormSim_Fine' conds{c} '.mat']),'SimNLL',...
        'BestParameters','params','SimData');


end

