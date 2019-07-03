# load choice data for all subjects

# load mouse Choice data for all subjects
MouseData = read.table(paste('SubjectData/',subjNames[1],'/MouseTracePerChoice_', subjNames[1], '.txt', sep = ""),sep = "\t",header = TRUE)

for(subj in 2:nSubjects){ # subjNames[2:nSubjects]
  print(paste('Loading', subjNames[subj]))
  temp = read.table(paste('SubjectData/', subjNames[subj], '/MouseTracePerChoice_', subjNames[subj], '.txt', sep = ""),sep = "\t",header = TRUE)
  MouseData = rbind.data.frame(MouseData,temp)
}
MouseData$Subject = as.factor(MouseData$Subject)

# load mouse Choice 100 data for all subjects
MouseData100 = read.table(paste('SubjectData/', subjNames[1], '/MouseTrace100PerChoice_', subjNames[1], '.txt', sep = ""),sep = "\t",header = TRUE)


for(subj in 2:nSubjects){
  temp = read.table(paste('SubjectData/', subjNames[subj], '/MouseTrace100PerChoice_', subjNames[subj], '.txt', sep = ""),sep = "\t",header = TRUE)
  MouseData100 = rbind.data.frame(MouseData100,temp)
}
MouseData100$Subject = as.factor(MouseData100$Subject)

# load choice data for all subjects
ChoiceData = read.table(paste('SubjectData/',subjNames[1],'/ChoiceData_', subjNames[1], '.txt', sep = ""),sep = "\t",header = TRUE)

for(subj in 2:nSubjects){
  temp = read.table(paste('SubjectData/',subjNames[subj],'/ChoiceData_', subjNames[subj], '.txt', sep = ""),sep = "\t",header = TRUE)
  ChoiceData = rbind.data.frame(ChoiceData,temp)
}

# load rating data for all subjects
RatingData = read.table(paste('SubjectData/',subjNames[1],'/RatingDataForGLM_', subjNames[1], '.txt', sep = ""),sep = "\t",header = TRUE)

for(subj in 2:nSubjects){
  temp = read.table(paste('SubjectData/',subjNames[subj],'/RatingDataForGLM_', subjNames[subj], '.txt', sep = ""),sep = "\t",header = TRUE)
  RatingData = rbind.data.frame(RatingData,temp)
}

ChoiceData$DrxFirstDevChoice[ChoiceData$DrxFirstDevChoice == -1] = 0
ChoiceData$Choice[ChoiceData$Choice == -1] = 0
ChoiceData$Condition = 'nat'
ChoiceData$Condition[ChoiceData$Instruction == 'Focus on Health'] = 'health'
ChoiceData$Condition[ChoiceData$Instruction == 'Decrease Desire'] = 'decrease'
