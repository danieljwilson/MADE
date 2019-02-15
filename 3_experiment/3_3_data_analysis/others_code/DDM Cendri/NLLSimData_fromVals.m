function NLLData = NLLSimData_fromVals(Data, simParams, ProbMat, vals, paramIDs)
% function NLLData = NLLSimData(Data, simParams, ProbMat, uniqueVals, barrierCombos)
% calculate the simulated negative log-likelihood of the data given a set
% of input parameters
% Data: structure with fields 'resp', 'rt', and drift values
%
% ProbMat: Matrix of simulated probability distribution of DDM response and
% RTs at different combinations of drifts - generated from normal CDF method
%
% valPairs: Key identifying each combination of drift value pairs in
% ProbMat
%
% RTBins - the RTBins used for grouping the data


% assign each data observation its corresponding probability, and transform
% it using the negative log of the probability
NLLDataProb = zeros(length(Data.resp),1);  % create array to hold the summed neg. log likelihood probs

dataVals = round(Data.attribVals/5)*5 * simParams(end - 1:end)'; % DRIFT RATE recode to nearest 5 to match simulation values
dataVals = str2num(num2str(dataVals,4)); % recode to match stupid value rounding error - FIX THIS LATER!!!
Data.rt = Data.rt - simParams(3); % correct RT for non-decision time

for i = 1:length(Data.resp)
    % identify the correct value simulation to use
    Driftbin = vals == dataVals(i);
    if ~any(Driftbin)
        Driftbin = find(abs(vals - dataVals(i)) == min(abs(vals - dataVals(i))),1);
    end
    ProbMatToUse = ProbMat(Driftbin).SimData.ProbMat{paramIDs.upper == simParams(1), paramIDs.collapseRate == simParams(2)};

    RTbin = round(Data.rt(i) * 1000);
    if RTbin > 10000 % catches weird glitch where some RTs are slightly over 10 seconds
        RTbin = NaN;
    end
    
    if ~isnan(RTbin) % 
        % expand out course temporal resolution to fine temporal
        % resolution using linear interpolation (finer grained likelihood)
        temp = interp1(125:250:9875,ProbMatToUse(Data.resp(i) + 1,1:end-1),0:9999,'linear','extrap');
        temp(temp < 0) = 0;
        temp(temp > 1) = 1;
        temp = temp*(sum(ProbMatToUse(Data.resp(i) + 1,1:end - 1))/sum(temp)); % rescale to have same sum as original    
        if all(isnan(temp))
            temp = zeros(1,length(temp));
        end
        % assign the probability based on response
        if RTbin > 0
            NLLDataProb(i) = -log(temp(RTbin) + eps);
        else
            NLLDataProb(i) = -log(eps); % because you can't take negative log of zero
        end
    else
        % sum all responses that took place beyond the time limit (includes RTs
        % that would go beyond the time limit because of non-decision time
        temp1 = interp1(125:250:9875,ProbMatToUse(1,1:end-1),0:9999,'linear','extrap');
        temp1(temp1 < 0) = 0;
        temp1(temp1 > 1) = 1;
        temp1 = temp1*(sum(ProbMatToUse(1,1:end - 1))/sum(temp1));

        temp2 = interp1(125:250:9875,ProbMatToUse(2,1:end-1),0:9999,'linear','extrap');
        temp2(temp2 < 0) = 0;
        temp2(temp2 > 1) = 1;
        temp2 = temp2*(sum(ProbMatToUse(2,1:end - 1))/sum(temp2));
        
        if all(isnan(temp1))
            temp1 = zeros(1,length(temp1));
        end

        if all(isnan(temp2))
            temp2 = zeros(1,length(temp2));
        end
        pNonResp = ProbMatToUse(end,1) ...
            + sum(temp1((paramIDs.maxRT*1000 - simParams(3)*1000 + 1):end)) ...
            + sum(temp2((paramIDs.maxRT*1000 - simParams(3)*1000 + 1):end));
        NLLDataProb(i) = -log(pNonResp + eps); % assign probability of non-resp
    end
end

% sum over all log(prob)
NLLData = sum(NLLDataProb);
