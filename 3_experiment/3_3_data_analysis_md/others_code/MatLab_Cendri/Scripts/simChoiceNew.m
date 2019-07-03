% USED TO PLOT!!

pathtofile = mfilename('fullpath');
path = pathtofile(1:(regexp(pathtofile,'scripts') - 1))
subjNameList = [6:24, 26:28, 29:34, 36:40];
% 25 and 29 excluded for saying no 100% of the time

        
model = input('Which model?: ','s');
cond = input('Which condition?: ','s');
clear AllParams;

condnames = {'Short' 'Long'};
for s = 1:length(subjNameList)
    
    subject = num2str(subjNameList(s))
    Results.subject{s} = subject;
    
    ddmFile = fullfile(path,'FittedResults',model, ['DDM_fittedResults_m' model '_' subject '_' cond '.mat']);
    
    if exist(ddmFile,'file')
        load(ddmFile);
        if ~isfield(SimData,'drift')
            SimData.drift = SimData.dim1;
            SimData.drift2 = SimData.dim2;
        end
        
        AllParams(s,:) = BestParameters;
        
        load(fullfile(path,'SubjectData',subject,['Data.' subject '.choice.mat']))

        NonResp = cellfun(@(x)strcmp(x,'NULL'),Data.Resp);
        Data.Resp(NonResp) = {NaN};
        Data.Resp = +(cell2mat(Data.Resp) == 2);
        Data.Resp(NonResp) = NaN;

        Resp = Data.Resp;
        %NonResp = strcmp(Resp,'NULL');
        RT = cell2mat(Data.ChoiceRT);
        %Resp(NonResp) = {NaN};
        %RT(NonResp) = {NaN};
        TrialType = cell2mat(Data.TimeLimit);
        SelfAmount = cell2mat(Data.SelfProposal) - 10;
        OtherAmount = cell2mat(Data.OtherProposal) - 10;

        clear Data;
        SimData.resp = +SimData.resp;
        
        if strcmp(cond, 'Short')
            TimeLimit = 2;
        else
            TimeLimit = 10;
        end
        
        SimData.resp(SimData.rt > TimeLimit) = NaN;
%         SimData.switchOccurred(SimData.rt > 4) = NaN;
        SimData.rt(SimData.rt > TimeLimit) = NaN;
        %SimData.resp = SimData.resp > 0;

        selectedTrials = TrialType == TimeLimit;
        Results.SimData{s} = SimData;
        Data1(s).resp = Resp(~NonResp & selectedTrials);% final Response
        Results.numNonResp(s) = sum(NonResp);
        Data1(s).rt = RT(~NonResp & selectedTrials); % final RT

        Data1(s).dim1 = SelfAmount(~NonResp & selectedTrials)'; % taste
        Data1(s).dim2 = OtherAmount(~NonResp & selectedTrials)'; % health

        Data1(s).Pred = NaN * zeros(1,length(Data1(s).dim1));
        Data1(s).PredError = NaN * zeros(1,length(Data1(s).dim1));
        for t = 1:length(Data1(s).PredError)
            PredictedProb = nanmean(SimData.resp(SimData.drift == Data1(s).dim1(t) & ...
                                                 SimData.drift2 == Data1(s).dim2(t)));
            Data1(s).Pred(t) = PredictedProb;
            Data1(s).PredError(t) = Data1(s).resp(t) - PredictedProb;
            Data1(s).PredRT(t) = nanmean(SimData.rt(SimData.drift == Data1(s).dim1(t) & ...
                                                 SimData.drift2 == Data1(s).dim2(t)));
        end
        Results.MeanPredError(s) = nanmean(abs(Data1(s).PredError));

        fprintf('Mean RT = %f\n',nanmean(Data1(s).rt))
        fprintf('Predicted RT = %f\n',nanmean(SimData.rt))

        GChoiceSim = ((SimData.resp - .5) .* (SimData.drift2 - SimData.drift)) > 0;
