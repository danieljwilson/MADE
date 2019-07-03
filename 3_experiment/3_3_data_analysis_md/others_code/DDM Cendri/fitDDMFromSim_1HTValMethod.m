function [SimNLL, BestParameters] = fitDDMFromSim_1HTValMethod(subject)

pathtofile = mfilename('fullpath');
path = pathtofile(1:(regexp(pathtofile,'scripts') - 1));
model = regexp(pathtofile,'_(\d.*)','tokens');
model = model{1}{1};

simID = 'AllValues';
simInfo = load(fullfile('/Volumes','DATALOTTADATA','DVNR', 'Simulations', simID, 'simInfo.mat'));

%% load behavioral data
files = dir(fullfile(path, 'BehavioralData',subject, 'Data*mat'));
files = {files(~cellfun(@isempty,regexp({files.name},'Data.*\.\d\.mat'))).name};

ratings = dir(fullfile(path, 'BehavioralData',subject, 'Data*mat'));
if isempty(cell2mat(regexp({ratings.name},'Data.*\.AttributeRatings-Post\.mat','once')))
    ratings = {ratings(~cellfun(@isempty,regexp({ratings.name},'Data.*\.AttributeRatings-Pre\.mat'))).name};
else
    ratings = {ratings(~cellfun(@isempty,regexp({ratings.name},'Data.*\.AttributeRatings-Post\.mat'))).name};
end
    
RateData = load(fullfile(path,'BehavioralData',subject,ratings{1}));
RateData = RateData.Data;
Resp = {};
RT = {};
Health = {};
Taste = {};
TrialType = {};
for i = 1:length(files)
    load(fullfile(path, 'BehavioralData',subject, files{i}));
    Resp = [Resp, Data.Resp]; % (~cellfun(@isnan,Data.Resp))
    RT = [RT,Data.ChoiceRT]; % (~cellfun(@isnan,Data.Resp))
    for t = 1:length(Data.Resp)
        tempH{t} = str2num(RateData.Resp{strcmp(RateData.Food,Data.Food{t}) & strcmp(RateData.Attribute,'Health')});
        tempT{t} = str2num(RateData.Resp{strcmp(RateData.Food,Data.Food{t}) & strcmp(RateData.Attribute,'Taste')});
    end
    Health = [Health,tempH];
    Taste = [Taste,tempT];
    TrialType = [TrialType, Data.Instruction];
end

TrialType(strcmp(TrialType,'Respond Naturally')) = {'Nat'};
TrialType(strcmp(TrialType,'Focus on Taste')) = {'Taste'};
TrialType(strcmp(TrialType,'Focus on Health')) = {'Health'};

clear Data;
NonResp = strcmp(Resp,'NULL');
Resp(NonResp) = {NaN};
RT(NonResp) = {NaN};


Data.resp = cell2mat(Resp);% final Response
Data.resp = +(Data.resp > 2);
Data.resp(NonResp) = NaN;
Data.rt = cell2mat(RT); % final RT

Data.dim1 = 10 * cell2mat(Taste)' - 30; % taste converted into $self range
Data.dim2 = 10 * cell2mat(Health)' - 30; % health converted into $other range

%% coarse grid search for best parameters
combo.tasteW = -.008:.008:.024; %-.016:.008:.04;
combo.healthW = -.008:.008:.024; %-.016:.008:.04;
combo.upper = (10:4:34)/100;
combo.collapseRate = [0, .00025 .0005, .00075, .001, .002]; %[0, .0001, .00025 .0005, .00075, .001, .002];
combo.nonDec = .25:.25:1.25;

% create all combinations of desired variables
comboVars = fieldnames(combo);
parameterCombos = combo.(comboVars{1})';
for v = 2:length(comboVars)
    parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
        sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
end

