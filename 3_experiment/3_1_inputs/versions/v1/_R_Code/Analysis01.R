
####################
# ANALYSES
####################

#GROUP
#Percent Correct
mean(total_NM$correct)
mean(total_M$correct)

#Mean Response Time
mean(total_NM$decisionTime)
mean(total_M$decisionTime)

#Cleaned Mean Response Time
mean(total_NM_clean$decisionTime)
mean(total_M_clean$decisionTime)

#SD Response Time
#Cleaned Mean Response Time
sd(total_NM_clean$decisionTime)
sd(total_M_clean$decisionTime)

#Mean response time with multipliers
#RT WITH TWO multipliers
mean(total_M_clean$decisionTime[(total_M_clean$mult2Face>1) & (total_M_clean$mult1House>1)])
#vs WITHOUT
mean(total_M_clean$decisionTime[(total_M_clean$mult2Face<2) & (total_M_clean$mult1House<2)])
#with only FACE multiplier
mean(total_M_clean$decisionTime[(total_M_clean$mult2Face>1) & (total_M_clean$mult1House==1)])
#with only HOUSE multiplier
mean(total_M_clean$decisionTime[(total_M_clean$mult2Face==1) & (total_M_clean$mult1House>1)])

#BOXPLOT: mean RT vs mean 
boxplot(decisionTime ~ factor(subject),
        varwidth = TRUE, xlab = "subject",
        main = "Boxplot of RT conditional on\
        subject", ylab = "RT", data = total_M_clean)

#DOTPLOT: mean RT vs earnings
plot(y = total_M_clean$finalEarnings, x = mean(total_M_clean$decisionTime),
     xlab = "Mean RT Age Moby",
     ylab = "Final Earnings")
abline(M2)

#BAR PLOT
library(magrittr)
library(ggplot2)
library(dplyr)
#First get means for each condition of FLIP by Subject
d <- total_M_clean2

subject_means <- group_by(d, subject, flip) %>%
  summarize(rt = mean(decisionTime, na.rm = T))
subject_means

#PLOT
barplot <- ggplot(subject_means, aes(x = flip, y = rt)) +
  stat_summary(
    geom = "bar",
    fun.y = "mean",
    col = "black",
    fill = "gray70"
  ) +
  geom_point(position = position_jitter(h = 0, w = 0.2)) +
  scale_y_continuous(limits = c(0, max(d$decisionTime, na.rm = T)),
                     expand = c(0, 0))
barplot

#WITHIN SUBJECT SCATTER PLOT
library(tidyr)
subject_means_wide <-
  spread(subject_means,
         key = flip,
         value = rt,
         sep = "_")
subject_means_wide

#Then we can simply map the per-subject angle-means to the X and Y axes:
ggplot(subject_means_wide, aes(x = flip_1, y = flip_2)) +
  geom_point()

lims <- c(min(d$decisionTime, na.rm = T), max(d$decisionTime, na.rm = T))
wsplot <-
  ggplot(subject_means_wide, aes(x = flip_2, y = flip_1)) +
  geom_point() +
  geom_abline() +
  scale_x_continuous("no flip", limits = lims) +
  scale_y_continuous("flip", limits = lims) +
  theme(aspect.ratio = 1)
wsplot

#WITHING SUBJECT WITH SES
subject_summaries <- group_by(d, subject, flip) %>%
  summarize(mean = mean(decisionTime, na.rm = T),
            se = sd(decisionTime, na.rm = T) / sqrt(n()))
subject_summaries

#Now we simply need to reformat the data to wide with respect to both the means and SEs.
means <- select(subject_summaries, -se) %>%
  spread(key=flip, value=mean, sep = "_")
means

ses <- select(subject_summaries, -mean) %>%
  spread(key=flip, value=se, sep = "SE")
ses

sums <- left_join(means, ses)
sums 

ggplot(sums, aes(x=flip_2, y=flip_1)) +
  geom_point() +
  geom_errorbar(aes(ymin=flip_1-flipSE1*1.96, ymax=flip_1+flipSE1*1.96)) +
  geom_errorbarh(aes(xmin=flip_2-flipSE2*1.96, xmax=flip_2+flipSE2*1.96)) +
  geom_abline() +
  scale_x_continuous("NO FLIP", limits = lims) +
  scale_y_continuous("FLIP", limits = lims) +
  theme(aspect.ratio=1)

hist(tapply(total_M_clean$finalEarnings, total_M_clean$subject, function(x)mean(x)))

