#------------------------#
# SET WORKING DIRECTORY  #
#------------------------#
setwd("~/Dropbox/PHD/CENDRI/Project/Code/LabSharedFolder/MADE01/CODE/v2_a/data/TRIALS/")

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
total_NM_v2a <- NULL
total_M_v2a <- NULL

#-------------------------#
#   FORMAT DATA FRAMES 
#   (break into Multiplier and non-Multiplier)
#-------------------------#

#loop through and create data frames
for (i in 1:length(subjects)) {
  
  temp <- eval(as.name(paste0("s", i)))
  
  #remove extraneous rows
  temp <- temp[, -c(1:23)]
  
  #create non-multiplier data frame
  temp_NM <- temp[c(1:100), c(1:11)]
  
  #create multiplier data frame
  temp_M <- temp[c(101:400), c(1:14)]
  temp_M <- temp_M[,-c(10:11)] #deleting entry rows from NM

  #renameSomeColumns
  library(plyr)
  temp_NM <- plyr::rename(temp_NM, c("numberEntry_3.keys"="swapChoose", "numberEntry_3.rt"="timings"))
  temp_M <- plyr::rename(temp_M, c("numberEntry_4.keys"="swapChoose", "numberEntry_4.rt"="timings"))
  
  #make summed value a value to 2 decimal places
  temp_NM$summedVal <- format(round(temp_NM$summedVal, 2), nsmall = 2)
  temp_M$summedVal <- format(round(temp_M$summedVal, 2), nsmall = 2)
  
  #make numeric
  temp_NM$summedVal <- as.numeric(temp_NM$summedVal)
  temp_M$summedVal <- as.numeric(temp_M$summedVal)
  
  #label subjects
  temp_NM$subject <- i
  temp_M$subject <- i
  
  #get original subject number
  hold <- eval(as.name(paste0("s", i)))
  temp_M$origNumber <- hold$participant[1:300]
  
  total_NM_v2a <- rbind(total_NM_v2a, temp_NM)
  total_M_v2a <- rbind(total_M_v2a, temp_M)
}

#------------------------#
# CONVERT FACTORS TO LISTS  # 
#------------------------#

#convert timings as factor to timings2 as list
for(x in 1:nrow(total_M_v2a)){
  test <- strsplit(as.character(total_M_v2a$timings[x]), ", ")[[1]]
  test<- gsub('\\[|\\]', '', test)
  total_M_v2a$timings2[x] <- list(as.numeric(test))
  total_M_v2a$rt[x] <- tail(total_M_v2a$timings2[x][[1]], n=1) #use last value in list to get RT value
}

for(x in 1:nrow(total_NM_v2a)){
  test <- strsplit(as.character(total_NM_v2a$timings[x]), ", ")[[1]]
  test<- gsub('\\[|\\]', '', test)
  total_NM_v2a$timings2[x] <- list(as.numeric(test))
  total_NM_v2a$rt[x] <- tail(total_NM_v2a$timings2[x][[1]], n=1) #use last value in list to get RT value
}

#convert imageList as factor to imageSequence as list
for(x in 1:nrow(total_M_v2a)){
  test <- strsplit(as.character(total_M_v2a$imageList[x]), ", ")[[1]]
  test<- gsub('\\[|\\]', '', test)
  total_M_v2a$imageSequence[x] <- list(as.numeric(test))
}

for(x in 1:nrow(total_NM_v2a)){
  test <- strsplit(as.character(total_NM_v2a$imageList[x]), ", ")[[1]]
  test<- gsub('\\[|\\]', '', test)
  total_NM_v2a$imageSequence[x] <- list(as.numeric(test))
}

