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
# INITIALIZE DATA FRAMES  #
#-------------------------#
total_NM <- NULL
total_M <- NULL

#-------------------------#
#   FORMAT DATA FRAMES 
#   (break into Multiplier and non-Multiplier)
#-------------------------#

#loop through and create data frames
for (i in 1:length(subjects)) {
  
  temp <- eval(as.name(paste0("s", i)))
  
  #remove extraneous rows
  temp <- temp[-c(1:3), -c(1:29)]
  
  #create non-multiplier data frame
  temp_NM <- temp[c(1:100), c(1:10) ]
  
  #create multiplier data frame
  temp_M <- temp[c(103:404), c(1:17)]
  temp_M <- temp_M[,-c(9:14)]
  temp_M <- temp_M[-c(101,202),]

  #renameSomeColumns
  library(plyr)
  temp_NM <- plyr::rename(temp_NM, c("numberEntry_3.keys"="acceptReject", "numberEntry_3.rt"="decisionTime"))
  temp_M <- plyr::rename(temp_M, c("numberEntry_4.keys"="acceptReject", "numberEntry_4.rt"="decisionTime"))
  
  #clean up acceptReject column
  index <- c("['f']", "['j']")
  values <- c(1, 0) #where 1 is accept and 0 is reject
  temp_NM$acceptReject <- values[match(temp_NM$acceptReject, index)]
  temp_M$acceptReject <- values[match(temp_M$acceptReject, index)]
  
  #make summed value a value to 2 decimal places
  temp_NM$summedVal <- format(round(temp_NM$summedVal, 2), nsmall = 2)
  temp_M$summedVal <- format(round(temp_M$summedVal, 2), nsmall = 2)
  
  #make numeric
  temp_NM$summedVal <- as.numeric(temp_NM$summedVal)
  temp_M$summedVal <- as.numeric(temp_M$summedVal)
  
  #remove brackets on RT column
  temp_NM$decisionTime <- gsub("\\[|\\]", "", temp_NM$decisionTime)
  temp_M$decisionTime <- gsub("\\[|\\]", "", temp_M$decisionTime)
  #make Numeric
  temp_NM$decisionTime <- as.numeric(temp_NM$decisionTime)
  temp_M$decisionTime <- as.numeric(temp_M$decisionTime)
  
  #label subjects
  temp_NM$subject <- i
  temp_M$subject <- i
  
  total_NM <- rbind(total_NM, temp_NM)
  total_M <- rbind(total_M, temp_M)
}

#Make row numbering sequential
rownames(total_NM) <- 1:nrow(total_NM)
rownames(total_M) <- 1:nrow(total_M)

#make final earnings column to remove people later
total_NM$finalEarnings = total_NM$earnings[total_NM$subject * 100]
total_M$finalEarnings = total_M$earnings[total_M$subject * 300]

#FIND THE NA VALUES
which(is.na(total_M$decisionTime))
#In this case, row 1031 has an NA Val.
total_M <- total_M[-1031,] #Remove

#change flips that are coded 3 to 2s.
for(i in 1:nrow(total_M)){
  if (total_M$flip[i] == 3){
    total_M$flip[i] = 2
  }
}

#add row of absolute difference between the two values
total_NM$absDIff <-abs(total_NM$faceVal - total_NM$houseVal)
total_M$absDIff <-abs(total_M$faceVal - total_M$houseVal)

#clean outliers due to distraction
total_NM_clean<- total_NM[!(total_NM$decisionTime>10),]
total_M_clean<- total_M[!(total_M$decisionTime>10),]

#clean people who earned less than $30
total_M_clean2 <- total_M_clean[!(total_M_clean$finalEarnings<80),]
  #NEED TO FIGUREO OUT HOW TO SELECT SAME SUBJECTS TO FILTER NM





head(total_M)

