DDMopt = function(driftrate = 1, threshold = 500, startingPt = 0, ndt = 300){
  # DDM is a function for computing a single decision by using sequential evidence accumulation
  # The function returns a list of two variables:
  # 1) Decision (0 if reject, 1 if accept)
  # 2) Response Time (in milliseconds)
  # DDM uses some default values for drift rate, threshold, startingPt, and non-decision time
  Decision = NA 
  DDM = startingPt
  while(is.na(Decision)){
    DDM = c(DDM, DDM[length(DDM)] + driftrate*1:threshold + cumsum(rnorm(threshold, sd = 25)))
    crossingPts = which(DDM < -1*threshold | DDM > threshold)
    if(length(crossingPts) > 0){
      RT = min(crossingPts)
      Decision = sign(DDM[RT]) > 0
      DDM = DDM[1:RT]
    }
  }
  d = list(Decision = Decision > 0, RT = length(DDM) + ndt, driftTrace = DDM)
  return(d)
}

x = DDMopt(2,500,0,500)

plot(x$driftTrace)
