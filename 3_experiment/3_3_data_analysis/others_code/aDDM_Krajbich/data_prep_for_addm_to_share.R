#this requires a data file with a matrix in it called "data" that has each row as one fixation and the following columns (for 2-item choice):
#choice (1=left choice, 0=right choice)
#rt (reaction time in ms)
#leftval (value of the left item in arbitrary units)
#rightval (value of the right item in arbitrary units)
#roi (that fixation's region of interest; 1=left item, 2=right item)
#fixdur (duration of the current fixation in ms)
#fixnum (is this the trial's first fixation, second fixation, third fixation, etc.?)
#revfixnum (is this the trial's last fixation, second-to-last fixation, third-to-last fixation, etc.?)
#subject (this is optional; use it if you want to fit/simulate subjects one at a time)

#If you run into an error with "randfix" on, it is possible that you have trials without any fixations.  This will cause the code to crash.  You should remove those trials from the data, since the aDDM assumes that decisions are only happening during fixations.


rm(list=ls())
library(gtools)

#############specify options 
randfix<-1 #do you want to add random fixations when the data runs out?
load("et2_data_raw.RData") #specify the data file
#data<-sims #if you are reading in simulations
#data<-data[data$subject==10,] #use this for individual subject analysis
lower_bound<-0 #lower RT bound in ms
upper_bound<-100000 #upper RT bound in ms
dmaxfix<-max(data$revfixnum) #maximum number of fixations (use the data to specify)
#############################

#throw out "fast guesses" and really long outliers
data<-data[data$rt>lower_bound & data$rt<upper_bound,]

#basic features of the data
drois<-max(data$roi) #how many rois?
temp<-data[data$fixnum==1,]
dtrials<-nrow(temp) #how many trials total?
rm(temp)

#create version of dataset with only middle fixations (we use this later for drawing random middle fixations)
temp<-data[(data$fixnum>1 & data$revfixnum>1),]

#prepare data matrix
data_mat<-matrix(0,nrow=dtrials,ncol=(2+drois+dmaxfix*2)) #choice,rt,roi values,rois,fixation lengths



#two item case
if (drois==2){
	n=0
	for (i in 1:nrow(data)){
		if (data$fixnum[i]==1){
			n<-n+1
			data_mat[n,1]<-data$choice[i] #1=left choice, 0=right choice
			data_mat[n,2]<-data$rt[i] #in milliseconds
			data_mat[n,3]<-data$leftval[i] #left value
			data_mat[n,4]<-data$rightval[i] #right value
			data_mat[n,5]<-data$roi[i] #1=left, 2=right
			data_mat[n,(5+dmaxfix)]<-data$fixdur[i] #fixation duration in ms
		}
		if (data$fixnum[i]>1){
			data_mat[n,(4+data$fixnum[i])]<-data$roi[i]
			data_mat[n,(4+dmaxfix+data$fixnum[i])]<-data$fixdur[i]
		}
	}
}


#fill in missing fixation locations and durations for 2 items
if (randfix==1 & drois==2){
	####fill in missing fixation locations
	first_rois<-data_mat[,5]
	dim(first_rois)<-c(nrow(data_mat),1)
	second_rois<-3-data_mat[,5]
	dim(second_rois)<-c(nrow(data_mat),1)
	
	#cover the case of even nmaxfix
	if (even(dmaxfix)){
		roi_mat<-rep(c(first_rois,second_rois),floor(dmaxfix/2))
		dim(roi_mat)<-c(nrow(data_mat),(dmaxfix))
		data_mat[,5:(4+dmaxfix)]<-roi_mat
	}
	
	#cover the case of odd nmaxfix
	if (odd(dmaxfix)){
		roi_mat<-rep(c(second_rois,first_rois),floor(dmaxfix/2))
		dim(roi_mat)<-c(nrow(data_mat),(dmaxfix-1))
		data_mat[,6:(4+dmaxfix)]<-roi_mat
	}	
	
	####fill in missing fixation durations
	pfixmat<-sample(temp$fixdur,dmaxfix*nrow(data_mat),replace=TRUE)
	dim(pfixmat)<-c(nrow(data_mat),dmaxfix)
	
	#matrix with 1s for missing fixations and 0s for non-missing fixations
	fix_mat<-ceiling((1-(data_mat[1:nrow(data_mat),(5+dmaxfix):ncol(data_mat)]))/1000000)
	data_mat[1:nrow(data_mat),(5+dmaxfix):ncol(data_mat)]<-data_mat[1:nrow(data_mat),(5+dmaxfix):ncol(data_mat)]+fix_mat*pfixmat
}

#remove everything but data_mat
rm(data,dmaxfix,drois,dtrials,first_rois,fix_mat,i,n,pfixmat,randfix,roi_mat,second_rois,temp,lower_bound,upper_bound,j,prois)

#now save this workspace file with a name of your choosing (comment out for manual saving)
save(data_mat,file="et2_data_prepped.RData")

load("et2_data_prepped.RData")
