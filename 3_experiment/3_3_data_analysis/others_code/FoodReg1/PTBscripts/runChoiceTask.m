function varargout = runChoiceTask(varargin)
%
% Script for running a single subject through a ratings task, to collect measures of 
% subjective perceptions of health and taste for the self-other
% decision-making task
%
% Author: Cendri Hutcherson
% Last modified: Sept. 26, 2013

% try % for debugging purposes

%% --------------- START NEW DATAFILE FOR CURRENT SESSION --------------- %
    studyid = 'FoodReg1'; % change this for every study
    homepath = determinePath(studyid);
if isempty(varargin)
    addpath([homepath filesep 'PTBScripts'])
    PTBParams = InitPTB(homepath,'DefaultSession','ChoiceTask');
else
    PTBParams = varargin{1};
    PTBParams.inERP = 0;
    Data.subjid = PTBParams.subjid;
    Data.ssnid = 'ChoiceTask';
    Data.time = datestr(now);
 
    PTBParams.datafile = fullfile(PTBParams.homepath, 'SubjectData', ...
                         num2str(PTBParams.subjid), ['Data.' num2str(PTBParams.subjid) '.' Data.ssnid '.mat']);
    save(PTBParams.datafile, 'Data')
end

%% ----------------------- INITIALIZE VARIABLES ------------------------- %
PTBParams.imgpath = fullfile(PTBParams.homepath,'PTBScripts');
foodPathIndex = regexp(PTBParams.homepath,studyid);
PTBParams.foodPath = fullfile(PTBParams.homepath(1:foodPathIndex - 1),'AllFoodPics');

[PTBParams.StartButton, PTBParams.StartButtonSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'StartButton.png'), 'PNG', PTBParams);
[PTBParams.StartButtonHighlighted, PTBParams.StartButtonSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'StartButton_highlighted.png'), 'PNG', PTBParams);
[PTBParams.YesButton, PTBParams.YesButtonSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'YesButton.png'), 'PNG', PTBParams);
[PTBParams.YesButtonHighlighted, PTBParams.YesButtonHighlightedSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'YesButton_highlighted.png'), 'PNG', PTBParams);
[PTBParams.NoButton, PTBParams.NoButtonSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'NoButton.png'), 'PNG', PTBParams);
[PTBParams.NoButtonHighlighted, PTBParams.NoButtonHighlightedSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'NoButton_highlighted.png'), 'PNG', PTBParams);

if mod(PTBParams.subjid,4) < 2
    PTBParams.RLOrder = 0;
else
    PTBParams.RLOrder = 1;
end

[PTBParams.NatInsrx, PTBParams.NatPicSize] = ...
    makeTxtrFromImg(fullfile(PTBParams.imgpath, 'NatInsrx.png'), 'PNG', PTBParams);
if mod(PTBParams.subjid,2) == 0
    [PTBParams.RegInsrx, PTBParams.RegPicSize] = ...
        makeTxtrFromImg(fullfile(PTBParams.imgpath, 'HealthInsrx.png'), 'PNG', PTBParams);
else
    [PTBParams.RegInsrx, PTBParams.RegPicSize] = ...
        makeTxtrFromImg(fullfile(PTBParams.imgpath, 'DecreaseInsrx.png'), 'PNG', PTBParams);
end

%% create pairs of foods for choices, using attribute ratings if they exist,
% and normative ratings if they don't

subjRatingFile = fullfile(PTBParams.homepath,'SubjectData',num2str(PTBParams.subjid),...
        ['Data.', num2str(PTBParams.subjid), '.AttributeRatings-Pre.mat']);
if exist(subjRatingFile,'file')
    RateData = load(subjRatingFile);
    RateData = RateData.Data;
    
    RateData.Resp = cell2mat(RateData.Resp);
    RateData.Taste = RateData.Resp(strcmp(RateData.Attribute,'Taste'));
    RateData.Health = RateData.Resp(strcmp(RateData.Attribute,'Health'));
    RateData.Liking = RateData.Resp(strcmp(RateData.Attribute,'Liking'));
else
    fid = fopen(fullfile(PTBParams.homepath,'NormedFoodRatings.txt'));
    temp = textscan(fid,'%s','HeaderLines',1,'Delimiter','\t');
    temp = reshape(temp{1},11,236)';
    RateData.Food = temp(:,2)';
    
    RateData.Taste = temp(:,9)';
    RateData.Health = temp(:,6)';
    RateData.Taste = cellfun(@(x)str2num(x),RateData.Taste);
    RateData.Health = cellfun(@(x)str2num(x),RateData.Health);
end

