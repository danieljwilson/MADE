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
NLLDataProb = zeros(length(Data.resp),1);
dataVals = Data.attribVals * simParams(1:2)'; % recode to nearest 5 to match simulation values
%dataVals = str2num(num2str(dataVals,4)); % recode to match stupid value rounding error - FIX THIS LATER!!!
Data.rt = Data.rt - simParams(5); % correct RT for non-decision time
maxRT = paramIDs.maxRT;
for i = 1:length(Data.resp)
    % identify the correct value simulation to use
    % Note: simulations were run only with positive values, so negative
    % values will require a flip of yes/no frequencies later (see circshift line). Here, we are
    % just identifying the appropriate absolute drift rate that is closest
    % to the trial's value
    Driftbin = find(abs(vals - abs(dataVals(i))) == min(abs(vals - abs(dataVals(i)))),1);
    
    ProbMatToUse = ProbMat(Driftbin).SimData.ProbMat{paramIDs.upper == simParams(3), paramIDs.collapseRate == simParams(4)};

    if dataVals(i) < 0 % recode simulations if the trial involves a negative value (because only positive values were simulated)
        % note that the last column of ProbMat is non-responses, so we
        % retain that in its original position
        ProbMatToUse = [circshift(ProbMatToUse(:,1:end - 1),1), ProbMatToUse(:,end)];
    end
    
    RTbin = round(Data.rt(i) * 1000);
    if RTbin > maxRT*1000 % catches weird glitch where some RTs are slightly over the time limit
        if RTbin < maxRT*1000 + 20
            RTbin = maxRT*1000;
        else
            RTbin = NaN;
        end
    end
    
    if ~isnan(RTbin) % 
        % expand out course temporal resolution to fine temporal
        % resolution using linear interpolation
        temp = interp1(50:100:9950,ProbMatToUse(Data.resp(i) + 1,1:end-1),0:9999,'linear','extrap');
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
            NLLDataProb(i) = -log(eps);
        end
    else
        % sum all responses that took place beyond the time limit (includes RTs
        % that would go beyond the time limit because of non-decision time
        temp1 = interp1(50:100:9950,ProbMatToUse(1,1:end-1),0:9999,'linear','extrap');
        temp1(temp1 < 0) = 0;
        temp1(temp1 > 1) = 1;
        temp1 = temp1*(sum(ProbMatToUse(1,1:end - 1))/sum(temp1));

        temp2 = interp1(50:100:9950,ProbMatToUse(2,1:end-1),0:9999,'linear','extrap');
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
            + sum(temp1((maxRT*1000 - simParams(5)*1000 + 1):end)) ...
            + sum(temp2((maxRT*1000 - simParams(5)*1000 + 1):end));
        NLLDataProb(i) = -log(pNonResp + eps); % assign probability of non-resp
    end
end

% sum over all log(prob)
NLLData = sum(NLLDataProb);