#convert swapChoose as factor to acceptReject as list and add column
for(x in 1:nrow(total_M_v2a)){
  test <- strsplit(as.character(total_M_v2a$swapChoose[x]), ", ")[[1]]
  test<- gsub('\\[|\\]', '', test)
  test<- gsub('space', '', test)
  total_M_v2a$acceptReject[x] <- list(test)
  choice <- tail(total_M_v2a$acceptReject[x][[1]], n=1)
  #f means accept
  if(choice == "'f'"){
    total_M_v2a$acceptReject[x]=1
  }
  #j means reject
  if(choice == "'j'"){
    total_M_v2a$acceptReject[x]=0
  }
}

#------------------------#
# REFORMAT COLUMN        # 
#------------------------#

#change flips that are coded 3 to 2s.
for(i in 1:nrow(total_M_v2a)){
  if (total_M_v2a$flip[i] == 3){
    total_M_v2a$flip[i] = 2
  }
}

#--------------------------------------------------#
#  RENUMBER TRIALS TO MAKE CONTINUOUS by SUBJECT   #
#--------------------------------------------------#

subject_count = length(unique(total_M_v2a$subject))
total_M_v2a$Trial = rep(1:300, subject_count)

#------------------------#
# ADD COLUMNS            # 
#------------------------#

# Figure out histogram bin size, based on equal numbers of observations
library(Hmisc) # cut2

# How many bins?
numBins = 15

# SUMMED VAL
total_M_v2a$valBin <- as.numeric(cut2(total_M_v2a$summedVal, g=numBins))
total_M_v2a$valBinAmt <- cut2(total_M_v2a$summedVal, g=numBins)
total_M_v2a$valBinCtr <- cut2(total_M_v2a$summedVal, g=numBins, levels.mean=TRUE)
# Round to 2 decimal places
total_M_v2a$valBinCtr <- format(round(as.numeric(as.character(total_M_v2a$valBinCtr)), 2), nsmall = 2)

##########################################################

# Create Choice Column: 0 = reject, 1 = accept
total_M_v2a$choice = 0
# accepted correctly
total_M_v2a$choice[total_M_v2a$summedVal>0 & total_M_v2a$correct==1] = 1
# acceped incorrectly
total_M_v2a$choice[total_M_v2a$summedVal<=0 & total_M_v2a$correct==0] = 1

#column for individual FIXATION TIMINGS
total_M_v2a$fixation_timing <- vector("list", 20)

for(x in 1:nrow(total_M_v2a)){
  for(y in 1:lengths(total_M_v2a$timings2[x])){
    if (y==1){
      subVal <- total_M_v2a$timings2[x][[1]][1]
      total_M_v2a$fixation_timing[x][[1]][y] <- subVal
    }
    if (y>1){
      subVal <- total_M_v2a$timings2[x][[1]][y] - total_M_v2a$timings2[x][[1]][y-1]
      total_M_v2a$fixation_timing[x][[1]][y] <- subVal
    }
  }
}

total_NM_v2a$fixation_timing <- vector("list", 20)

for(x in 1:nrow(total_NM_v2a)){
  for(y in 1:lengths(total_NM_v2a$timings2[x])){
    if (y==1){
      subVal <- total_NM_v2a$timings2[x][[1]][1]
      total_NM_v2a$fixation_timing[x][[1]][y] <- subVal
    }
    if (y>1){
      subVal <- total_NM_v2a$timings2[x][[1]][y] - total_NM_v2a$timings2[x][[1]][y-1]
      total_NM_v2a$fixation_timing[x][[1]][y] <- subVal
    }
  }
}


#FACE & HOUSE viewing time totals columns
#initialize columns
total_M_v2a$total_0_face <- 0
total_M_v2a$total_1_house <- 0
total_M_v2a$lastImage <- 0