%         1        |        2
% Tasty-Unhealthy  |  Tasty-Healthy
% -----------------------------------
%         3        |        4
% Untasty-Unhealthy| Untasty-Healthy

Quad1Foods = RateData.Food(RateData.Taste > 3 & RateData.Health <= 3);
Quad2Foods = RateData.Food(RateData.Taste > 3 & RateData.Health > 3);
Quad3Foods = RateData.Food(RateData.Taste <= 3 & RateData.Health <=3);
Quad4Foods = RateData.Food(RateData.Taste <= 3 & RateData.Health > 3);

FoodOrderNat = [Quad1Foods(1:2:length(Quad1Foods)), ...
                Quad2Foods(1:2:length(Quad2Foods)), ...
                Quad3Foods(1:2:length(Quad3Foods)), ...
                Quad4Foods(1:2:length(Quad4Foods))];
FoodOrderNat = FoodOrderNat(randperm(size(FoodOrderNat,1)),:);
FoodOrderReg = [Quad1Foods(2:2:length(Quad1Foods)), ...
                Quad2Foods(2:2:length(Quad2Foods)), ...
                Quad3Foods(2:2:length(Quad3Foods)), ...
                Quad4Foods(2:2:length(Quad4Foods))];
FoodOrderReg = FoodOrderReg(randperm(size(FoodOrderReg,1)),:);    

if length(FoodOrderReg) > length(FoodOrderNat)
    diff = length(FoodOrderReg) - length(FoodOrderNat);
    FoodOrderNat = [FoodOrderNat FoodOrderReg(1:(diff/2))];
    FoodOrderReg(1:(diff/2)) = [];
else
    if length(FoodOrderReg) < length(FoodOrderNat)
        diff = length(FoodOrderNat) - length(FoodOrderReg);
        FoodOrderReg = [FoodOrderReg FoodOrderNat(1:(diff/2))];
        FoodOrderNat(1:(diff/2)) = [];
    end
end
SessionStartTime = GetSecs();
datafile = PTBParams.datafile;
logData(datafile,1,SessionStartTime);

% determine pseudorandom order of blocks (no more than 2 reps of any given
% block type)
BlockOrder = [];
for block = 1:10
    BlockOrder = [BlockOrder, randperm(2)];
end

datafile = PTBParams.datafile;
logData(datafile,1,FoodOrderNat,FoodOrderReg,BlockOrder);

trial = 0;
for block = 1:length(BlockOrder) %
    if BlockOrder(block) == 1
        InsrxPic = PTBParams.NatInsrx;
        InsrxSize = PTBParams.NatPicSize;
        Food = FoodOrderNat(1:10);
        FoodOrderNat(1:10) = [];
        Insrx = 'Respond Naturally';
    else
        InsrxPic = PTBParams.RegInsrx;
        InsrxSize = PTBParams.RegPicSize;
        Food = FoodOrderReg(1:10);
        FoodOrderReg(1:10) = [];
        if mod(PTBParams.subjid,2) == 0
            Insrx = 'Focus on Health';
        else
            Insrx = 'Decrease Desire';
        end
    end
    
    Screen('DrawTexture',PTBParams.win,InsrxPic,[],...
        findPicLoc(InsrxSize,[.5,.5],PTBParams,'ScreenPct',1));
    Screen('Flip',PTBParams.win);
    WaitSecs(5);
    
    for t = 1:10
        trial = trial + 1;   
        TrialData = runChoiceTrial(Food{t},Insrx,PTBParams);
        logData(PTBParams.datafile,trial,TrialData);
    end
    
    % give participants a break every 40 trials
    if mod(block,4) == 0 && block < 20
        DrawFormattedText(PTBParams.win,['You may now take a break.\n'...
            'Whenever you are ready to continue, press any key.'], 'center',...
            'center',PTBParams.white,40);
        Screen('Flip',PTBParams.win);
        collectResponse;
    end
    
end

SessionEndTime = datestr(now);
logData(datafile,1,SessionEndTime);

% show end-screen
% showInstruction(36,PTBParams);
    
% catch ME
%     ME
%     ME.stack.file
%     ME.stack.line
%     ME.stack.name
%     Screen('CloseAll');
%     ListenChar(1);
% end



%% ------------------------  CLEAN-UP AND END  -------------------------- %

if isempty(varargin)
    close all; Screen('CloseAll'); ListenChar(1);
end

%-------------------------------------------------------------------------%

%=========================================================================%
%                   FUNCTIONS CALLED BY MAIN SCRIPT                       %
%=========================================================================%

function path = determinePath(studyid)
	% determines path name, to enable some platform independence
	pathtofile = mfilename('fullpath');

	path = pathtofile(1:(regexp(pathtofile,studyid)+ length(studyid)));