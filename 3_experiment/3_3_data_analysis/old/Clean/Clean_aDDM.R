# FINESSE DATA to match Tavares format for expdata.csv and fixations.csv

# First RUN DataClean_v2a.R

# removes all variables but NOT functions
rm(list = setdiff(ls(), lsf.str()))

# SET WORKING DIRECTORY
setwd("~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis")

# LOAD DATA 
load("Data/S_M.Rdata")
load("Data/S_M_K.Rdata")

# MAKE choice -1 and 1 instead of 0 and 1 (reject/accept)
S_M$choice[S_M$choice==0] = -1

table(S_M$houseValBinCtr)
table(S_M$faceValBinCtr)

#---------------------------#
# Response DF               #
#---------------------------#

# parcode,trial,rt,choice,item_left,item_right,valid (don't actually need valid)

expdata <- data.frame("parcode" = S_M$subject , "trial" = S_M$Trial,
                      "rt" = S_M$rt * 1000, # convert to ms 
                      "choice" = S_M$choice,
                      "item_left" = S_M$faceTotal, "item_right" = S_M$houseTotal,
                      "item_left_val" = S_M$faceValBinCtr, "item_right_val" = S_M$houseValBinCtr)

write.csv(expdata, file = "/Users/djw/Dropbox/PROGRAMMING/*NEURO/aDDM_Tavares/made_data/expdata.csv", row.names=FALSE)


# from  S_M_K we need:
# parcode, trial, fix_item, fix_time

fixations <- data.frame("parcode" = S_M_K$subject,
                        "trial" = S_M_K$trial,
                        "fix_item" = S_M_K$roi + 1, # tavares uses 1 and 2 for left and right fixes
                        "fix_time" = S_M_K$fixDur *1000, # convert to ms
                        "fix_num" = S_M_K$fixNum,
                        "rev_fix_num" = S_M_K$revFixNum)

write.csv(fixations, file = "/Users/djw/Dropbox/PROGRAMMING/*NEURO/aDDM_Tavares/made_data/fixations.csv", row.names=FALSE)


