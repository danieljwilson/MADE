function Data = simulDDM(varargin)
% function simulDDM(params,[RespOptions],['ReturnTraces', % to return])
% Simulates a DDM for each input value [default = ones(1000,1)]
%
% params is a structure with fields for the variables for which
% non-default values wish to be specified
% 
% Parameters (and default values) are:
%
% 'inputvals' [ones(1000,1)] - specifies input for each requested ddm 
%    simulation on first dimension
% 'inputvals2' [ones(1000,1)] - specifies input for each requested ddm 
%    simulation on second dimension
%
% 'startvar' (.08) - variability in the starting point of each DDM -
%    uniformly distributed +/- around zero
%
% 'nondec' (300 ms) - non-decision processing time (e.g. motor)
% 'nondecvar' (50 ms) - variability in non-decision time (uniform)
% 'nondec2' (300 ms) - non-decision processing time (e.g. motor)
% 'nondecvar2' (50 ms) - variability in non-decision time (uniform)
%
% 'MaxRT' (Inf) - longest possible observed response. If given, DDMs that 
% have not terminated by this time are cut off and listed as non-responses
% Note that, for efficiency's sake, non-decision times are not included
% here, and must be accounted for separately to achieve actualy desired
% responses
%
% 'upper' (.15) - upper boundary
% 'lower' (.15) - lower boundary
%
% 'drift' (.08) - drift rate scalar for 1st dimension
% 'driftvar' (half of drift1) - cross-trial drift variability (Gaussian)
% 'drift2' (.08) - drift rate scalar for 2nd dimension
% 'driftvar2' (half of drift2) - drift variability (Gaussian) for 2nd
% dimension
%
% 'precision' (.001) - temporal precision, in secs, of simulated DDM
%
% Note: DDMs also use a fixed parameter (within-trial drift variability) that
% is not specified by the user. This is because it is essentially unidentified
% and functions simply as a scaling parameter. By convention it is set to .1
%
% RespOptions - optional variable specifying the possible responses that
% could be given by a subject (e.g., {0 1}, {'a','l'} etc.)
%
% ReturnTraces - optional variable specifying whether DDM traces should be
% retained. If used, requires additional specification of what fraction (0
% - 1) should be retained. This is usually required to be less than 1 for 
% memory reasons.
%
% Author: Cendri Hutcherson

% set defaults
inputvals = ones(1000,1);
inputvals2 = ones(1000,1);
nondec = .3; % non-decision time (in secs) for 1st dimension
nondecvar = .05; % variability in non-decision time (in secs) for 1st dimension
upper = .15;  % upper bound (correct answer)
lower = -.15;   % lower bound (incorrect answer)
drift = .08; % drift rate (units/sec)
drift2 = .08; % drift rate (units/sec)
precision = .001; % simulation time precision in seconds
collapseRate = 0;

s = .1; % within-trial drift parameter, serving as scaling parameter that by convention is set to .1
MaxRT = Inf;
RespOptions = {-1 1};

% overwrite defaults if specified
if ~isempty(varargin)
    paramNames = fieldnames(varargin{1});
    params = varargin{1};
    
    for i = 1:length(paramNames)
        eval([paramNames{i} '= params.' paramNames{i} ';']);
    end
end

% MaxRT = Inf;
% if any(strcmp(varargin,'MaxRT'))
%     MaxRT = varargin{find(strcmp(varargin,'MaxRT')) + 1};
% end

% specify variability in relationship to different parameters if not
% already specified
if ~exist('startvar','var')
    startvar = .25 * (upper - lower); % variability in starting point of the ddm process
end

if ~exist('driftvar','var')
    driftvar = .5 * drift; % variability in trial-to-trial drift rate
end

if ~exist('driftvar2','var')
    driftvar2 = .5 * drift2;
end

nSims = length(inputvals);

if any(strcmp(varargin,'ReturnTraces'))
    ReturnTraces = 1;
    PercentRetained = varargin{find(strcmp(varargin,'ReturnTraces')) + 1};
    TracesToRetain = round(linspace(1,nSims,nSims*PercentRetained));
    traces = NaN * zeros(length(TracesToRetain),min(MaxRT*1000,5000));
else
    ReturnTraces = 0;
end

% initialize some parameters for the requested drift passages
withinBounds = true(nSims,1);
ddms = zeros(nSims,1) + startvar * (rand(nSims,1) - .5); % initialize location vector for each drift
resp = NaN * ones(nSims,1); % initialize choices
rt = NaN * ones(nSims,1); % initialize RT
drift = drift*inputvals + driftvar*randn(nSims,1); % set drifts for each simulation
drift2 = drift2*inputvals2 + driftvar2*randn(nSims,1); % set drifts for each simulation

% simulate the ddms
% entry = nondec + nondecvar * (rand(length(rt),1) - .5);
% if entry < 0 % catch for negative non-decision times
%     entry = 0;
% end

t = 0;
initUpper = upper;
AUC = zeros(length(drift),1);
AUC2 = zeros(length(drift),1);
while t < (MaxRT/precision) && sum(withinBounds) % any paths still going
    t = t+1;

    meandrift = (drift(withinBounds) + drift2(withinBounds))/2; % take the average of the two drifts
    dy = meandrift*precision + s*sqrt(precision)*randn(sum(withinBounds),1);
    
    ddms(withinBounds) = ddms(withinBounds) + dy;
    AUC(withinBounds) = AUC(withinBounds) + abs(ddms(withinBounds));
    AUC2(withinBounds) = AUC2(withinBounds) + ddms(withinBounds);
    
    if ReturnTraces
        traces(:,t) = ddms(TracesToRetain);
    end
    withinBounds(ddms >= upper | ddms <= lower) = false;
    % select ddms that have completed but don't have response data recorded
    justDone = ~withinBounds & isnan(resp); 
    % log resp and RT data
    resp(justDone) = sign(ddms(justDone));
    rt(justDone) = t;
    
    % implement boundary collapse
    upper = initUpper * exp(-1 * collapseRate * t);
    lower = -1 * upper;
end

resp(withinBounds) = NaN;
rt(withinBounds) = NaN;
 
% add non-decision time for each simulation
rt = rt*precision;
% rt = rt + entry;

% recode responses into possible outputs (e.g. keys used by subject)
resp(resp == -1) = RespOptions{1};
resp(resp == 1) = RespOptions{2};

Data.rt = rt;
Data.resp = resp;
Data.drift = inputvals;
Data.drift2 = inputvals2 ;
Data.AUC = AUC;
Data.AUC2 = AUC2;

if ReturnTraces
    traces(:,round(1000*max(rt) + 1):end) = []; % remove NaNs
    Data.ddms = traces;
end

% fprintf('Mean RT = %.3f\n',mean(rt))
% fprintf('SD RT = %.3f\n',std(rt)*10000)
% fprintf('Percent correct = %.3f\n',mean(resp == 1))
% 
% hist(rt)