%         mean(HChoiceSim)
        GChoiceRT = nanmean(SimData.rt(GChoiceSim));
        SChoiceRT = nanmean(SimData.rt(~GChoiceSim));

        GChoiceObs = (((Data1(s).resp - .5)' .* Data1(s).dim2 - Data1(s).dim1) >     0);
%         mean(GChoiceObs)
        GChoiceRTObs = nanmean(Data1(s).rt(GChoiceObs));
        SChoiceRTObs = nanmean(Data1(s).rt(~GChoiceObs));

        Results.AcceptanceObs(s) = nanmean(Data1(s).resp);
        Results.AcceptancePred(s) = nanmean(SimData.resp);
        Results.RTAcceptObs(s) = nanmean(Data1(s).rt(Data1(s).resp == 1));
        Results.RTRejectObs(s) = nanmean(Data1(s).rt(Data1(s).resp == 0));
        Results.RTAcceptSim(s) = nanmean(SimData.rt(SimData.resp == 1));
        Results.RTRejectSim(s) = nanmean(SimData.rt(SimData.resp == 0));
        Results.GChoiceSim(s) = nanmean(GChoiceSim);
        Results.GChoiceRTSim(s) = GChoiceRT;
        Results.SChoiceRTSim(s) = SChoiceRT;
        Results.PredictedRT(s) = nanmean(SimData.rt);

        Results.GChoiceObs(s) = mean(GChoiceObs);
        Results.GChoiceRTObs(s) = GChoiceRTObs;
        Results.SChoiceRTObs(s) = SChoiceRTObs;
        Results.ObservedRT(s) = nanmean(Data1(s).rt);
        Results.ObservedRTVar(s) = nanstd(Data1(s).rt);
        Results.SimRTVar(s) = nanstd(SimData.rt);
%         Results.AveAUC(s) = nanmean(SimData.AUC(~isnan(SimData.rt)));
%         Results.AveGChoiceAUC(s) = nanmean(SimData.AUC(~isnan(SimData.rt) & GChoiceSim == 1));
%         Results.AveSChoiceAUC(s) = nanmean(SimData.AUC(~isnan(SimData.rt) & GChoiceSim == 0));
        
%         Results.AveAUC2(s) = nanmean(SimData.AUC(~isnan(SimData.rt)));
%         Results.AveGChoiceAUC2(s) = nanmean(SimData.AUC2(~isnan(SimData.rt) & GChoiceSim == 1));
%         Results.AveSChoiceAUC2(s) = nanmean(SimData.AUC2(~isnan(SimData.rt) & GChoiceSim == 0));


        beta = glmfit([Data1(s).dim1 Data1(s).dim2], Data1(s).resp', 'binomial','logit');
        
        Results.InterceptObs(s) = beta(1);
        Results.SelfBetaObs(s) = beta(2);
        Results.OtherBetaObs(s) = beta(3);
        
        beta = glmfit([SimData.drift, SimData.drift2], SimData.resp, 'binomial','logit');
        
        Results.InterceptSim(s) = beta(1);
        Results.SelfBetaSim(s) = beta(2);
        Results.OtherBetaSim(s) = beta(3);
        
        NLLBest = min(SimNLL(:));
        Results.NLL(s) = NLLBest;
%         [Results.AIC(s) Results.BIC(s)] = aicbic(-1 * NLLBest,size(AllParams,2),length(Data1(s).rt));
    else
        AllParams(s,:) = NaN*zeros(1,5);
    end
end

f = figure('Name','Ave Acceptance Rate');
scatter(Results.AcceptanceObs,Results.AcceptancePred)
hold on;
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

f = figure('Name','Ave Generous Choice');
scatter(Results.GChoiceObs,Results.GChoiceSim)
hold on;
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

f = figure('Name','Ave. RT');
scatter(Results.ObservedRT,Results.PredictedRT')
hold on;
pause(1)
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

f = figure('Name','Ave. RT Variability');
scatter(Results.ObservedRTVar,Results.SimRTVar)
hold on;
pause(1)
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

f = figure('Name','Ave. Generous RT');
scatter(Results.GChoiceRTObs,Results.GChoiceRTSim)
hold on;
pause(1)
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

f = figure('Name','Ave. Selfish RT');
scatter(Results.SChoiceRTObs,Results.SChoiceRTSim)
hold on;
pause(1)
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

f = figure('Name','Ave. GvS RT');
scatter(Results.GChoiceRTObs - Results.SChoiceRTObs,Results.GChoiceRTSim - Results.SChoiceRTSim)
hold on;
pause(1)
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')


mean(Results.GChoiceRTSim)
mean(Results.SChoiceRTSim)
[h p] = ttest(Results.GChoiceRTSim,Results.SChoiceRTSim)

mean(Results.GChoiceRTObs)
mean(Results.SChoiceRTObs)
[h p] = ttest(Results.GChoiceRTObs,Results.SChoiceRTObs)

corrcoef(Results.GChoiceSim(~isnan(Results.GChoiceRTSim)),...
            Results.GChoiceRTSim(~isnan(Results.GChoiceRTSim))...
            - Results.SChoiceRTSim(~isnan(Results.SChoiceRTSim)))
corrcoef(Results.GChoiceObs, Results.GChoiceRTObs - Results.SChoiceRTObs)
% 
% figure('Position', [100,100,900,700],'Name','Model value vs Sim and Obs Acceptance')
% obsResp = zeros(length(subjNameList),10);
% simResp = zeros(length(subjNameList),10);
% for s = 1:length(subjNameList)
%     temp = Results.SimData{s};
%     Pairs = unique([temp.drift,temp.drift2],'rows');
%     ProbYes = zeros(size(Pairs,1),1);
%     for p = 1:size(Pairs,1)
%         ProbYes(p) = nanmean(temp.resp(temp.drift == Pairs(p,1) & temp.drift2 == Pairs(p,2)) == 1);        
%     end
%     
%     binEdges = linspace(min(ProbYes),max(ProbYes),11);
%     [h,whichBin] = histc(ProbYes, binEdges);
%     
%     
%     for b = 1:10
%         matchingTrials = ismember([Data1(s).dim1,Data1(s).dim2],Pairs(whichBin == b,:),'rows');
%         obsResp(s,b) = nanmean(Data1(s).resp(matchingTrials));
%         matchingTrials = ismember([temp.drift,temp.drift2],Pairs(whichBin == b,:),'rows');
%         simResp(s,b) = nanmean(temp.resp(matchingTrials) == 1);
%     end
%     f = subplot(7,8,s);
%     hold on;
%     scatter(simResp(s,:),obsResp(s,:),20,'fill')
%     set(f,'XLimMode','manual','YlimMode','manual')
%     plot(get(f,'XLim'),get(f,'XLim'),'--')
%     hold off;
% end


figure('Position', [100,100,900,700],'Name','Model vs. Subject Prob of Acceptance')
obsResp = zeros(length(subjNameList),10);
simResp = zeros(length(subjNameList),10);
AvePredErrorChoice = zeros(length(subjNameList),1);
AveCorrChoice = NaN*zeros(length(subjNameList),1);
AveCorrChoice2 = NaN*zeros(length(subjNameList),1);
for s = 1:length(subjNameList)
    temp = Results.SimData{s};
    if ~isempty(temp)
        Pairs = unique([temp.drift,temp.drift2],'rows');
        ProbYes = zeros(size(Pairs,1),1);
        ProbYesObs = ProbYes;
        for p = 1:size(Pairs,1)
            ProbYes(p) = nanmean(temp.resp(temp.drift == Pairs(p,1) & temp.drift2 == Pairs(p,2)) == 1); 
            ProbYesObs(p) = nanmean(Data1(s).resp(Data1(s).dim1 == Pairs(p,1) & Data1(s).dim2 == Pairs(p,2)) == 1);
        end

        binEdges = linspace(min(ProbYes),max(ProbYes),11);
        [h,whichBin] = histc(ProbYes, binEdges);


        for b = 1:10
            matchingTrials = ismember([Data1(s).dim1,Data1(s).dim2],Pairs(whichBin == b,:),'rows');
            obsResp(s,b) = nanmean(Data1(s).resp(matchingTrials));
            matchingTrials = ismember([temp.drift,temp.drift2],Pairs(whichBin == b,:),'rows');
            simResp(s,b) = nanmean(temp.resp(matchingTrials) == 1);
        end
        f = subplot(7,8,s);
        hold on;
        scatter(simResp(s,:),obsResp(s,:),20,'fill')
        AvePredErrorChoice(s) = nanmean(simResp(s,:) - obsResp(s,:));
        missingPts = isnan(obsResp(s,:));
        temp = corrcoef(simResp(s,~missingPts),obsResp(s,~missingPts));
        AveCorrChoice(s) = temp(2);
        
        missingPts = isnan(ProbYesObs);
        temp = corrcoef(ProbYes(~missingPts),ProbYesObs(~missingPts));
        AveCorrChoice2(s) = temp(2);
        set(f,'XLimMode','manual','YlimMode','manual')
        plot(get(f,'XLim'),get(f,'XLim'),'--')
        hold off;
    end
end

f = figure('Name','Average Model vs. Subject Acceptance Prob');
scatter(nanmean(simResp,1),nanmean(obsResp,1),'fill')
hold on
errorbar(nanmean(simResp,1),nanmean(obsResp,1),nanstd(obsResp,1)/sqrt(33),'.')
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')



% ave Resps v2
figure('Position', [100,100,900,700],'Name','Model vs. Subject Prob of Acceptance, v2')
selfMidPts = [2, 6, 10, 14, 18] - 10;
obsResp = zeros(length(subjNameList),5);
simResp = zeros(length(subjNameList),5);
percObs = zeros(length(subjNameList),5);
AveCorrChoice5Pts = NaN*zeros(length(subjNameList),1);
for s = 1:length(subjNameList)
    temp = Results.SimData{s};
    if ~isempty(temp)
        for b = 1:5
            matchingTrials = Data1(s).dim1 >= selfMidPts(b) - 2 & Data1(s).dim1 <= selfMidPts(b) + 2;
            obsResp(s,b) = nanmean(Data1(s).resp(matchingTrials));
            matchingTrials = temp.drift >= selfMidPts(b) - 2 & temp.drift <= selfMidPts(b) + 2;
            simResp(s,b) = nanmean(temp.resp(matchingTrials) == 1);
            percObs(s,b) = mean(matchingTrials);
        end
        f = subplot(6,6,s);
        hold on;
        scatter(obsResp(s,:),simResp(s,:),20,'fill')
        missingPts = isnan(obsResp(s,:));
        temp = corrcoef(simResp(s,~missingPts),obsResp(s,~missingPts));
        AveCorrChoice5Pts(s) = temp(2);
        
        set(f,'XLimMode','manual','YlimMode','manual')
        plot(get(f,'XLim'),get(f,'XLim'),'--')
        hold off;
    end
end

f = figure('Name','Average Model vs. Subject Acceptance Prob, v2');
scatter(nanmean(simResp,1),nanmean(obsResp,1),'fill')
hold on
errorbar(nanmean(simResp,1),nanmean(obsResp,1),nanstd(obsResp,1)/sqrt(33),'.')
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')





figure('Position', [100,100,900,700], 'Name', 'Model vs. Subject RT');
obsRT = zeros(length(subjNameList),10);
simRT = zeros(length(subjNameList),10);
AveCorrRT = zeros(length(subjNameList),1);
for s = 1:length(subjNameList)
    temp = Results.SimData{s};
    if ~isempty(temp)
%         Pairs = unique([temp.drift,temp.drift2],'rows');
        Pairs = unique([Data1(s).dim1,Data1(s).dim2],'rows');
        AveRTs = zeros(size(Pairs,1),1);
        AveObsRT = zeros(size(Pairs,1),1);
        for p = 1:size(Pairs,1)
            AveRTs(p) = nanmean(temp.rt(temp.drift == Pairs(p,1) & temp.drift2 == Pairs(p,2))); 
            AveObsRT(p) = nanmean(Data1(s).rt(Data1(s).dim1 == Pairs(p,1) & Data1(s).dim2 == Pairs(p,2)));    
        end

        binEdges = linspace(min(AveRTs),max(AveRTs),10);
        [h,whichBin] = histc(AveRTs, binEdges);


        for b = 1:10
            matchingTrials = ismember([Data1(s).dim1,Data1(s).dim2],Pairs(whichBin == b,:),'rows');
            obsRT(s,b) = nanmean(Data1(s).rt(matchingTrials));
            matchingTrials = ismember([temp.drift,temp.drift2],Pairs(whichBin == b,:),'rows');
            simRT(s,b) = nanmean(temp.rt(matchingTrials));
        end
        f = subplot(8,7,s);
        hold on;
        scatter(simRT(s,:),obsRT(s,:),20,'fill')
    %     set(f,'XLimMode','manual','YlimMode','manual')
        plot(get(f,'XLim'),get(f,'XLim'),'--')
        hold off;

        missingPts = isnan(obsRT(s,:));
        temp = corrcoef(simRT(s,~missingPts),obsRT(s,~missingPts));
        AveCorrRT(s) = temp(2);
        missingPts = isnan(AveObsRT);
        temp = corrcoef(AveObsRT(~missingPts),AveRTs(~missingPts));
        AveCorrRT2(s) = temp(2);
    end
end

f = figure('Name','Average Model vs. Subject RT');
scatter(nanmean(simRT,1),nanmean(obsRT,1),'fill')
hold on
errorbar(nanmean(simRT,1),nanmean(obsRT,1),nanstd(obsRT,1)/sqrt(43),'.')
pause(1)
set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')

Results.AveCorrChoice = AveCorrChoice;
Results.AveCorrChoice2 = AveCorrChoice2;
Results.AveCorrRT = AveCorrRT;
Results.AveCorrRT2 = AveCorrRT2;


% figure('Position', [100,100,900,700], 'Name', 'Model vs. Subject RT');
% obsRT = zeros(length(subjNameList),10);
% simRT = zeros(length(subjNameList),10);
% AveCorrRT = zeros(length(subjNameList),1);
% for s = 1:length(subjNameList)
%     temp = Results.SimData{s};
%     if ~isempty(temp)
% %         Pairs = unique([temp.drift,temp.drift2],'rows');
%         Pairs = unique([Data1(s).dim1,Data1(s).dim2],'rows');
%         AveRTs = zeros(size(Pairs,1),1);
%         AveObsRT = zeros(size(Pairs,1),1);
%         for p = 1:size(Pairs,1)
%             AveRTs(p) = nanmean(temp.rt(temp.drift == Pairs(p,1) & temp.drift2 == Pairs(p,2))); 
%             AveObsRT(p) = nanmean(Data1(s).rt(Data1(s).dim1 == Pairs(p,1) & Data1(s).dim2 == Pairs(p,2)));    
%         end
% 
%         binEdges = linspace(min(AveRTs),max(AveRTs),10);
%         [h,whichBin] = hist(Data1(s).rt);
%         
% 
% 
%         for b = 1:10
%             matchingTrials = ismember([Data1(s).dim1,Data1(s).dim2],Pairs(whichBin == b,:),'rows');
%             obsRT(s,b) = nanmean(Data1(s).rt(matchingTrials));
%             matchingTrials = ismember([temp.drift,temp.drift2],Pairs(whichBin == b,:),'rows');
%             simRT(s,b) = nanmean(temp.rt(matchingTrials));
%         end
%         f = subplot(8,7,s);
%         hold on;
%         scatter(simRT(s,:),obsRT(s,:),20,'fill')
%     %     set(f,'XLimMode','manual','YlimMode','manual')
%         plot(get(f,'XLim'),get(f,'XLim'),'--')
%         hold off;
% 
%         missingPts = isnan(obsRT(s,:));
%         temp = corrcoef(simRT(s,~missingPts),obsRT(s,~missingPts));
%         AveCorrRT(s) = temp(2);
%         missingPts = isnan(AveObsRT);
%         temp = corrcoef(AveObsRT(~missingPts),AveRTs(~missingPts));
%         AveCorrRT2(s) = temp(2);
%     end
% end
% 
% f = figure('Name','Average Model vs. Subject RT, Per Trial');
% scatter(nanmean(simRT,1),nanmean(obsRT,1),'fill')
% hold on
% errorbar(nanmean(simRT,1),nanmean(obsRT,1),nanstd(obsRT,1)/sqrt(43),'.')
% pause(1)
% set(get(f,'CurrentAxes'),'XLimMode','manual','YlimMode','manual')
% line(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'LineStyle','--')
% 
% 
% TrialPairs = {[-2,-2; -2,-1; -2,0; -1,-1; -1,0; 0,0] * 5, ...
%               [0,2; -1,2; -1,1; -2,0; -2,1; -2,2] * 5, ...
%               [0,0; 0,-1; 0,-2; -1,-1; -1,-2; -2,-2] * 5, ...
%               [0, 0; -1, 0; -2,0; 0, 1; -1, 1; 0,2] * 5, ...
%               [2,0; 1,0; 1,-1; 0,0; 0,-1; 0,-2] * 5, ...
%               [2,2; 1,2; 1,1; 0,2; 0,1; 0,0] * 5, ...
%               [2,-2; 2,-1; 2,0; 1,-2; 1, -1; 0,-2] * 5, ...
%               [2,2; 2,1; 2,0; 1,1; 1,0; 0,0] * 5};
% ObservedAcceptance = NaN * zeros(size(TrialPairs,2),length(subjNameList));
% SimulatedAcceptance = NaN * zeros(size(TrialPairs,2),length(subjNameList));
% 
% ObservedTrialRT = NaN * zeros(size(TrialPairs,2),length(subjNameList));
% SimulatedTrialRT = NaN * zeros(size(TrialPairs,2),length(subjNameList));
% CorrAcceptance = zeros(length(subjNameList),1);
% CorrRT = zeros(length(subjNameList),1);
% 
% for p = 1:size(TrialPairs,2)
%     for s = 1:length(subjNameList)
%         temp = ismember([Data1(s).dim1, Data1(s).dim2],TrialPairs{p}, 'rows');
%         selectedTrials = temp & ~isnan(Data1(s).rt');
%     
%         ObservedAcceptance(p,s) = mean(Data1(s).resp(selectedTrials));
%         ObservedTrialRT(p,s) = mean(Data1(s).rt(selectedTrials));  
%         
%         temp = ismember([Results.SimData{s}.drift, Results.SimData{s}.drift2], TrialPairs{p},'rows');
%         selectedTrials = temp & ~isnan(Results.SimData{s}.resp);
%                
%         SimulatedAcceptance(p,s) = mean(Results.SimData{s}.resp(selectedTrials));
%         SimulatedTrialRT(p,s) = ObservedAcceptance(p,s) * nanmean(Results.SimData{s}.rt(selectedTrials & Results.SimData{s}.resp == 1)) ...
%             + (1 - ObservedAcceptance(p,s)) * nanmean(Results.SimData{s}.rt(selectedTrials & Results.SimData{s}.resp == 0));
%     end
%     
%     
% end
% % 
% % for s = 1:length(subjNameList)
% %     temp = corrcoef(ObservedAcceptance(:,s),SimulatedAcceptance(:,s));
% %     CorrAcceptance(s) = temp(2);
% %     
% %     temp = corrcoef(ObservedTrialRT(:,s),SimulatedTrialRT(:,s));
% %     CorrRT(s) = temp(2);
% % end
% % 
% f = figure('Name','Average Model vs. Subject Acceptance: Per Trial');
% scatter(nanmean(SimulatedAcceptance,2),nanmean(ObservedAcceptance,2),'fill')
% hold on
% errorbar(nanmean(SimulatedAcceptance,2),nanmean(ObservedAcceptance,2),nanstd(ObservedAcceptance')/sqrt(43),'.')
% pause(.5)
% plot(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'--')
% 
% f = figure('Name','Average Model vs. Subject RT: Per Trial');
% scatter(nanmean(SimulatedTrialRT,2),nanmean(ObservedTrialRT,2),'fill')
% hold on
% errorbar(nanmean(SimulatedTrialRT,2),nanmean(ObservedTrialRT,2),nanstd(ObservedTrialRT')/sqrt(43),'.')
% pause(.5)
% plot(get(get(f,'CurrentAxes'),'XLim'),get(get(f,'CurrentAxes'),'XLim'),'--')

% 
% % figure('Position', [100,100,900,700],'Name','RT Histogram')
% % for s = 1:length(subjNameList)
% %     
% %     f = subplot(7,8,s);
% %     hist(Data1(s).rt)
% % end
% % 
% % figure('Position', [100,100,900,700],'Name','RT Histogram')
% % for s = 1:length(subjNameList)
% %     
% %     f = subplot(7,8,s);
% %     hist(Results.SimData{s}.rt)
% % end
% % 
% 
% % meanGDDMs = zeros(length(subjNameList),2200);
% % meanSDDMs = zeros(length(subjNameList),2200);
% % for s = 1:length(subjNameList)
% %     subplot(5,5,s)
% %     SimData = Results.SimData{s};
% %     GChoiceSim = (SimData.resp .* (SimData.drift - SimData.drift2)) < 0;
% %     GChoiceSim = GChoiceSim(round(linspace(1,length(SimData.resp),length(SimData.resp)*.1)));
% %     TempResp = SimData.resp(round(linspace(1,length(SimData.resp),length(SimData.resp)*.1)));
% %     
% %     DDMs = mean(bsxfun(@rdivide,SimData.ddms(GChoiceSim,:),TempResp(GChoiceSim)),1);
% %     plot(DDMs)
% %     DDMs = DDMs(DDMs > 0);
% %     meanGDDMs(s,:) = DDMs(1:2200);
% %     
% %     hold on;
% %     DDMs = mean(bsxfun(@rdivide,SimData.ddms(~GChoiceSim,:),TempResp(~GChoiceSim)),1);
% %     plot(DDMs,'r')
% %     DDMs = DDMs(DDMs > 0);
% %     meanSDDMs(s,:) = DDMs(1:2200);  
% % end
% 
% if isfield(Results.SimData{1},'switchOccurred')
%     GSwitchLikelihood = zeros(s,1);
%     SSwitchLikelihood = zeros(s,1);
% end
% GErrorLikelihood = zeros(s,1);
% SErrorLikelihood = zeros(s,1);
% ErrorLikelihood = zeros(s,1);
% ObsErrorLikelihood = zeros(s,1);
% ObsGErrorLikelihood = zeros(s,1);
% ObsSErrorLikelihood = zeros(s,1);
% for s = 1:length(subjNameList)
%     GChoiceSim = ((Results.SimData{s}.resp - .5) .* ...
%         (Results.SimData{s}.drift - Results.SimData{s}.drift2)) < 0;
%     CorrectChoice = zeros(length(GChoiceSim),1);
%     CorrectChoice((Results.SimData{s}.drift * AllParams(s,1) + Results.SimData{s}.drift2 * AllParams(s,2)) > 0) = 1;    
%     ErrorLikelihood(s) = nanmean(Results.SimData{s}.resp ~= CorrectChoice);
%     GErrorLikelihood(s) = nanmean(Results.SimData{s}.resp(GChoiceSim) ~= CorrectChoice(GChoiceSim));
%     SErrorLikelihood(s) = nanmean(Results.SimData{s}.resp(~GChoiceSim) ~= CorrectChoice(~GChoiceSim));
%     
% %     if isfield(Results.SimData{1},'switchOccurred')
% %         GSwitchLikelihood(s) = nanmean(Results.SimData{s}.switchOccurred(GChoiceSim'));
% %         SSwitchLikelihood(s) = nanmean(Results.SimData{s}.switchOccurred(~GChoiceSim'));
% %     end
% %     
%     GChoiceObs = ((Data1(s).resp - .5)' .* (Data1(s).dim1 - Data1(s).dim2)) < 0;
%     CorrectChoice = zeros(length(Data1(s).resp),1);
%     CorrectChoice((Data1(s).dim1 * AllParams(s,1) + Data1(s).dim2 * AllParams(s,2)) > 0) = 1;
%     ObsErrorLikelihood(s) = nanmean(Data1(s).resp ~= CorrectChoice');
%     ObsGErrorLikelihood(s) = nanmean(Data1(s).resp(GChoiceObs) ~= CorrectChoice(GChoiceObs)');
%     ObsSErrorLikelihood(s) = nanmean(Data1(s).resp(~GChoiceObs) ~= CorrectChoice(~GChoiceObs)');
% end
% 
% % fid = fopen(fullfile(path, 'Simulations', ['DDM1' cond '_fittedPreds.txt']),'a');
% % fprintf(fid,'Subject\tTrial\tSelfProposal\tOtherProposal\tPred\tPredRT\n');
% % 
% % for s = 1:length(subjNameList)
% %     for t = 1:length(Data1(s).resp)
% %         fprintf(fid,'%s\t%d\t%d\t%d\t%f\t%f\n',subjNameList{s},t,...
% %                 Data1(s).dim1(t) + 20,Data1(s).dim2(t) + 20, ...
% %                 Data1(s).Pred(t), Data1(s).PredRT(t));
% %     end
% % end
% % fclose(fid);