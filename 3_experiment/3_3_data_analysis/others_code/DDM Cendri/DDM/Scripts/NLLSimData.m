function NLLData = NLLSimData(Data, ProbMat, valPairs, RTBins)
% function NLLData = NLLSimData(Data, ProbMat, valPairs, RTBins)
%
% calculate the simulated negative log-likelihood of the data given a set
% of input parameters
% Data: structure with fields 'resp', 'rt', and drift values
%
% ProbMat: Matrix of simulated probability distribution of DDM response and
% RTs at different combinations of drifts
%
% valPairs: Key identifying each combination of drift value pairs in
% ProbMat
%
% RTBins - the RTBins used for grouping the data


% assign each data observation its corresponding probability, and transform
% it using the negative log of the probability
NLLDataProb = zeros(length(Data.resp),1);
for i = 1:length(Data.resp)
    % identify the correct conditions defining the probability
    Driftbin = intersect(find(Data.dim1(i) == valPairs(:,1)),find(Data.dim2(i) == valPairs(:,2)));
    Respbin = searchcell({0, 1},Data.resp(i)); % converted to drift-rate space
    RTbin = find(RTBins(Respbin,2:end) > Data.rt(i) & ...
                 RTBins(Respbin,1:end - 1) <= Data.rt(i));

    if isempty(RTbin) % non-response
        % assign the probability based on non-response
        NLLDataProb(i) = -log(ProbMat{Driftbin}(1,end) + eps);
    else
        % assign the probability based on response
        NLLDataProb(i) = -log(ProbMat{Driftbin}(Respbin,RTbin) + eps);
    end
end

% sum over all log(prob)
NLLData = sum(NLLDataProb);