for(x in 1:nrow(total_M_v2a)){
  #Column for last image looked at
  total_M_v2a$lastImage[x] <- tail(total_M_v2a$imageSequence[x][[1]], n=1)
  
  for(y in 1:lengths(total_M_v2a$fixation_timing[x])){ #length of imageSequence is the same
    #if the first image is 0
    if (total_M_v2a$imageSequence[x][[1]][1]==0){ 
      if (y%%2 == 1){
        #add the even images for total 0
        total_M_v2a$total_0_face[x] <- total_M_v2a$total_0_face[x] + total_M_v2a$fixation_timing[x][[1]][y] 
      }
      if (y%%2 == 0){
        #add the odd images for total 1
        total_M_v2a$total_1_house[x] <- total_M_v2a$total_1_house[x] + total_M_v2a$fixation_timing[x][[1]][y] 
      }
    }
    #if the first image is 1
    if (total_M_v2a$imageSequence[x][[1]][1]==1){ #if the first image is 0
      if (y%%2 == 1){
        #add the even images for total 0
        total_M_v2a$total_1_house[x] <- total_M_v2a$total_1_house[x] + total_M_v2a$fixation_timing[x][[1]][y] 
      }
      if (y%%2 == 0){
        #add the odd images for total 1
        total_M_v2a$total_0_face[x] <- total_M_v2a$total_0_face[x] + total_M_v2a$fixation_timing[x][[1]][y] 
      }
    }
  }
}

#initialize columns
total_NM_v2a$total_0_face <- 0
total_NM_v2a$total_1_house <- 0
total_NM_v2a$lastImage <- 0

for(x in 1:nrow(total_NM_v2a)){
  #Column for last image looked at
  total_NM_v2a$lastImage[x] <- tail(total_NM_v2a$imageSequence[x][[1]], n=1)
  
  for(y in 1:lengths(total_NM_v2a$fixation_timing[x])){ #length of imageSequence is the same
    #if the first image is 0
    if (total_NM_v2a$imageSequence[x][[1]][1]==0){ 
      if (y%%2 == 1){
        #add the even images for total 0
        total_NM_v2a$total_0_face[x] <- total_NM_v2a$total_0_face[x] + total_NM_v2a$fixation_timing[x][[1]][y] 
      }
      if (y%%2 == 0){
        #add the odd images for total 1
        total_NM_v2a$total_1_house[x] <- total_NM_v2a$total_1_house[x] + total_NM_v2a$fixation_timing[x][[1]][y] 
      }
    }
    #if the first image is 1
    if (total_NM_v2a$imageSequence[x][[1]][1]==1){ #if the first image is 0
      if (y%%2 == 1){
        #add the even images for total 0
        total_NM_v2a$total_1_house[x] <- total_NM_v2a$total_1_house[x] + total_NM_v2a$fixation_timing[x][[1]][y] 
      }
      if (y%%2 == 0){
        #add the odd images for total 1
        total_NM_v2a$total_0_face[x] <- total_NM_v2a$total_0_face[x] + total_NM_v2a$fixation_timing[x][[1]][y] 
      }
    }
  }
}


#FINAL EARNINGS column (to remove people later)
total_NM_v2a$finalEarnings = total_NM_v2a$earnings[total_NM_v2a$subject * 100]
total_M_v2a$finalEarnings = total_M_v2a$earnings[total_M_v2a$subject * 300]

#ABSOLUTE DIFFERENCE between the two values column
total_NM_v2a$absDiff <-abs(total_NM_v2a$faceVal - total_NM_v2a$houseVal)
total_M_v2a$absDiff <-abs(total_M_v2a$faceVal - total_M_v2a$houseVal)

#new column with NUMBER OF SWAPS
total_M_v2a$swapAmount <- lengths(total_M_v2a$imageSequence)
total_NM_v2a$swapAmount <- lengths(total_NM_v2a$imageSequence)

#new column with MEAN SWAP NUMBER
grouped <- group_by(total_M_v2a, subject)
swapMeans <- dplyr::summarise(grouped, meanSwap = mean(swapAmount))

for(x in 1:nrow(total_M_v2a)){
  total_M_v2a$swapAvg[x] <- swapMeans$meanSwap[total_M_v2a$subject[x]]
}

