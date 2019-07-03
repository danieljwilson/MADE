function ProbMat = getProbMat(Data, RTBins, params)
% function Prob = getProbMat(Data, RTBins)
% calculate a course likeihood function for each combination of inputs
%
% Author: Cendri Hutcherson

% get unique combinations of observed inputs
Pairs = unique([Data.drift,Data.drift2],'rows');
Pairs = sortrows(Pairs);

% get the conditional probabilities of a particular combination of response
% and RT for each given combination of inputs
for d = 1:size(Pairs,1)
    temp.resp = Data.resp(Data.drift == Pairs(d,1) & Data.drift2 == Pairs(d,2));
    temp.rt = Data.rt(Data.drift == Pairs(d,1) & Data.drift2 == Pairs(d,2));
    
    if(isfield(params,'MaxRT'))
        temp.resp(temp.rt > params.MaxRT) = NaN;
        temp.rt(temp.rt > params.MaxRT) = NaN;
    end

    [temp1 temp2] = ddm_observedprobs(temp,RTBins,params.RespOptions);
    ProbMat{d} = temp2;
end