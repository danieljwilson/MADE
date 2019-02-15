function Data = simulDDM_normApprox(varargin)
% function simulDDM_normApprox([params])
% Determines the probability of boundary crossing for a DDM process given
% particular parameters, using several approximations to achieve a
% reasonable balance between accuracy and speed of estimation (the irony of
% which tradeoff is deeply appreciated)
% Approximations include:
%  1) a discrete transition probability matrix, in both time and diffusion
%  space (see simPrecision and numSteps variables)
%  2) a discrete/limited updating of transition probabilities under
%  conditions of collapsing barriers
%
% Author: Cendri Hutcherson
% Date: 04/05/2015
%
% Arguments:
% params - a structure with fields that specify core variables of the DDM 
% and levels of precision desired for the approximation. If params is not 
% given, or does not contain a fieldname for a given variable, the default
% value will be used
%
% driftRate: scalar/vector specifying the rate(s) of value accumulation
%            default = .08
% barrier: decision threshold
%          default = .15;
% barrierCollapse: rate at which the decision threshold collapses to 0
%                  default = 0
% startPt: bias in starting point
%          default = 0;
% nonDec: non-decision time (sum of sensory and motor delays, in secs)
%         default = .3;
% maxRT: maximum response time limit (in secs)
%        default = 4 seconds
% s: noise parameter, by convention set to .1 (all other parameter values
%    will scale to this noise term)
% simPrecision: discrete time step (in secs) to estimate state transitions
%               default = .001
% summaryPrecision: time step for reporting probabilities (in secs)
%                   helps if you want to compress variables for storage; 
%                   also smooths out bumps in probabilities when using the
%                   barrierCollapse variable, which is particularly sensitive
%                   to the bin size in the approximation                 
%                   default = .001 (no compression)
% numSteps: bin size for estimate diffusion movement (this is the heart of
%           approximation that allows for faster computation)
% barrierUpdateStep: variable (in units of simPrecision) that determines how often
%                    transition probabilities should be updated to account
%                    for new barriers
%                    most useful as a way to speed up computation without
%                    losing too much in the way of accuracy, but it will
%                    introduce some subtle deviations from "true" probs
%                    default = 50 (determined after some fiddling with
%                    tradeoff between accuracy and speed)
%
% Output:
% Data structure each separate driftRate value with following fields:
% pCross1: prob of a no response in each time-bin (uses summaryPrecision)
% pCross2: prob of a yes response in each time-bin
% pNonResp: probability of no response within given time limit
%
% Notes: 
% 1) The core approximation (disrete bins for estimating transition
% probabilities) is a Matlab adaptation of python scripts by Gabriela Tavares
% 2) There is also a companion script (simulDDM_exactSim) that will generate
% actual simulated DDM paths using the same parameter structure specified
% here. simulDDM_exactSim is slower, but can be useful both for answering 
% specific scientific questions about the nature of the DDM paths, as well 
% as for getting a sense of the differences between the approximation 
% method and a more direct simulation approach


%% ----------------- INITIALIZE PARAMETERS OF MODEL ---------------------%%

% set defaults for inputs to DDM (e.g. integrated value of the option)
driftRate = .08; % value of the option

% set defaults for parameters of DDM
barrier = .15;  % bounds on DDM process (defines -barrier and +barrier)
barrierCollapse = 0;
startPt = 0;
nonDec = .3; % non-decision time for each attribute
maxRT = 4;
s = .1; % within-trial drift parameter, serving as scaling parameter that by convention is set to .1

% set defaults for estimation
simPrecision = .001; % simulation time precision in seconds
summaryPrecision = .001; % precision for summary - helps to condense for data storage

numSteps = 50; % defines granularity of states
barrierUpdateStep = 50;

% overwrite defaults for any specified parameters (contained in params
% structure)
if ~isempty(varargin)
    paramNames = fieldnames(varargin{1});
    params = varargin{1};
    
    for i = 1:length(paramNames)
        eval([paramNames{i} '= params.' paramNames{i} ';']);
    end
end

%% -------------- SET UP AND RUN DDM  -------------- %%
nTimeSteps = floor(maxRT/simPrecision);

binLowEdge = [-Inf linspace(-barrier, barrier, numSteps + (mod(numSteps,2) == 1))]; % define bins for each drift state
binHiEdge = [linspace(-barrier, barrier, numSteps + (mod(numSteps,2) == 1)) Inf];
CoMstates = (binLowEdge + binHiEdge)/2; % define the center of each state-bin

