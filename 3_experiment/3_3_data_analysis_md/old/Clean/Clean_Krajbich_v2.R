# FINESSE DATA to match Krajbich's format for data_prep_for_addm_to_share

# First RUN DataClean_v2a.R

# removes all variables but NOT functions
rm(list = setdiff(ls(), lsf.str()))

# SET WORKING DIRECTORY
setwd("~/Dropbox/PROGRAMMING/*NEURO/2017_MADE/Analysis")

# LOAD DATA 
load("Data/S_M.Rdata")

# || SUBJECT || TRIAL || LEFTVAL || RIGHTVAL || SUMMEDVAL || RT || CHOICE  || FIXNUM || REVFIXNUM || ROI || FIXDUR ||

# CREATE DF

df <- NULL

# MAKE DF WITH NUMBER OF ROWS = TOTAL NUMBER OF FIXATIONS
# FIRST: Find out how many fixations TOTAL

# make sure every trial ends with an NA val
S_M$`14_fixation` <- NA     



# find the first NA val in each row
naVal <- vector(mode="numeric", length=0)
for(x in 1:length(S_M$Trial)){
  naVal[x] <- min(which(is.na(S_M[x,])))
}

# Check that we are starting at column fix#1
firstFix = which(names(S_M) == "1_fixation")

# Create New DataFrame
i = 1
for(x in 1:length(S_M$Trial)){
  j = 1
  for(y in firstFix:(naVal[x]-1)){
    df$subject[i] = S_M$subject[x]
    df$accuracy[i] = S_M$accuracy[x]
    df$earnings[i] = S_M$finalEarnings[x]
    df$trial[i] = S_M$Trial[x]
    df$faceVal[i] = S_M$faceVal[x] 
    df$houseVal[i] = S_M$houseVal[x]
    df$multFace[i] = S_M$mult2Face[x]
    df$multHouse[i] = S_M$mult1House[x]
    df$multNum[i] = S_M$multNum[x]
    df$totValFace[i] = S_M$faceTotal[x]
    df$totValHouse[i] = S_M$houseTotal[x]
    df$summedVal[i] = S_M$summedVal[x]
    
    df$rt[i] = S_M$rt[x]
    df$choice[i] = S_M$choice[x]
    df$correct[i] = S_M$correct[x]
    
    # for ROI 0 = FACE, 1 = HOUSE
    df$roi[i] = (S_M$firstImage[x] + j - 1) %% 2   # Goes between ROI 0 and 1 with each Fixation
    df$fixNum[i] = j  
    df$revFixNum[i] =  naVal[x] - firstFix -j +1 
    df$fixDur[i] = S_M[x,y]
    
    df$fixNumAvg[i] = S_M$swapAvg[x]
    df$firstFix[i] = S_M$firstImage[x]
    df$finalFix[i] = S_M$lastImage[x]
    j = j+1
    i = i+1
  }
}

df_K = data.frame("subject" = df$subject, 
                  "accuracy" = df$accuracy, 
                  "earnings" = df$earnings, 
                  "trial" = df$trial, 
                  "faceVal" = df$faceVal, 
                  "houseVal" = df$houseVal, 
                  "multFace" = df$multFace,
                  "multHouse" = df$multHouse, 
                  "multNum" = df$multNum, 
                  "totValFace" = df$totValFace, 
                  "totValHouse" = df$totValHouse, 
                  "summedVal" = df$summedVal, 
                  "rt" = df$rt, 
                  "choice" = df$choice, 
                  "correct" = df$correct,
                  "roi" = df$roi, 
                  "fixNum" = df$fixNum, 
                  "revFixNum" = df$revFixNum, 
                  "fixDur" = df$fixDur, 
                  "fixNumAvg" = df$fixNumAvg, 
                  "firstFix" = df$firstFix, 
                  "finalFix" = df$finalFix)

S_M_K <- df_K
save(S_M_K, file = "~/Dropbox/PROGRAMMING/*NEURO/2017_MADE/Analysis/Data/S_M_K.Rdata")
save(S_M_K, file = "~/Dropbox/PROGRAMMING/*NEURO/aDDM_Krajbich/S_M_K.Rdata")