grouped <- group_by(total_NM_v2a, subject)
swapMeans <- dplyr::summarise(grouped, meanSwap = mean(swapAmount))

for(x in 1:nrow(total_NM_v2a)){
  total_NM_v2a$swapAvg[x] <- swapMeans$meanSwap[total_NM_v2a$subject[x]]
}

#find out which imagesequence had the most swaps
max(lengths(total_M_v2a$imageSequence))
which(lengths(total_M_v2a$imageSequence) == max(lengths(total_M_v2a$imageSequence)))

#------------------------#
# CLEAN UP               # 
#------------------------#

#Remove unneccessary columns
total_M_v2a$swapChoose = NULL
total_M_v2a$timings = NULL


#Make row numbering sequential
rownames(total_NM_v2a) <- 1:nrow(total_NM_v2a)
rownames(total_M_v2a) <- 1:nrow(total_M_v2a)

#FIND THE NA VALUES
which(is.na(total_M_v2a))


##################################################
# Add columns that get created in analysis here? #
##################################################

#Create Log Column
total_M_v2a$logRT <- log(total_M_v2a$rt)
#Create Accuracy Column
subject_accuracy <- group_by(total_M_v2a, subject) %>%
  dplyr::summarize(accuracy = mean(correct, na.rm = T))

for(x in 1:nrow(total_M_v2a)){
  total_M_v2a$accuracy[total_M_v2a$subject == x] <- subject_accuracy$accuracy[subject_accuracy==x]
}

subject_accuracy <- group_by(total_NM_v2a, subject) %>%
  dplyr::summarize(accuracy = mean(correct, na.rm = T))

for(x in 1:nrow(total_NM_v2a)){
  total_NM_v2a$accuracy[total_NM_v2a$subject == x] <- subject_accuracy$accuracy[subject_accuracy==x]
}

#Create abs(SummedValue) Column
total_M_v2a$absSummedVal <- abs(total_M_v2a$summedVal)
total_NM_v2a$absSummedVal <- abs(total_NM_v2a$summedVal)

#Create MultNum Column
total_M_v2a$multNum[total_M_v2a$mult1House==1 & total_M_v2a$mult2Face==1] <- 0
total_M_v2a$multNum[total_M_v2a$mult1House>1 & total_M_v2a$mult2Face==1] <- 1
total_M_v2a$multNum[total_M_v2a$mult1House==1 & total_M_v2a$mult2Face>1] <- 1
total_M_v2a$multNum[total_M_v2a$mult1House>1 & total_M_v2a$mult2Face>1] <- 2

#Create Difficulty Column
total_M_v2a$difficulty <- 0;
total_M_v2a$difficulty[total_M_v2a$absSummedVal<0.5] = 1;

#create face total and house total columns
total_M_v2a$faceTotal <- total_M_v2a$faceVal*total_M_v2a$mult2Face
total_M_v2a$houseTotal <- total_M_v2a$houseVal*total_M_v2a$mult1House

#----------------------#
# Bin Face/House Vals  #
#----------------------#

# FACE VAL
numBins = 9
# SUMMED VAL
total_M_v2a$faceValBin <- as.numeric(cut2(total_M_v2a$faceTotal, g=numBins))
total_M_v2a$faceValBinAmt <- cut2(total_M_v2a$faceTotal, g=numBins)
total_M_v2a$faceValBinCtr <- cut2(total_M_v2a$faceTotal, g=numBins, levels.mean=TRUE)
# Round to 2 decimal places
total_M_v2a$faceValBinCtr <- format(round(as.numeric(as.character(total_M_v2a$faceValBinCtr)), 2), nsmall = 2)

