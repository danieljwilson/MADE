setwd('~/Desktop/Dropbox/Experiments/FoodReg1/')
source('~/Desktop/Dropbox/General/Rscripts/detachDataRS.R')$value() # clear out the workspace
rm(list = ls())
source('~/Desktop/Dropbox/General/Rscripts/lineanderrbars.R')
source('~/Desktop/Dropbox/General/Rscripts/PrettyBarPlots.R')

pck = c('nlme','MASS','ggplot2','logistf','lme4','Hmisc','fields','colorRamps','R.matlab','RColorBrewer','Cairo')
temp = lapply(pck,library,character.only=T)
rm(list = c('temp','pck'))

load('~/Desktop/Dropbox/Experiments/FoodReg1/Analysis/FoodReg1.RData')
subjNames = c(1,2,4:9, 11, 13:21,23:46, 49:50, 52:69,72:87,89:93,95:127,129)
nSubjects = length(subjNames)
source('Analysis/LoadSubjectData.R')
source('Analysis/ProcessPerSubjectData.R')

  
summary(lme(Choice ~ Taste + Amount + Health + Liking, random = ~1|Subject, na.action = na.omit
            , data = subset(ChoiceData, Instruction == 'Decrease Desire')))
summary(lme(Choice ~ Taste + Amount + Health + Liking, random = ~1|Subject, na.action = na.omit
            , data = subset(ChoiceData, Subject %% 2 == 1 & Instruction == 'Respond Naturally')))
summary(lme(Choice ~ Taste + Amount + Health + Liking, random = ~1|Subject, na.action = na.omit
            , data = subset(ChoiceData, Instruction == 'Focus on Health')))
summary(lme(Choice ~ Taste + Amount + Health + Liking, random = ~1|Subject, na.action = na.omit
            , data = subset(ChoiceData, Subject %% 2 == 0 & Instruction == 'Respond Naturally')))

summary(lme(Choice ~ Instruction*Taste + Instruction*Amount + Instruction*Health + Instruction*Liking, random = ~1|Subject, na.action = na.omit
            , data = subset(ChoiceData, Subject %% 2 == 1)))
summary(lme(Choice ~ Instruction*Taste + Instruction*Amount + Instruction*Health + Instruction*Liking, random = ~1|Subject, na.action = na.omit
            , data = subset(ChoiceData, Subject %% 2 == 0)))