% mus = inputvals*driftRates/length(driftRates); % integrated value mu for each trial

% create distance matrices for the low and high end of each bin from each
% bin center
allDiffsLo = repmat(binLowEdge',1,length(CoMstates)) - repmat(CoMstates,length(CoMstates),1);
allDiffsHi = repmat(binHiEdge',1,length(CoMstates)) - repmat(CoMstates,length(CoMstates),1);


for i = 1:length(driftRate)
    pStates = zeros(length(CoMstates),1); % # of states + 2 absorbing states (boundary crosses)
    pStates(find(binLowEdge <= startPt & binHiEdge > startPt,1)) = 1; % start with 100% probability mass at starting point

    cumCrossUp = zeros(nTimeSteps,1);
    cumCrossDown = zeros(nTimeSteps,1);

    % estimate transition probabilities for remaining 
    pDiffsLo = normcdf(allDiffsLo,driftRate(i)*simPrecision,s*sqrt(simPrecision));
    pDiffsHi = normcdf(allDiffsHi,driftRate(i)*simPrecision,s*sqrt(simPrecision));
    pTransit = pDiffsHi - pDiffsLo; % creates transition matrix from state to state
    pTransit(isnan(pTransit)) = 1;

    for t = (1 + floor(nonDec/simPrecision)):nTimeSteps
        barrierNow = barrier/(1 + barrierCollapse*(t - 1 - floor(nonDec/simPrecision)));
        absorbingLow = +(binHiEdge <= -barrierNow); % states firmly past barrier
        transStateDown = find(binLowEdge < -barrierNow & binHiEdge >= -barrierNow); % states in transition paste barrier
        if transStateDown > 1 && mod(t,barrierUpdateStep) == 0
            % we'll use a fudge here of assigning transitions to ANY state
            % beyond the barrier to the one closest to the barrier
            pTransit(absorbingLow == 1,:) = 0;
            % get probability in the bin of transitioning beyond
            pTransBarrier = normcdf(-barrierNow - CoMstates, driftRate(i)*simPrecision, s*sqrt(simPrecision));
            pJumpToRemainder = 1 - sum(pTransit((transStateDown + 1):end,:)) - pTransBarrier;
            pTransit(transStateDown - 1,:) = pTransBarrier;
            pTransit(transStateDown,:) = pJumpToRemainder;
        end

        absorbingHi = +(binLowEdge >= barrierNow); % states firmly past barrier
        transStateUp = find(binHiEdge > barrierNow & binLowEdge <= barrierNow); % states in transition paste barrier
        if transStateUp < length(absorbingHi) && mod(t,barrierUpdateStep) == 0
            % get probability in the bin of transitioning beyond
            pTransit(absorbingHi == 1,:) = 0;
            pTransBarrier = 1 - normcdf(barrierNow - CoMstates, driftRate(i)*simPrecision, s*sqrt(simPrecision));
            pJumpToRemainder = 1 - sum(pTransit(1:transStateUp - 1,:)) - pTransBarrier;
            pTransit(transStateUp + 1,:) = pTransBarrier;
            pTransit(transStateUp,:) = pJumpToRemainder;
        end
        % estimate cumulative fraction of DDMs in absorbing states
        cumCrossUp(t) = absorbingHi*pStates;
        cumCrossDown(t) = absorbingLow*pStates;

        absorbMat = +diag(absorbingLow | absorbingHi);
        pTransitAtT = pTransit;
        pTransitAtT(:,absorbingLow | absorbingHi) = absorbMat(:,absorbingLow | absorbingHi);
        pStates = pTransitAtT*pStates;
        if(sum(pStates(~absorbingLow & ~absorbingHi)) < eps)
            break;
        end
    end

    cumCrossUp(t+1:end) = cumCrossUp(t);
    cumCrossDown(t+1:end) = cumCrossDown(t);
    pCross1 = [0;diff(cumCrossDown)];
    pCross2 = [0;diff(cumCrossUp)];
    condenseFactor = summaryPrecision/simPrecision;
    if condenseFactor > 1
        pCross1 = reshape(pCross1,condenseFactor,length(pCross1)/condenseFactor);
        pCross1 = sum(pCross1,1);
        pCross2 = reshape(pCross2,condenseFactor,length(pCross2)/condenseFactor);
        pCross2 = sum(pCross2,1);
    end

    Data(i).pCross1 = pCross1;
    Data(i).pCross2 = pCross2;
    Data(i).pNonResp = 1 - sum(Data(i).pCross1) - sum(Data(i).pCross2);
end