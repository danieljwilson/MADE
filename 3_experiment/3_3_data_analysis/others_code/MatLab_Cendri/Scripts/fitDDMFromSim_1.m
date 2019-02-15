function [SimNLL, BestParameters] = fitDDMFromSim_1(subject)

pathtofile = mfilename('fullpath');
path = pathtofile(1:(regexp(pathtofile,'Analysis') - 1));
model = '1';


simID = '1';
% check if operating on UTSC cluster or on local computer
homepath = '/psyhome/u7/hutchers/';
if exist(homepath,'dir')
    simInfo = load(fullfile(homepath, 'ATP1','Simulations', simID, ['simInfo_', simID, '.mat']));
else
    simInfo = load(fullfile('~/Desktop/Dropbox/Projects/SelfOtherFoodDM/DDMAnalysis/Simulations/', simID, ['simInfo_', simID, '.mat']));
end

%% load behavioral data
load(fullfile(path,'SubjectData',subject,['Data.' subject '.choice.mat']))

NonResp = cellfun(@(x)strcmp(x,'NULL'),Data.Resp);
Data.Resp(NonResp) = {NaN};
Data.Resp = +(cell2mat(Data.Resp) == 2);
Data.Resp(NonResp) = NaN;

Data.SelfProposal = cell2mat(Data.SelfProposal);
Data.OtherProposal = cell2mat(Data.OtherProposal);

%% coarse grid search for best parameters
combo.weight1 = -.04:.01:.07;
combo.weight2 = -.04:.01:.07;
combo.upper = (8:2:20)/100;
combo.collapseRate = [0, .001, .003, .005, .007, .01];
combo.nonDec = 0:.2:1;

% create all combinations of desired variables
comboVars = fieldnames(combo);
parameterCombos = combo.(comboVars{1})';
for v = 2:length(comboVars)
    parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
        sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
end

conds = {'Short' 'Long'};
timelimit = [2 10];
for c = 1:2
    simInfo.combo.maxRT = timelimit(c);
    selectedTrials = cellfun(@(x)x == timelimit(c), Data.TimeLimit);
    
    tempData.resp = Data.Resp(selectedTrials);
    tempData.rt = cell2mat(Data.ChoiceRT(selectedTrials));
    tempData.attribVals = [Data.SelfProposal(selectedTrials)' - 10 ...
                           Data.OtherProposal(selectedTrials)' - 10];
    
    
    uniqueVals = unique(abs(tempData.attribVals*parameterCombos(:,1:2)'));
    valStruct = struct('SimData',[]);                  
    for v = 1:length(uniqueVals) % 15 secs
        valStruct(v) = load(fullfile(path,'Simulations',simID,sprintf('Sim_%0.6f.mat',uniqueVals(v))));
    end
    
    SimNLL = zeros(length(parameterCombos),1);
    nLoops = numel(SimNLL);
    
    ddmFile = fullfile(path,'Analysis','FittedResults',simID, ['DDM_fittedResults_m' model '_' subject '_' conds{c} '.mat']);
    if exist(ddmFile, 'file')
        % delete(ddmFile) % for use if you want to quickly delete old results
        load(ddmFile)
    end
    
    if any(SimNLL(:) == 0) % run simulations if not complete yet
        
        for loop = 1:nLoops
            % check to see if a kill command has been
            % issued
            if exist(fullfile(path,['kill' model '.mat']),'file')
                break;
            end
            
            if SimNLL(loop) == 0
                
                % get negative log likelihood of the data for each combination of
                % parameter values
                SimNLL(loop) = NLLSimData_fromVals(tempData,parameterCombos(loop,:),valStruct,uniqueVals, simInfo.combo);
                
                if mod(loop,100) == 0 || (loop > nLoops - 101)
                    save(ddmFile,'SimNLL','loop');
                end
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
    params = simInfo.params;
    params.inputvals = repmat(tempData.attribVals*parameterCombos(i,1:2)',1000,1);
    params.upper = BestParameters(3);
    params.lower = -1*BestParameters(3);
    params.collapseRate = BestParameters(4);
    %params.nonDec = BestParameters(5);
      
    SimData = simulDDM(params);
    SimData.rt = SimData.rt + BestParameters(5);
    
    SimData.drift = repmat(tempData.attribVals(:,1),1000,1);
    SimData.drift2 = repmat(tempData.attribVals(:,2),1000,1);
    
    % save all parameters used in simulations
    params.candidate_driftTaste = combo.weight1;
    params.candidate_driftHealth = combo.weight2;
    params.candidate_nondec = combo.nonDec;
    params.candidate_barrier = combo.upper;
    params.candidate_barrierCollapse = combo.collapseRate;
    params.simCode = simInfo.params.whichSim;
    
%     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_' conds{c} '.mat']),'SimNLL',...
%         'SimData','BestParameters','params');

    save(ddmFile,'SimNLL','BestParameters','params','SimData');

end


% %% finer simulation around best parameters from coarse grid search
% 
% combo.weight1 = -.04:.02:.16;
% combo.weight2 = -.04:.02:.16;
% combo.upper = (8:2:20)/100;
% combo.collapseRate = [0, .001, .0025, .005, .0075, .01];
% combo.nonDec = 0:.1:.6;
% 
% for c = 1:3
%     
%     selectedTrials = TrialType == c;
%     
%     tempData.resp = Data.resp(selectedTrials);
%     tempData.rt = Data.rt(selectedTrials);
%     tempData.attribVals = [Data.dim1(selectedTrials) ...
%                            Data.dim2(selectedTrials)];
% 
%     % get BestParameters variable from previous simulation
%     ddmFile = fullfile(path,'DDMAnalysis','FittedResults',simID, ['DDM_fittedResults_m' model '_' subject '_' conds{c} '.mat']);
%     load(ddmFile);
%     
%     % simulate set of choices on full dataset using best parameters
%     params = simInfo.params;
%     params.driftRate = tempData.attribVals*BestParameters(1:3)';
%     params.simsPerDrift = 1000;
%     params.barrier = BestParameters(4);
%     params.barrierCollapse = BestParameters(5);
%     params.nonDec = BestParameters(6);
%       
%     SimData = simulDDM_normApproxSimResps(params);
%     SimData.drift = reshape(repmat(tempData.attribVals(:,1),1,params.simsPerDrift)',...
%         1,numel(repmat(tempData.attribVals(:,1),params.simsPerDrift,1)))';
%     SimData.drift2 = reshape(repmat(tempData.attribVals(:,2),1,params.simsPerDrift)',...
%         1,numel(repmat(tempData.attribVals(:,2),params.simsPerDrift,1)))';
%     SimData.drift3 = reshape(repmat(tempData.attribVals(:,3),1,params.simsPerDrift)',...
%         1,numel(repmat(tempData.attribVals(:,3),params.simsPerDrift,1)))';
%     
%     % save all parameters used in simulations
%     params.candidate_driftSelf = combo.selfW;
%     params.candidate_driftOther = combo.otherW;
%     params.candidate_driftIneq = combo.ineqW;
%     params.candidate_nondec = combo.nonDec;
%     params.candidate_barrier = combo.upper;
%     params.candidate_barrierCollapse = combo.collapseRate;
%     params.simCode = simInfo.simCode;
%     
% %     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_' conds{c} '.mat']),'SimNLL',...
% %         'SimData','BestParameters','params');
% 
%     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model 'NormSim_Fine' conds{c} '.mat']),'SimNLL',...
%         'BestParameters','params','SimData');
% 
% 
% end

