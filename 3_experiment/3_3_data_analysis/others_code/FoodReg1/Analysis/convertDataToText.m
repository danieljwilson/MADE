function convertDataToText(varargin)

if ~isempty(varargin)
    showPlots = varargin{1};
else
    showPlots = 0;
end


% subjects = input('Subject: ');
subjects = [96,98:129];
startTrial = input('Which trial to start (default = 1): ');
if isempty(startTrial)
    startTrial = 1;
end 

fileName = mfilename('fullpath');
dataPath = regexp(fileName,'.*Analysis','match');
dataPath = fullfile(dataPath{1}(1:(end - 8)), 'SubjectData/');

for s = 1:length(subjects)
    subjID = num2str(subjects(s));
    fprintf('Processing mouse data for subject %s...\n',subjID)
    
    %% Get trial data for each part
    clear Choice
    % process data for Part 1 (unregulated choice)
    load([dataPath subjID '/Data.' subjID '.ChoiceTask.mat'])
    
    if exist(fullfile(dataPath,subjID,'MouseChoice.mat'),'file')
        load(fullfile(dataPath,subjID,'MouseChoice.mat'))
    end
    
    if showPlots
        [w, rect] = Screen('OpenWindow',0, [], [1100,645,1440,900]); 
    end
    if startTrial < length(Data.Choice)
        for t = startTrial:length(Data.Choice)
            clc;
            sprintf('Processing trial %d\n\n',t)
    %         input(['View trial ' num2str(t)])
            Choice(t) = processMouseTrace_handCorrect([Data.ChoiceX{t},Data.ChoiceY{t}],Data.ChoiceTime{t},showPlots);
            save(fullfile(dataPath,subjID,'MouseChoice.mat'),'Choice');
        end 
    end    
    % load pre-task rating data
    PreRating = load([dataPath subjID '/Data.' subjID '.AttributeRatings-Pre.mat']);

    %% Print mouse trace trial data to .txt file
    
    % delete file if it already exists (avoids appending each time this is
    % run)
    if exist([dataPath subjID '/MouseTracePerChoice_' subjID '.txt'],'file')
        delete([dataPath subjID '/MouseTracePerChoice_' subjID '.txt'])
    end
    
    fid = fopen([dataPath subjID '/MouseTracePerChoice_' subjID '.txt'],'a');
    
    fprintf(fid, ['Subject\tTrial\t' ...
                  'TimePt\tTime\tChoiceX\tChoiceSignedX\tChoiceY\tDrx\tTrajectory\n']);
    
    % print info for choice task
    for trial = 1:length(Choice) % for each trial
        for m = 1:length(Choice(trial).normX) % for each mouse sample
            fprintf(fid, '%s\t%d\t',subjID, trial);
            
            fprintf(fid, '%d\t%.3f\t%.4f\t%.4f\t%.4f\t%d\t%.4f\n', ...
                    m,Choice(trial).tracetime(m),Choice(trial).normX(m),...
                    Choice(trial).normXSigned(m), Choice(trial).normY(m),...
                    Choice(trial).currentDrx(m),Choice(trial).normedTrajectory2(m));
        end

    end
    
    
    
    fclose(fid);
    
    %% Print mouse trace trial data interpolated to 100 pts to .txt file
    
    % delete file if it already exists (avoids appending each time this is
    % run)
    if exist([dataPath subjID '/MouseTrace100PerChoice_' subjID '.txt'],'file')
        delete([dataPath subjID '/MouseTrace100PerChoice_' subjID '.txt'])
    end
    
    fid = fopen([dataPath subjID '/MouseTrace100PerChoice_' subjID '.txt'],'a');
    
    fprintf(fid, ['Subject\tTrial\t' ...
                  'TimePt\tChoiceX\tChoiceSignedX\tChoiceY\tDrx\tTrajectory\n']);
    
    % print info for choice task
    for trial = 1:length(Choice) % for each trial
        for m = 1:length(Choice(trial).normX100) % for each mouse sample
            fprintf(fid, '%s\t%d\t',subjID, trial);
            fprintf(fid, '%d\t%.4f\t%.4f\t%.4f\t%d\t%.4f\n', ...
                    m,Choice(trial).normX100(m),Choice(trial).normXSigned100(m),...
                    Choice(trial).normY100(m),Choice(trial).currentDrx100(m),...
                    Choice(trial).normedTrajectory2100(m));
        end

    end
    
    fclose(fid);
    
    %% Print trial-by-trial variables to separate .txt file
   
    fprintf('Processing trial data for subject %s...\n',subjID)
    
    % delete file if it already exists (avoids appending each time this is
    % run)
    if exist([dataPath subjID '/ChoiceData_' subjID '.txt'],'file')
        delete([dataPath subjID '/ChoiceData_' subjID '.txt'])
    end
    
    fid = fopen([dataPath subjID '/ChoiceData_' subjID '.txt'],'a');
    
    headers = {'Subject','Trial','Instruction','Food','Liking','Taste','Health','Amount' ...
            'Choice','ChoiceRT','FirstDevTimeChoice',...    
            'InitAngleChoice','NumChangeMindChoice','FinalDevTimeChoice','MaxVelocityChoice',...
            'DrxFirstDevChoice','TotalAUCChoice','AUCtoNonChosenChoice',...
            'AUCtoChosenChoice','MaxDevChoice'};
    % print vars at top of file
    for h = 1:length(headers) - 1
        fprintf(fid,'%s\t',headers{h});
    end
    
    fprintf(fid,'%s\n',headers{end});
    
    % print info 
    colVars = {'Data.subjid','t','Data.InstructionOnTrial{t}','FoodStem',...
               'Liking','Taste','Health','Amount',...
               'Data.Choice{t}','Data.ChoiceTime{t}(end)',...
               'Choice(t).firstDeviation','Choice(t).initialAngle','Choice(t).nChangeMind',...
               'Choice(t).timeFinalChoice','Choice(t).maxVelocity',...
               'Choice(t).drxFirstDev','Choice(t).AUCTotal',...
               'Choice(t).AUCToNonChosen','Choice(t).AUCToChosen','Choice(t).maxDev'...
               };
    
    for t = 1:length(Data.Choice) % for each trial
        Health = PreRating.Data.Resp{strcmp(PreRating.Data.Attribute,'Health') ...
            & strcmp(PreRating.Data.Food,Data.FoodOnTrial{t})};
        Taste = PreRating.Data.Resp{strcmp(PreRating.Data.Attribute,'Taste') ...
            & strcmp(PreRating.Data.Food,Data.FoodOnTrial{t})};
        Liking = PreRating.Data.Resp{strcmp(PreRating.Data.Attribute,'Liking') ...
            & strcmp(PreRating.Data.Food,Data.FoodOnTrial{t})};
        
        if mod(Data.subjid,2) == 0
            Data.InstructionOnTrial(strcmp(Data.InstructionOnTrial,'Decrease Desire')) = {'Focus on Health'};
        end
        
        if mod(Data.subjid,2) == 1
            Data.InstructionOnTrial(strcmp(Data.InstructionOnTrial,'Focus on Health')) = {'Decrease Desire'};
        end
        
        FoodStem = Data.FoodOnTrial{t}(1:(regexp(Data.FoodOnTrial{t},'_','once') - 1));
        Amount = Data.FoodOnTrial{t}(regexp(Data.FoodOnTrial{t},'_','once') + 1);
        
        for c = 1:length(colVars) - 1
            eval(['v = ' colVars{c} ';']);
            printvar(v,fid,'\t');
        end
        eval(['v = ' colVars{c + 1} ';']);
        printvar(v,fid,'\n');

    end
    
    