conds =  {'Nat','Taste','Health'};
for c = 1:3
    selectedTrials = cellfun(@(x)(~isempty(regexp(x,conds{c},'once'))), TrialType);
    
    tempData.resp = Data.resp(selectedTrials);
    tempData.rt = Data.rt(selectedTrials);
    tempData.attribVals = [Data.dim1(selectedTrials) ...
                           Data.dim2(selectedTrials)];

    uniqueVals = unique(tempData.attribVals*parameterCombos(:,1:2)');  % unique drift rates
    valStruct = struct('SimData',[]);                  
    for v = 1:length(uniqueVals) % 15 secs
        valStruct(v) = load(fullfile('/Volumes','DATALOTTADATA','DVNR', 'Simulations',simID,['Val' num2str(uniqueVals(v)) '.mat']));
    end
    
    SimNLL = zeros(length(parameterCombos),1);  % matrix to save SUMMED neg. log likelihood of each parameter combo
    nLoops = numel(SimNLL); % same as rows of number of parameter combos
    
    if exist(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']), 'file')
%         delete(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']))
        load(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']))
    end
    
    if any(SimNLL(:) == 0) % run simulations if not complete yet
        
        for loop = 1:nLoops
            % check to see if a kill command has been
            % issued
            if exist(fullfile(path,['kill' model '.mat']),'file')  % to cleanly stop and then resume later
                break;
            end
            
            if SimNLL(loop) == 0
                
                % get negative log likelihood of the data for each combination of
                % parameter values
                SimNLL(loop) = NLLSimData_fromVals(tempData,parameterCombos(loop,:),valStruct,uniqueVals, simInfo.barrierCombos);
                %NLLSIMData... is for behavioral simulation data (tempdata,
                %parameter combos
                %valStruct is where the distributions have been saved
                %unique vals is for unique drift rates
                %sim info contains info on barrier combinations
                
                
                if mod(loop,10) == 0 || (loop > nLoops - 11)
                    save(fullfile(path,'BehavioralData',subject, ...
                        ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']),...
                        'SimNLL','loop');
                end
            end
%             clc;
%             fprintf('Loop %d completed: %.1f percent finished\n\n',loop,loop/nLoops * 100)
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
    params.driftRate = tempData.attribVals*BestParameters(1:2)';
    params.simsPerDrift = 1000;
    params.barrier = BestParameters(3);
    params.barrierCollapse = BestParameters(4);
    params.nonDec = BestParameters(5);
      
    SimData = simulDDM_normApproxSimResps(params);
    
    SimData.drift = reshape(repmat(tempData.attribVals(:,1),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,1),params.simsPerDrift,1)))';
    SimData.drift2 = reshape(repmat(tempData.attribVals(:,2),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,2),params.simsPerDrift,1)))';
    
    % save all parameters used in simulations
    params.candidate_driftTaste = combo.tasteW;
    params.candidate_driftHealth = combo.healthW;
    params.candidate_nondec = combo.nonDec;
    params.candidate_barrier = combo.upper;
    params.candidate_barrierCollapse = combo.collapseRate;
    params.simCode = simInfo.simCode;
    
%     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_' conds{c} '.mat']),'SimNLL',...
%         'SimData','BestParameters','params');

    save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']),'SimNLL',...
        'BestParameters','params','SimData');

end