# HOUSE VAL
numBins = 9
# SUMMED VAL
total_M_v2a$houseValBin <- as.numeric(cut2(total_M_v2a$houseTotal, g=numBins))
total_M_v2a$houseValBinAmt <- cut2(total_M_v2a$houseTotal, g=numBins)
total_M_v2a$houseValBinCtr <- cut2(total_M_v2a$houseTotal, g=numBins, levels.mean=TRUE)
# Round to 2 decimal places
total_M_v2a$houseValBinCtr <- format(round(as.numeric(as.character(total_M_v2a$houseValBinCtr)), 2), nsmall = 2)


#create firstImage column
for(x in 1:nrow(total_M_v2a)){
  total_M_v2a$firstImage[x] <- total_M_v2a$imageSequence[x][[1]][1]
}

for(x in 1:nrow(total_NM_v2a)){
  total_NM_v2a$firstImage[x] <- total_NM_v2a$imageSequence[x][[1]][1]
}

#create firstVal column [face is 0, house is 1]
for(x in 1:nrow(total_M_v2a)){
  if (total_M_v2a$firstImage[x] == 0){
    total_M_v2a$firstVal[x] <- total_M_v2a$faceTotal[x]
  }
  if (total_M_v2a$firstImage[x] == 1){
    total_M_v2a$firstVal[x] <- total_M_v2a$houseTotal[x]
  }
}
    # non-mult
for(x in 1:nrow(total_NM_v2a)){
  if (total_NM_v2a$firstImage[x] == 0){
    total_NM_v2a$firstVal[x] <- total_NM_v2a$faceTotal[x]
  }
  if (total_NM_v2a$firstImage[x] == 1){
    total_NM_v2a$firstVal[x] <- total_NM_v2a$houseTotal[x]
  }
}

#create secondVal column [face is 0, house is 1 BUT since it is the second image it is the opposite]
for(x in 1:nrow(total_M_v2a)){
  if (total_M_v2a$firstImage[x] == 1){
    total_M_v2a$secondVal[x] <- total_M_v2a$faceTotal[x]
  }
  if (total_M_v2a$firstImage[x] == 0){
    total_M_v2a$secondVal[x] <- total_M_v2a$houseTotal[x]
  }
}
    # non-mult
for(x in 1:nrow(total_NM_v2a)){
  if (total_NM_v2a$firstImage[x] == 1){
    total_NM_v2a$secondVal[x] <- total_NM_v2a$faceTotal[x]
  }
  if (total_NM_v2a$firstImage[x] == 0){
    total_NM_v2a$secondVal[x] <- total_NM_v2a$houseTotal[x]
  }
}

#create firstMult column [face is 0, house is 1]
for(x in 1:nrow(total_M_v2a)){
  if (total_M_v2a$firstImage[x] == 0){
    total_M_v2a$firstMult[x] <- total_M_v2a$mult2Face[x]
  }
  if (total_M_v2a$firstImage[x] == 1){
    total_M_v2a$firstMult[x] <- total_M_v2a$mult1House[x]
  }
}

#create secondMult column (reverse the house/face values)
for(x in 1:nrow(total_M_v2a)){
  if (total_M_v2a$firstImage[x] == 1){
    total_M_v2a$secondMult[x] <- total_M_v2a$mult2Face[x]
  }
  if (total_M_v2a$firstImage[x] == 0){
    total_M_v2a$secondMult[x] <- total_M_v2a$mult1House[x]
  }
}

#CREATE NEW COLUMN for multDif
total_M_v2a$multDif = abs(total_M_v2a$mult1House - total_M_v2a$mult2Face)

# Fixation Timings
for(fixNum in 1:13){
  for(x in 1:nrow(total_M_v2a)){
    total_M_v2a[[paste0(fixNum, "_fixation")]][x] <- total_M_v2a$fixation_timing[x][[1]][fixNum]
  }
}

    # Non Mult
for(fixNum in 1:13){
  for(x in 1:nrow(total_NM_v2a)){
    total_NM_v2a[[paste0(fixNum, "_fixation")]][x] <- total_NM_v2a$fixation_timing[x][[1]][fixNum]
  }
}


