function [FreqMatrix, PMatrix] = ddm_observedprobs(Data, RTBins, RespOptions)
% Data should be a structure with two fields: 'resp' and 'rt'
%
% RTBins should be a RespOptions x NumQuantiles + 1 matrix, with
% zeros as the first entry (to allow for binning of observations)
%
% RespOptions should be a cell matrix specifying the possible values that 
% could appear in Data.resp


% Initialize matrix for p(RT * response | trialtype) within RT bins
% FreqMatrix = zeros(length(RespOptions),size(RTBins,2) - 1);
%
% Author: Cendri Hutcherson

FreqMatrix = zeros(length(RespOptions),size(RTBins,2)); % include extra bin for non-responses

nObs = length(Data.resp);

for r = 1:length(RespOptions)
    for t = 1:size(RTBins,2) - 1
        FreqMatrix(r,t) = sum(Data.resp == RespOptions{r} & ...
                              Data.rt > RTBins(r,t) & ...
                              Data.rt <= RTBins(r,t+1));
    end % loop over trial types
end % loop over response types

% total non-responses
FreqMatrix(1,size(RTBins,2)) = sum(isnan(Data.rt));

PMatrix = FreqMatrix/sum(FreqMatrix(:));