%% Process rating data independently
    fprintf('Processing ratings data for subject %s...\n',subjID)
    if exist([dataPath subjID '/RatingDataForGLM_' subjID '.txt'],'file')
        delete([dataPath subjID '/RatingDataForGLM_' subjID '.txt'])
    end


    fid = fopen([dataPath subjID '/RatingDataForGLM_' subjID '.txt'],'a');

    headers = {'Subject','Block','Trial','Attribute','Food','Rating','RT'};
    % print vars at top of file
    for h = 1:length(headers) - 1
        fprintf(fid,'%s\t',headers{h});
    end

    fprintf(fid,'%s\n',headers{end});

    colVars = {'PreRating.Data.subjid','Block',...
        't','PreRating.Data.Attribute{t}','PreRating.Data.Food{t}',...
        'PreRating.Data.Resp{t}','PreRating.Data.RT{t}',};

    for t = 1:length(PreRating.Data.Food)
        if strcmp(PreRating.Data.Attribute{t},PreRating.Data.Attribute{1})
            Block = 1;
        else
            Block = 2;
        end

        for c = 1:length(colVars) - 1
                eval(['v = ' colVars{c} ';']);
                printvar(v,fid,'\t');
        end
        eval(['v = ' colVars{c + 1} ';']);
        printvar(v,fid,'\n');
    end
    
    fclose(fid);
    
end

function printvar(var,fid,endCap)
    if isempty(var) || any(isnan(var))
        var = 'NA';
    end
    varInfo = whos('var');
    
    switch varInfo.class
        case 'char'
            fprintf(fid,['%s' endCap],var);
        case 'logical'
            fprintf(fid,['%d' endCap],var);
        otherwise
            fprintf(fid,['%.4f' endCap],var);
    end
    