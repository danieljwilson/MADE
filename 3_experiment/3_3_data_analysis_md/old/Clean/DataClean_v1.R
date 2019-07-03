#------------------------#
# SET WORKING DIRECTORY  #
#------------------------#
setwd("~/Dropbox/PHD/CENDRI/Project/Code/LabSharedFolder/MADE01/CODE/v1/data/TRIALS/")

#------------------------#
# IMPORT CSV FILES       #
#------------------------#
subjects = list.files(pattern="*.csv")
for (i in 1:length(subjects)){
  assign(paste0("s", i), read.csv(subjects[i]))
} 

#------------------------#
# SET WORKING DIRECTORY  # 
#------------------------#
setwd("~/Dropbox/PROGRAMMING/R/WeightsExp/Pilot")

#-------------------------#
# LOAD LIBRARIES          #
#-------------------------#
library(dplyr)

#-------------------------#
# INITIALIZE DATA FRAMES  #
#-------------------------#
total_NM_v1 <- NULL
total_M_v1 <- NULL

#-------------------------#
#   FORMAT DATA FRAMES 
#   (break into Multiplier and non-Multiplier)
#-------------------------#

#loop through and create data frames
for (i in 1:length(subjects)) {
  
  temp <- eval(as.name(paste0("s", i)))
  
  #remove extraneous rows
  temp <- temp[-c(1:3), -c(1:29)]
  temp <- temp[, -c(11:14)]
  
  #create non-multiplier data frame
  temp_NM <- temp[c(1:100), c(1:24)]
  temp_NM <- temp_NM[, -c(12:23)]
  
  #create multiplier data frame
  temp_M <- temp[c(101:404), c(1:24)]
  temp_M <- temp_M[-c(1:2),]
  temp_M <- temp_M[-c(101),]
  temp_M <- temp_M[-c(201),]
  
  temp_M <- temp_M[,-c(9:10)] #deleting entry rows from NM
  temp_M <- temp_M[,-c(12:21)] #deleting entry rows from NM
  
  #renameSomeColumns
  library(plyr)
  temp_NM <- plyr::rename(temp_NM, c("numberEntry_3.keys"="selection", "numberEntry_3.rt"="timings"))
  temp_M <- plyr::rename(temp_M, c("numberEntry_4.keys"="selection", "numberEntry_4.rt"="timings"))
  
  #make summed value a value to 2 decimal places
  temp_NM$summedVal <- format(round(temp_NM$summedVal, 2), nsmall = 2)
  temp_M$summedVal <- format(round(temp_M$summedVal, 2), nsmall = 2)
  
  #make numeric
  temp_NM$summedVal <- as.numeric(temp_NM$summedVal)
  temp_M$summedVal <- as.numeric(temp_M$summedVal)
  
  #label subjects
  temp_NM$subject <- i
  temp_M$subject <- i
  
  total_NM_v1 <- rbind(total_NM_v1, temp_NM)
  total_M_v1 <- rbind(total_M_v1, temp_M)
  total_M_v1$origNumber <- total_M_v1$participant
}

total_NM_v1$timings<- as.numeric(gsub('\\[|\\]', '', as.character(total_NM_v1$timings)))

total_M_v1$timings<- as.numeric(gsub('\\[|\\]', '', as.character(total_M_v1$timings)))
dropRow = which(is.na(total_M_v1$timings)) # there was one row with an NA value
total_M_v1 <- total_M_v1[-c(dropRow), ] # drop that row

# RENAME timings->rt
names(total_NM_v1)[names(total_NM_v1) == 'timings'] <- 'rt'
names(total_M_v1)[names(total_M_v1) == 'timings'] <- 'rt'

# FINAL EARNINGS column (to remove people later)
total_NM_v1$finalEarnings = total_NM_v1$earnings[total_NM_v1$subject * 100]
total_M_v1$finalEarnings = total_M_v1$earnings[total_M_v1$subject * 299] # because we dropped 1 row!

# ACCURACY Column
subject_accuracy <- group_by(total_M_v1, subject) %>%
  dplyr::summarize(accuracy = mean(correct, na.rm = T))

for(x in 1:nrow(total_M_v1)){
  total_M_v1$accuracy[total_M_v1$subject == x] <- subject_accuracy$accuracy[subject_accuracy==x]
}

subject_accuracy <- group_by(total_NM_v1, subject) %>%
  dplyr::summarize(accuracy = mean(correct, na.rm = T))

for(x in 1:nrow(total_NM_v1)){
  total_NM_v1$accuracy[total_NM_v1$subject == x] <- subject_accuracy$accuracy[subject_accuracy==x]
}

# SAVE AS CSV
write.csv(total_NM_v1, file = "~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis/Data/NS_NM.csv") #Write to Analysis Folder
write.csv(total_M_v1, file = "~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis/Data/NS_M.csv") 