##############
# Clean Data
##############
max(total_M_v2a$rt)

# 45 subjects
#remove earnings below 0
total_M_clean <- total_M_v2a[!(total_M_v2a$finalEarnings<0),]
total_NM_clean <- total_NM_v2a[!(total_NM_v2a$finalEarnings<0),]

length(unique(total_M_clean$subject))
# 33 
#remove swap avgs less than 1.5
total_M_clean <- total_M_clean[!(total_M_clean$swapAvg<1.5),]
total_NM_clean <- total_NM_clean[!(total_NM_clean$swapAvg<1.5),]

# 24
#MORE AGRESSIVE: REMOVE BELOW 70% 
total_M_clean2 <- total_M_clean[!(total_M_clean$accuracy<0.70),]
total_NM_clean <- total_NM_clean[!(total_NM_clean$accuracy<0.70),]

length(unique(total_M_clean2$subject))

# Remove reactions faster than .2 seconds
# https://www.humanbenchmark.com/tests/reactiontime/statistics
total_M_clean2<- total_M_clean2[!(total_M_clean2$rt<0.2),]
total_NM_clean<- total_NM_clean[!(total_NM_clean$rt<0.2),]

length(total_M_clean2$Trial)
#REMOVE TRIALS where they did not look at BOTH images
#total_M_clean2 <- total_M_clean2[!(total_M_clean2$swapAmount==1), ]


# Remove outlier (mainly slow) reactions using MAD
# https://rpubs.com/hauselin/outliersDetect
# https://www.r-bloggers.com/absolute-deviation-around-the-median/
  
outliersMAD <- function(data, MADCutOff = 2.5, replace = NA, values = FALSE, bConstant = 1.4826, digits = 2) {
  #compute number of absolute MADs away for each value
  #formula: abs( ( x - median(x) ) )/ mad(x)
  absMADAway <- abs((data - median(data, na.rm = T))/mad(data, constant = bConstant, na.rm = T))
  #subset data that has absMADAway greater than the MADCutOff and replace them with replace
  #can also replace values other than replace
  data[absMADAway > MADCutOff] <- replace
  
  if (values == TRUE) { 
    return(round(absMADAway, digits)) #if values == TRUE, return number of mads for each value
  } else {
    return(round(data, digits)) #otherwise, return values with outliers replaced
  }
}

total_M_clean3 <- total_M_clean2[!(outliersMAD(total_M_clean2$rt, values=T) > 5),]
total_NM_clean2 <- total_NM_clean[!(outliersMAD(total_NM_clean$rt, values=T) > 5),] 
max(total_M_clean3$rt)
max(total_NM_clean2$rt)

length(total_M_clean3$Trial)

#SAVE Rdata FILE
S_NM <- total_NM_clean2
save(S_NM, file = "~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis/Data/S_NM.Rdata")

S_NM_raw <- total_NM_v2a
save(S_NM_raw, file = "~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis/Data/S_NM_raw.Rdata")

S_M <- total_M_clean3
save(S_M, file = "~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis/Data/S_M.Rdata")

S_M_raw <- total_M_v2a
save(S_M_raw, file = "~/Dropbox/PROGRAMMING/_NEURO/2017_MADE/Analysis/Data/S_M_raw.Rdata")

##SAVE as CSV FILE
df = subset(total_M_clean3, select = -c(timings2, fixation_timing, imageSequence, acceptReject))
write.csv(df, file = "savedFiles/v2Mult.csv")
write.csv(df, file = "~/Dropbox/PROGRAMMING/PythonLearning/DDM/examples/v2Mult.csv") #Write to hDDM folder
write.csv(df, file = "~/Dropbox/PROGRAMMING/_NEURO/hDDM_Clithero/Code/Data/CSV_data/s_m.csv") #Write to clithero hDDM folder

