function varargout = runPracticeForChoice(varargin)
%
% Script for running a single subject through instructions for the choice
% task, as well as practice trials
%
% Author: Cendri Hutcherson
% Last modified: Feb 15, 2016

% try % for debugging purposes

%% --------------- START NEW DATAFILE FOR CURRENT SESSION --------------- %
studyid = 'FoodReg1'; % change this for every study
if isempty(varargin)
    homepath = determinePath(studyid);
    addpath([homepath filesep 'PTBScripts'])

    PTBParams = InitPTB(homepath,'DefaultSession','Practice');
else
    PTBParams = varargin{1};
    PTBParams.inERP = 0;
    Data.subjid = PTBParams.subjid;
    Data.ssnid = 'Practice';
    Data.time = datestr(now);
 
    PTBParams.datafile = fullfile(PTBParams.homepath, 'SubjectData', ...
                         num2str(PTBParams.subjid), ['Data.' num2str(PTBParams.subjid) '.' Data.ssnid '.mat']);
    save(PTBParams.datafile, 'Data')
end

datafile = PTBParams.datafile;

%% ----------------------- INITIALIZE VARIABLES ------------------------- %  
SessionStartTime = GetSecs();
logData(datafile,1,SessionStartTime);
PTBParams.imgpath = fullfile(PTBParams.homepath,'PTBScripts');
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

%% show Instructions
insrx = 7;
while insrx >= 7 && insrx <= 14
    if insrx == 7
        showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','right'});
        insrx = insrx + 1;
    else
        Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
        if strcmp(Resp,'LeftArrow') || isequal(Resp,'left')
            insrx = insrx - 1;
        else
            insrx = insrx + 1;
        end
    end
end

% Run 4 trials of the natural focus instructional condition with these 
% practice foods
foodPathIndex = regexp(PTBParams.homepath,studyid);
PTBParams.foodPath = fullfile(PTBParams.homepath(1:foodPathIndex - 1),'AllFoodPics');

% load names of foods
PTBParams.PracticeFoodNames = {'WetBeanCurd_3_8pc.jpg','Tostitos_4_15chips.jpg','TeddyGrahams_4_80cookies.jpg',...
         'Spam_5_5spoons.jpg'};

for trial = randperm(4) 
    TrialData = runChoiceTrial(PTBParams.PracticeFoodNames{trial},'', PTBParams);
end


while insrx >= 15 && insrx <= 25
    switch insrx
        case 15
            showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','right'});
            if mod(PTBParams.subjid,2) == 0
                insrx = insrx + 1;
            else
                insrx = insrx + 2;
            end
        case {16,22}
            Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
            if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                insrx = insrx + 2;
            else
                insrx = insrx - 1;
            end
        case {17,18}
            Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
            if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                insrx = insrx + 2;
            else
                insrx = insrx - 2;
            end
        case {19,23}
            Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
            if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                insrx = insrx + 1;
            else
                insrx = insrx - 2;
            end
        case {20,24}
            Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
            if mod(PTBParams.subjid,2) == 0
                if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                    insrx = insrx + 1;
                else
                    insrx = insrx - 2;
                end
            else
                if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                    insrx = insrx + 1;
                else
                    insrx = insrx - 1;
                end
            end
        case {21}
            Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
            if mod(PTBParams.subjid,2) == 0
                if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                    insrx = insrx + 1;
                else
                    insrx = insrx - 1;
                end
            else
                if isequal(Resp,'RightArrow') || isequal(Resp,'right')
                    insrx = insrx + 2;
                else
                    insrx = insrx - 1;
                end
            end
        otherwise
            Resp = showInstruction(insrx,PTBParams,'RequiredKeys',{'RightArrow','LeftArrow','right','left'});
            if strcmp(Resp,'LeftArrow') || isequal(Resp,'left')
                insrx = insrx - 1;
            else
                insrx = insrx + 1;
            end
    end
end


% %======================   RUN COMPREHENSION QUIZ   =======================%

CorrectAnswers = [2, 3, 1, 3];

for q = 1:length(CorrectAnswers)
    QuizResp = showInstruction(insrx, PTBParams, 'RequiredKeys',PTBParams.numKeys(1:3));
    QuizResp = QuizResp(1);
    logData(datafile, q, QuizResp)
    
    CorrectResponse = str2num(QuizResp) == CorrectAnswers(q);
    fprintf('Question %d: %d\n',q,CorrectResponse)
    
    if CorrectResponse
        showInstruction(insrx + 1, PTBParams,'RequiredKeys',{'RightArrow','right'});
    else
        showInstruction(insrx + 2, PTBParams,'RequiredKeys',{'RightArrow','right'});
    end
    
    logData(datafile, q, CorrectResponse);
    
    insrx = insrx + 3;
end

showInstruction(insrx, PTBParams,'RequiredKeys',{'RightArrow','right'});


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