t.test(psd$PercentAccepted[psd$Instruction == 'health'], psd$PercentAccepted[psd$Instruction == 'decrease'])
t.test(psd$RT[psd$Instruction == 'health'], psd$RT[psd$Instruction == 'decrease'], var.equal = TRUE)
t.test(psd$RT[psd$Cond == 'reg' & psd$Subject %% 2 == 1] - psd$RT[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$RT[psd$Cond == 'reg' & psd$Subject %% 2 == 0] - psd$RT[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$PercentChoseHT[psd$Instruction == 'health'], psd$PercentChoseHT[psd$Instruction == 'decrease'])
t.test(psd$PercentChoseHUT[psd$Instruction == 'health'], psd$PercentChoseHUT[psd$Instruction == 'decrease'])
t.test(psd$PercentChoseUHT[psd$Instruction == 'health'], psd$PercentChoseUHT[psd$Instruction == 'decrease'])
t.test(psd$PercentChoseUHUT[psd$Instruction == 'health'], psd$PercentChoseUHUT[psd$Instruction == 'decrease'])

# 0 == Focus on Health
quartz('',7,3); currDev = dev.cur()
par(mfrow = c(1,2))
PrettyBarPlots(subset(psd,Subject %% 2 == 1),varorder = 'RT', gpFactor = 'Cond', clrs = c('springgreen4','midnightblue'), yaxislim = c(0, 1.5))
PrettyBarPlots(subset(psd,Subject %% 2 == 0),varorder = 'RT', gpFactor = 'Cond', clrs = c('springgreen4','orange'), yaxislim = c(0, 1.5))

t.test(psd$M1_HealthWeight[psd$Instruction == 'health'], psd$M1_HealthWeight[psd$Instruction == 'decrease'], var.equal = TRUE)

t.test(psd$NChangeMind[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$NChangeMind[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$NChangeMind[psd$Cond == 'reg' & psd$Subject %% 2 == 1], psd$NChangeMind[psd$Cond == 'nat' & psd$Subject %% 2 == 1], paired = TRUE)
t.test(psd$NChangeMind[psd$Cond == 'reg' & psd$Subject %% 2 == 0], psd$NChangeMind[psd$Cond == 'nat' & psd$Subject %% 2 == 0], paired = TRUE)
t.test(psd$NChangeMind[psd$Cond == 'reg' & psd$Subject %% 2 == 1] - psd$NChangeMind[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$NChangeMind[psd$Cond == 'reg' & psd$Subject %% 2 == 0] - psd$NChangeMind[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

dev.set(currDev)
PrettyBarPlots(subset(psd,Subject %% 2 == 1),varorder = 'NChangeMind', gpFactor = 'Cond', clrs = c('springgreen4','midnightblue'))
PrettyBarPlots(subset(psd,Subject %% 2 == 0),varorder = 'NChangeMind', gpFactor = 'Cond', clrs = c('springgreen4','orange'))

t.test(psd$M1_Intercept[psd$Instruction == 'health'], psd$M1_Intercept[psd$Instruction == 'decrease'], var.equal = TRUE)
t.test(psd$M1_TasteWeight[psd$Instruction == 'health'], psd$M1_TasteWeight[psd$Instruction == 'decrease'], var.equal = TRUE)
t.test(psd$M1_HealthWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 1], psd$M1_HealthWeight[psd$Cond == 'nat'& psd$Subject %% 2 == 1], paired = TRUE)
t.test(psd$M1_HealthWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 0], psd$M1_HealthWeight[psd$Cond == 'nat'& psd$Subject %% 2 == 0], paired = TRUE)
t.test(psd$M3_LikingWeight[psd$Instruction == 'health'], psd$M3_LikingWeight[psd$Instruction == 'decrease'], var.equal = TRUE)
t.test(psd$M1_TasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M1_TasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)
t.test(psd$M1_HealthWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M1_HealthWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$HealthRegSucc[psd$Instruction == 'health'], psd$HealthRegSucc[psd$Instruction == 'decrease'], var.equal = TRUE)
t.test(psd$TasteRegSucc[psd$Instruction == 'health'], psd$TasteRegSucc[psd$Instruction == 'decrease'], var.equal = TRUE)

dev.set(currDev)
PrettyBarPlots(subset(psd,Subject %% 2 == 1),varorder = c('M1_TasteWeight','M1_HealthWeight'), gpFactor = 'Cond'
               , clrs = c('red','midnightblue'), dispSigPrd = FALSE, yaxislim = c(-.25, 1.5))
PrettyBarPlots(subset(psd,Subject %% 2 == 0),varorder = c('M1_TasteWeight','M1_HealthWeight'), gpFactor = 'Cond'
               , clrs = c('red','midnightblue'), dispSigPrd = FALSE, yaxislim = c(-.25, 1.5))
quartz('',6,3); par(mfrow = c(1,2))
PrettyBarPlots(subset(psd,Subject %% 2 == 1),varorder = c('TasteRegSucc','HealthRegSucc') 
               , clrs = c('red','midnightblue'), dispSigPrd = FALSE, yaxislim = c(-.25, 1))
PrettyBarPlots(subset(psd,Subject %% 2 == 0),varorder = c('TasteRegSucc','HealthRegSucc')
               , clrs = c('red','midnightblue'), dispSigPrd = FALSE, yaxislim = c(-.25, 1))

psd$TasteRegSuccRev = -1*psd$TasteRegSucc
quartz('',6,3); par(mfrow = c(1,2))
PrettyBarPlots(subset(psd,Subject %% 2 == 1),varorder = c('TasteRegSuccRev','HealthRegSucc') 
               , clrs = c('red','midnightblue'), dispSigPrd = FALSE, yaxislim = c(-.75, .75))
PrettyBarPlots(subset(psd,Subject %% 2 == 0),varorder = c('TasteRegSuccRev','HealthRegSucc')
               , clrs = c('red','midnightblue'), dispSigPrd = FALSE, yaxislim = c(-.75, .75))


t.test(psd$M2_FirstDevTasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M2_FirstDevTasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$M2_FirstDevTasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$M2_FirstDevTasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)
t.test(psd$M2_FirstDevTasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 1] - psd$M2_FirstDevTasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M2_FirstDevTasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 0] - psd$M2_FirstDevTasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)
t.test(psd$M1_TasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 1] - psd$M1_TasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M1_TasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 0] - psd$M1_TasteWeight[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)



t.test(psd$M1_TasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$M1_TasteWeight[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)
t.test(psd$M1_Intercept[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M1_Intercept[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)
t.test(psd$M1_Intercept[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$M1_Intercept[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$M2_Intercept[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$M2_Intercept[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)
t.test(psd$M2_Intercept[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$M2_Intercept[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)




t.test(psd$PercentAccepted[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$PercentAccepted[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$PercentAccepted[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$PercentAccepted[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$HealthWeightLiking[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$HealthWeightLiking[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$HealthWeightLiking[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$HealthWeightLiking[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$TasteWeightLiking[psd$Cond == 'nat' & psd$Subject %% 2 == 1]
       , psd$TasteWeightLiking[psd$Cond == 'nat' & psd$Subject %% 2 == 0], var.equal = TRUE)

t.test(psd$TasteWeightLiking[psd$Cond == 'reg' & psd$Subject %% 2 == 1]
       , psd$TasteWeightLiking[psd$Cond == 'reg' & psd$Subject %% 2 == 0], var.equal = TRUE)




StatsPerCondition = function(psd,varname, nDig = 2){
  var = psd[varname]
  stats = data.frame(Cond = c('natural1','health','natural2','decrease'),
                     N = NA, Mean = NA, SD = NA, Min = NA, Max = NA, vZero = NA, vNat = NA)
  c = 1
  Conditions = c('natural','health')
  tstats = vector(mode = 'character', length = 2)
  for(cond in Conditions){
    tVal = t.test(var[psd['Condition'] == cond])
    v0 = paste(formatC(tVal$statistic,digits = 2, format = "f"),'/',
               formatC(tVal$p.value,digits = 3, format = "f"),sep = "")
    for(t in 1:2){
      if(Conditions[t] == cond){
        tstats[t] = "."
      }else{
        tVal = t.test(var[psd['Condition'] == Conditions[t]], var[psd['Condition'] == cond], paired = TRUE)  
        tstats[t] = paste(formatC(tVal$statistic,digits = 2, format = "f"),'/',
                          formatC(tVal$p.value,digits = 3, format = "f"),sep = "")
      }
      
    }
    stats$N[c] = length(var[psd['Condition'] == cond & !is.na(var)]) # no. of observations
    stats$Mean[c] = mean(var[psd['Condition'] == cond], na.rm = TRUE) # mean
    stats$SD[c] = sd(var[psd['Condition'] == cond], na.rm = TRUE)
    stats$Min[c] = min(var[psd['Condition'] == cond], na.rm = TRUE)
    stats$Max[c] = max(var[psd['Condition'] == cond], na.rm = TRUE)
    stats[c,7:8] = c(v0,tstats)
    c = c + 1
  }
  print(format(stats, digits = nDig))
  print("")
  print("ANOVA: All Conditions")
  #a = summary(aov((formula(paste(varname, '~Condition + Error(Subject/Condition)'))), data = psd, na.action = na.omit))
  #a2 = summary(aov((formula(paste(varname, '~Condition + Error(Subject/Condition)'))), data = psd[psd$Condition != 'None',], na.action = na.omit))
  lmeFit <- lme(formula(paste(varname, '~Condition')), random=~1 | Subject, correlation=corCompSymm(form=~1|Subject),
                method="ML", data=psd, na.action = na.omit)
  print(anova(lmeFit))
  
  #print(a$"Error: Within"[[1]])
  #eta2 = a$"Error: Within"[[1]]['Condition','Sum Sq']/sum(c(a$"Error: Within"[[1]][,"Sum Sq"]),a$"Error: Subject"[[1]]$"Sum Sq")
  #print('Effect size eta^2')
  #   print(eta2)
  #   print("")
  #   print('ANOVA: 3 conditions only')
  #   print(a2$"Error: Within"[[1]])
}

for(pckg in c('nlme','lme4','MASS','ggplot2','logistf','reshape2','car')){
  library(pckg, character.only = TRUE)
}
rm(pckg)


source('Analysis/MouseAnalysis.R')
source('Analysis/PlotIndivMouseAnalysis.R')
xclude = function(x){subjNames %in% x}
PlotDataInCond = function(e, PredVars, Cond, filterOut = 0, ...){
  PlotData = lapply(mget(paste(PredVars,'Effects',gsub("\\s", "", Cond),sep = ""),envir=e),
                    function(x){x[xclude(filterOut),] = NA; return(x)})
  ylims = lineanderrbars(PlotData, newPlot = TRUE,
                         ylab = 'Effect on Trajectory',xlab = 'Time (ms)',xScale = c(0,16.67), linesAt = 0, ...)
  
}

PlotVarByCond = function(e, PredVar, whichConds = 1:3, filterOut = 0, ...){
  Conds = c('nat','decrease','health')
  PlotData = lapply(mget(paste(PredVar,'Effects',gsub("\\s", "", Conds[whichConds]),sep = ""),envir=e),
                    function(x){x[xclude(filterOut),] = NA; return(x)})
  
  ylims = lineanderrbars(PlotData, newPlot = TRUE,
                         ylab = 'Effect on Trajectory',xlab = 'Time (ms)',xScale = c(0,16.67), linesAt = 0, ...)
  
}

PlotVarByGroupByCond = function(e, PredVar, whichConds = 1:2, ...){
  Conds1 = c('nat','decrease')
  Conds2 = c('nat','health')
  PlotData = c(lapply(mget(paste(PredVar,'Effects',gsub("\\s", "", Conds1[whichConds]),sep = ""),envir=e),
                    function(x){x[xclude(subjNames[subjNames %% 2 == 0]),] = NA; return(x)}),
                  lapply(mget(paste(PredVar,'Effects',gsub("\\s", "", Conds2[whichConds]),sep = ""),envir=e),
                         function(x){x[xclude(subjNames[subjNames %% 2 == 1]),] = NA; return(x)}))
                  
  ylims = lineanderrbars(PlotData, newPlot = TRUE,
                         ylab = 'Effect on Trajectory',xlab = 'Time (ms)',xScale = c(0,16.67)
                         , linesAt = 0, linetype = rep(1:length(whichConds), each = 2), ...)
  
}


MouseData$DrxBin = MouseData$Drx
MouseData$DrxBin[MouseData$Drx == -1] = 0
PredVars = c('Taste','Health')
SimpleModel = MouseAnalysis(PredVars,MouseData,ChoiceData)
SimpleModelTraj = MouseAnalysis(PredVars,MouseData,ChoiceData, mouseVar = 'Trajectory', lmType = 'lm')

RegAnalysisTraj = list()
RegAnalysisTraj$HealthSucc_HvN = SimpleModelTraj$HealthEffectshealth - SimpleModelTraj$HealthEffectsnat
RegAnalysisTraj$TasteSucc_HvN = SimpleModelTraj$TasteEffectsnat - SimpleModelTraj$TasteEffectshealth
RegAnalysisTraj$HealthSucc_HvN[subjNames %% 2 == 1,] = (SimpleModelTraj$HealthEffectsdecrease - SimpleModelTraj$HealthEffectsnat)[subjNames %% 2 == 1,]
RegAnalysisTraj$TasteSucc_HvN[subjNames %% 2 == 1,] = (SimpleModelTraj$TasteEffectsnat - SimpleModelTraj$TasteEffectsdecrease)[subjNames %% 2 == 1,]

clrs = c('red','green','springgreen4','blue','orange')
quartz('',5,4)
PlotDataInCond(SimpleModelTraj,PredVars,Cond = 'decrease',color = clrs[1:2], showPVals = list(1,2))

quartz('',3.3, 2.6); par(mar = c(4,3,1,1) + .1); plotDevice = dev.cur()
lineanderrbars(list(RegAnalysisTraj$HealthSucc_HvN[subjNames %% 2 ==0,], RegAnalysisTraj$TasteSucc_HvN[subjNames %% 2 ==0,])
               , rawdata = TRUE, color = c('blue','red'), showPVals = list(1,2,c(1, 2))
               , newPlot = TRUE, linesAt = 0, xScale = c(0,16.667), xlab = "Time",ylab = 'Regulatory Success')

quartz('',3.3, 2.6); par(mar = c(4,3,1,1) + .1); plotDevice = dev.cur()
lineanderrbars(list(RegAnalysisTraj$HealthSucc_HvN[subjNames %% 2 ==1,], RegAnalysisTraj$TasteSucc_HvN[subjNames %% 2 ==1,])
               , rawdata = TRUE, color = c('blue','red'), showPVals = list(1,2,c(1, 2))
               , newPlot = TRUE, linesAt = 0, xScale = c(0,16.667), xlab = "Time",ylab = 'Regulatory Success')

quartz('',3.3, 2.6); par(mar = c(4,3,1,1) + .1); plotDevice = dev.cur()
lineanderrbars(list(RegAnalysisTraj$TasteSucc_HvN[subjNames %% 2 ==0,], RegAnalysisTraj$TasteSucc_HvN[subjNames %% 2 ==1,])
               , rawdata = TRUE, color = c('blue','red'), showPVals = list(1,2,c(1, 2))
               , newPlot = TRUE, linesAt = 0, xScale = c(0,16.667), xlab = "Time",ylab = 'Regulatory Success')

quartz('',3.3, 2.6); par(mar = c(4,3,1,1) + .1); plotDevice = dev.cur()
lineanderrbars(list(RegAnalysisTraj$HealthSucc_HvN[subjNames %% 2 ==0,], RegAnalysisTraj$HealthSucc_HvN[subjNames %% 2 ==1,])
               , rawdata = TRUE, color = c('blue','red'), showPVals = list(1,2,c(1, 2))
               , newPlot = TRUE, linesAt = 0, xScale = c(0,16.667), xlab = "Time",ylab = 'Regulatory Success')

dev.copy2pdf(device = plotDevice, file = 'Figures/DrxTimeSeries_RegSuccessIncreaseHealthDecreaseTaste.pdf')

psd$ThinkHealthyDiff = psd$ThinkHealthyReg - psd$ThinkHealthyNat
psd$DecreaseDesireDiff = psd$DecreaseDesireReg - psd$DecreaseDesireNat
summary(lm(HealthSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Cond == 'reg')))
summary(lm(TasteSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Cond == 'reg')))

summary(lm(HealthSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Instruction == 'health')))
summary(lm(HealthSuccess ~ ChangeThink + AvoidLook, data = subset(psd, Instruction == 'health')))

summary(lm(HealthSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Instruction == 'decrease')))
summary(lm(HealthSuccess ~ Decrease , data = subset(psd, Instruction == 'decrease')))

summary(lm(TasteSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Instruction == 'health')))
summary(lm(TasteSuccess ~ Decrease , data = subset(psd, Instruction == 'health')))

summary(lm(TasteSuccess ~ Lied, data = subset(psd, Instruction == 'decrease')))
summary(lm(TasteSuccess ~ Lied, data = subset(psd, Instruction == 'health')))




summary(lm(HealthSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Instruction == 'health')))


summary(lm(TasteSuccess ~ FocusUnhealthy + Avoid + ChangeThink + AvoidLook + Lied + FocusHealth + Decrease , data = subset(psd, Cond == 'reg')))



summary(lm(RegSuccessHealth_TWeight ~ FocusedUnhealthy + FocusedHunger + Reappraised + Avoided + Lied, data = subset(psd, Condition == 'natural')))
summary(lm(RegSuccessHealth_Perc ~ FocusedUnhealthy + FocusedHunger + Reappraised + Avoided + Lied, data = subset(psd, Condition == 'natural')))



quartz('',5,4)
PlotDataInCond(SimpleModelTraj,PredVars,Cond = 'health',color = clrs[1:2], showPVals = list(1,2, c(1,2)))

quartz('',5,4)
PlotDataInCond(SimpleModelTraj,PredVars,Cond = 'nat',color = clrs[1:2], showPVals = list(1,2, c(1,2)))

quartz('',5,4)
PlotVarByCond(SimpleModelTraj,'Taste',whichConds = c(1,3),color = c('red','brickred'), filterOut = subjNames[subjNames %% 2 == 1], showPVals = list(1,2,c(1,2)))

quartz('',5,4)
PlotVarByCond(SimpleModelTraj,'Taste',whichConds = c(1,3),color = c('red','firebrick4'), filterOut = subjNames[subjNames %% 2 == 1], showPVals = list(1,2,c(1,2)))

quartz('',5,4)
PlotVarByCond(SimpleModelTraj,'Health',whichConds = c(1,2),color = c('blue','midnightblue'), ylim = c(-.05,.3), filterOut = subjNames[subjNames %% 2 == 0], showPVals = list(1,2,c(1,2)))

quartz('',5,4)
PlotVarByCond(SimpleModelTraj,'Health',whichConds = c(1,2),color = clrs[1:2], filterOut = subjNames[subjNames %% 2 == 0], showPVals = list(1,2,c(1,2)))

quartz('',5,4)
PlotVarByGroupByCond(SimpleModelTraj,'Health',whichConds = c(1,2),color = c('springgreen4','midnightblue','springgreen4','orange'), showPVals = list(1,2,3,4,c(1,2), c(3,4)))

quartz('',5,4)
PlotVarByGroupByCond(SimpleModelTraj,'Taste',whichConds = c(1,2),color = c('springgreen4','midnightblue','springgreen4','orange'), showPVals = list(1,2,3,4,c(1,2), c(3,4)))


#TFEQ correlates
with(subset(psd,Cond == 'nat'),summary(lm(CogRestraint~ M1_TasteWeight + M1_HealthWeight))) # p .09 on Health
with(subset(psd,Cond == 'nat'),summary(lm(CogRestraint~ M1_HealthWeight))) # p .04 on Health
with(subset(psd,Cond == 'nat'),summary(lm(EmotEating~ M1_TasteWeight + M1_HealthWeight))) # p .01 on Health
with(subset(psd,Cond == 'nat'),summary(lm(UncontEating~ M1_TasteWeight + M1_HealthWeight))) # n.s.

with(subset(psd,Cond == 'reg'),summary(lm(CogRestraint~ M1_TasteWeight + M1_HealthWeight))) # p .07 on Taste
with(subset(psd,Cond == 'reg'),summary(lm(CogRestraint~ M1_TasteWeight))) # p .02 on Taste
with(subset(psd,Cond == 'reg'),summary(lm(EmotEating~ M1_TasteWeight + M1_HealthWeight))) # n.s.
with(subset(psd,Cond == 'reg'),summary(lm(UncontEating~ M1_TasteWeight + M1_HealthWeight))) # n.s.

# Food consumption habits
with(subset(psd,Cond == 'nat'),summary(lm(FiberConsumption~ M1_TasteWeight + M1_HealthWeight))) # p .01 Taste, p .05 Heaalth
with(subset(psd,Cond == 'nat'),summary(lm(VegConsumption~ M1_TasteWeight + M1_HealthWeight))) # p .06 Taste, p .06 Heaalth
with(subset(psd,Cond == 'nat'),summary(lm(VegConsumption~ M1_TasteWeight))) # p .01 Taste
with(subset(psd,Cond == 'nat'),summary(lm(VegConsumption~ M1_HealthWeight))) # p .01 Health
# others (Fatty Foods, MeatConsumption,FatConsumption,JunkConsumption) not significant
with(subset(psd,Cond == 'nat'),summary(lm(M1_TasteWeight ~ FiberConsumption + VegConsumption + FattyFoods + MeatConsumption + JunkConsumption + FatConsumption))) # p .01 Taste, p .05 Heaalth
with(subset(psd,Cond == 'nat'),summary(lm(M1_TasteWeight ~ M1_HealthWeight + FiberConsumption))) # p .01 Taste, p .05 Heaalth

with(subset(psd,Cond == 'nat'),summary(lm(M1_HealthWeight ~ FiberConsumption + VegConsumption + FattyFoods + MeatConsumption + JunkConsumption + FatConsumption))) # p .01 Taste, p .05 Heaalth
with(subset(psd,Cond == 'nat'),summary(lm(M1_HealthWeight ~ M1_TasteWeight + FiberConsumption))) # p .007 Fiber

# Barratt Impulsivity
with(subset(psd,Cond == 'nat'),summary(lm(BISAttention ~ M1_TasteWeight + M1_HealthWeight))) # p .009 Taste
with(subset(psd,Cond == 'reg'),summary(lm(BISAttention ~ M1_TasteWeight + M1_HealthWeight))) # p .03 Taste
with(subset(psd,Cond == 'reg'),summary(lm(BISPerseverence ~ M1_TasteWeight + M1_HealthWeight))) # p .09 Taste
# no other factors significant


psd$HealthSuccess[psd$Cond == 'reg'] = with(psd,M1_HealthWeight[Cond == 'reg'] - M1_HealthWeight[Cond == 'nat'])
psd$TasteSuccess[psd$Cond == 'reg'] = with(psd,M1_TasteWeight[Cond == 'nat'] - M1_TasteWeight[Cond == 'reg'])
psd$TotalSuccess = psd$TasteSuccess + psd$HealthSuccess
# no correlates of any form of regulatory success
