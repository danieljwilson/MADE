function [SimNLL, BestParameters] = fitDDMFromSim_3(subject)

pathtofile = mfilename('fullpath');
path = pathtofile(1:(regexp(pathtofile,'Scripts') - 1));
model = '1';


simID = '1';
% check if operating on UTSC cluster or on local computer
homepath = '/psyhome/u5/wilso603/';
if exist(homepath,'dir')
    simInfo = load(fullfile(homepath, 'FolderName','SubFolderName', simID, ['simInfo_', simID, '.mat']));
else
    simInfo = load(fullfile('~/Desktop/Dropbox/Projects/SelfOtherFoodDM/DDMAnalysis/Simulations/', simID, ['simInfo_', simID, '.mat']));
end

mkdir(fullfile(homepath, 'FolderName','SubFolderName','ExistingResultsFOLDER','NAME OF SIM ID ETC'))
%% load behavioral data
load(fullfile(path,'SubjectData',subject,['Data.' subject '.choice.mat']))  %in the file I have = 10

NonResp = cellfun(@(x)strcmp(x,'NULL'),Data.Resp);  %holds all non Responses
Data.Resp(NonResp) = {NaN};  % replace with NaN (avoid error in following line)
Data.Resp = +(cell2mat(Data.Resp) == 2); % Converting non null responses to 1/0
Data.Resp(NonResp) = NaN; % replace with NaN

Data.SelfProposal = cell2mat(Data.SelfProposal);         % house and face value with mults?
Data.OtherProposal = cell2mat(Data.OtherProposal);

%% grid search for best parameters
% These values need to be subset of values in simResults_3!!!

combo.weight1 = [.001:.005:.09];    % run both with one weight and individual weights on house and face
%combo.weight2 = [-.02:.005:.03, -.002, .002];
combo.upper = (4:4:20)/100;
combo.collapseRate = 0:.0002:.001;
combo.nonDec = 0:.15:.9;
combo.startBias = -.3:.05:.3;   % this is a percentage of the upper boundary

% create all combinations of desired variables
comboVars = fieldnames(combo);
parameterCombos = combo.(comboVars{1})';
for v = 2:length(comboVars)
    parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
        sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
end

%
simInfo.combo.maxRT = 10; % set maxRT

tempData.resp = Data.Resp;
tempData.rt = cell2mat(Data.ChoiceRT);
tempData.attribVals = [Data.SelfProposal' ...    % face value
                       Data.OtherProposal(selectedTrials)'];   % house value


uniqueVals = unique(abs(tempData.attribVals*parameterCombos(:,1:2)'));
valStruct = struct('SimData',[]);                  
for v = 1:length(uniqueVals)   % this is loading all of the likelihoods
    valStruct(v) = load(fullfile(path,'Simulations',simID,sprintf('Sim_%0.6f.mat',uniqueVals(v))));
end

SimNLL = zeros(length(parameterCombos),1);
nLoops = numel(SimNLL);

% model is named at the top of the script
ddmFile = fullfile(path,'Folder','SubFolder',model, ['DDM_fittedResults_m' model '_' subject '.mat']);
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
            SimNLL(loop) = NLLSimData_fromValswBias(tempData,parameterCombos(loop,:),valStruct,uniqueVals, simInfo.combo);

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
params.inputvals = repmat(tempData.attribVals*parameterCombos(i,1:2)',1000,1); %sim for 1000 times
params.upper = BestParameters(3);
params.lower = -1*BestParameters(3);
params.collapseRate = BestParameters(4);
params.startBias = BestParameters(6);
%params.nonDec = BestParameters(5);
      
SimData = simulDDM(params);
SimData.rt = SimData.rt + BestParameters(5);
    
SimData.drift = repmat(tempData.attribVals(:,1),1000,1);  % self/other  (Face house if doing separately)
SimData.drift2 = repmat(tempData.attribVals(:,2),1000,1); % drift is attribute VALUE (face and house)

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