%% finer simulation around best parameters from coarse grid search
for c = 1:3
    % get BestParameters variable from previous simulation
    courseSimData = load(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Coarse' conds{c} '.mat']));
    BestParameters = courseSimData.BestParameters;
    
    combo.tasteW = simInfo.vals.selfW(simInfo.vals.selfW >= BestParameters(1) - .008 & ...
                                 simInfo.vals.selfW <= BestParameters(1) + .008);
    combo.healthW = simInfo.vals.otherW(simInfo.vals.otherW >= BestParameters(2) - .008 & ...
                                     simInfo.vals.otherW <= BestParameters(2) + .008);
    combo.upper = simInfo.barriers.upper(simInfo.barriers.upper >= BestParameters(3) - .041 & ...
                                     simInfo.barriers.upper <= BestParameters(3) + .041);
    combo.collapseRate = [0, .00025 .0005, .00075 .001, .002];%[0, .0001, .00025 .0005, .00075 .001, .002];
    combo.nonDec = sort([(BestParameters(5) - .25):.1:(BestParameters(5) + .25), BestParameters(5)]);

    % create all combinations of desired variables
    comboVars = fieldnames(combo);
    parameterCombos = combo.(comboVars{1})';
    for v = 2:length(comboVars)
        parameterCombos = [repmat(parameterCombos, length(combo.(comboVars{v})), 1), ...
            sort(repmat(combo.(comboVars{v})',size(parameterCombos,1), 1))];
    end

    selectedTrials = cellfun(@(x)(~isempty(regexp(x,conds{c},'once'))), TrialType);
    
    tempData.resp = Data.resp(selectedTrials);
    tempData.rt = Data.rt(selectedTrials);
    tempData.attribVals = [Data.dim1(selectedTrials) ...
                           Data.dim2(selectedTrials)];

    uniqueVals = unique(tempData.attribVals*parameterCombos(:,1:2)');
    valStruct = struct('SimData',[]);                  
    for v = 1:length(uniqueVals) % 15 secs
        valStruct(v) = load(fullfile('/Volumes','DATALOTTADATA','DVNR', 'Simulations',simID,['Val' num2str(uniqueVals(v)) '.mat']));
    end
    
    SimNLL = zeros(length(parameterCombos),1);
    nLoops = numel(SimNLL);
    
    if exist(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Fine' conds{c} '.mat']), 'file')
%         delete(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Fine' conds{c} '.mat']))
        load(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Fine' conds{c} '.mat']))
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
                SimNLL(loop) = NLLSimData_fromVals(tempData,parameterCombos(loop,:),valStruct,uniqueVals, simInfo.barrierCombos);
                
                if mod(loop,10) == 0 || (loop > nLoops - 11)
                    save(fullfile(path,'BehavioralData',subject, ...
                        ['DDM_fittedResults_m' model '_Fine' conds{c} '.mat']),...
                        'SimNLL','loop');
                end
            end
%             clc;
%             fprintf('Loop %d completed: %.1f percent finished\n\n',loop,loop/nLoops * 100)
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
    params.driftRate = tempData.attribVals*BestParameters(1:2)';
    params.simsPerDrift = 1000;
    params.barrier = BestParameters(3);
    params.barrierCollapse = BestParameters(4);
    params.nonDec = BestParameters(5);
    
    SimData = simulDDM_exactSim(params);
    SimData.drift = reshape(repmat(tempData.attribVals(:,1),params.simsPerDrift,1),...
        numel(repmat(tempData.attribVals(:,1),params.simsPerDrift,1)),1);
    SimData.drift2 = reshape(repmat(tempData.attribVals(:,2),params.simsPerDrift,1),...
        numel(repmat(tempData.attribVals(:,2),params.simsPerDrift,1)),1);
    
    SimData = simulDDM_normApproxSimResps(params);
    
    SimData.drift = reshape(repmat(tempData.attribVals(:,1),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,1),params.simsPerDrift,1)))';
    SimData.drift2 = reshape(repmat(tempData.attribVals(:,2),1,params.simsPerDrift)',...
        1,numel(repmat(tempData.attribVals(:,2),params.simsPerDrift,1)))';
    
    % save all parameters used in simulations
    params.candidate_driftTaste = combo.tasteW;
    params.candidate_driftHealth = combo.healthW;
    params.candidate_nondec = combo.nonDec;
    params.candidate_barrier = combo.upper;
    params.candidate_barrierCollapse = combo.collapseRate;
    params.simCode = simInfo.simCode;
    
%     save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_' conds{c} '.mat']),'SimNLL',...
%         'SimData','BestParameters','params');

    save(fullfile(path,'BehavioralData',subject, ['DDM_fittedResults_m' model '_Fine' conds{c} '.mat']),'SimNLL',...
        'BestParameters','params','SimData');


end

