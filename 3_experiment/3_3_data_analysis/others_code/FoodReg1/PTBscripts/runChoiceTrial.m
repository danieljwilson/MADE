function TrialData = runChoiceTrial(FoodOnTrial, Instruction, PTBParams)
%function TrialData = runChoiceTrial(FoodOnTrial, MoneyOnTrial, PTBParams)
%
% Usage: takes a string identifying a food picture (just the name, not the 
% full path, and a number identifying the monetary amount to offer, 
% displays them to the participant, and collects a yes-no response to the 
% choice-pair using the mouse to click on 'Yes' or 'No' buttons
%
% Trial structure:
%    1. Show the start button, and require the participant to click the
%    button to reveal the choice options
%    2. Present the proposal (one food-money pair) and collect yes-no
%    choice from particant using a mouse
% 
ctr = PTBParams.ctr;

%========================= 1. Brief blank screen  ========================%

% display a blank screen for 500ms
Screen('FillRect',PTBParams.win,PTBParams.black);%VERY VERY IMPORTANT
Screen(PTBParams.win,'Flip');


[PTBParams.FoodPic, PTBParams.FoodPicSize] = makeTxtrFromImg(fullfile(PTBParams.foodPath,FoodOnTrial),...
    'JPG',PTBParams);

FoodPicPosition = findPicLoc(PTBParams.FoodPicSize, [.5, .5], PTBParams, 'ScreenPct', .4);

%============  2. Display START button and yes/no buttons  ==============%

% draw the START button in the center near the bottom of the screen
% (centered at 87.5% of the way to the bottom), so that it
% occupies roughly 10% of the screen vertically and horizontally
StartButtonPosition = findPicLoc(PTBParams.StartButtonSize, [.5, .825], PTBParams, ...
    'ScreenPct',.1);
Screen('DrawTexture',PTBParams.win,PTBParams.StartButton,[],StartButtonPosition);
DrawFormattedText(PTBParams.win, Instruction, ...
                  'center',StartButtonPosition(4) + 20, ...
                  PTBParams.white);
%%%%% Screen('DrawTexture', windowPointer, texturePointer ,sourceRect,destinationRect)

if PTBParams.RLOrder
    YesButtonPosition = findPicLoc(PTBParams.YesButtonSize, [.15, .15], PTBParams, 'ScreenPct', .1);    
    NoButtonPosition = findPicLoc(PTBParams.NoButtonSize, [.85, .15], PTBParams, 'ScreenPct', .1);
else
    YesButtonPosition = findPicLoc(PTBParams.YesButtonSize, [.85, .15], PTBParams, 'ScreenPct', .1);    
    NoButtonPosition = findPicLoc(PTBParams.NoButtonSize, [.15, .15], PTBParams, 'ScreenPct', .1);
end

Screen('DrawTexture',PTBParams.win, PTBParams.YesButton, [], YesButtonPosition);
Screen('DrawTexture',PTBParams.win, PTBParams.NoButton, [], NoButtonPosition);

% Ensure criteria for beginning mouse parameters (start location, start
% velocity) are met before displaying proposal

StartAborted = 1;

% Lines 51-79 require the participant to click on the START button and
% start moving upward in order to reveal the choice option.
while StartAborted
    StartOn = Screen(PTBParams.win,'Flip',[],1);
    % Wait for participant to click on START button, then highlight it
    mouseTrack([], 1, PTBParams, StartButtonPosition);
    Screen('DrawTexture',PTBParams.win,PTBParams.StartButtonHighlighted,[],StartButtonPosition);
    StartClicked = Screen(PTBParams.win,'Flip',[],1);
    
    % Wait for participant to move the mouse above the top rim of the START 
    % button. If they have not moved it within 500 ms, restart the trial
    % with a warning that they didn't start to move fast enough
    RegionAboveStartButton = [StartButtonPosition(1),0,...
                              StartButtonPosition(3), StartButtonPosition(2)];
    
    [t1, t2, time] = mouseTrack(.5, 0, PTBParams, RegionAboveStartButton);
    if time(end) > .5 - PTBParams.ifi
        [t1, t2, TextBounds] = DrawFormattedText(PTBParams.win, ...
                            'TOO SLOW!\nSTART OVER.', 'center','center', PTBParams.white);
        TooSlowScreenOn = Screen(PTBParams.win,'Flip',[],1);
        Screen('FillRect', ...
               PTBParams.win, ...
               PTBParams.black, ...
               [ctr(1) - ceil(TextBounds(3)/2), ctr(2) - ceil(TextBounds(4)/2), ...
                ctr(1) + ceil(TextBounds(3)/2), ctr(2) + ceil(TextBounds(4)/2)]);
        Screen('DrawTexture', PTBParams.win, PTBParams.StartButton,[], StartButtonPosition);
        Screen(PTBParams.win,'Flip',TooSlowScreenOn + .5,1);

    else
        StartAborted = 0;
    end
end %%%%Don't really understand this...?

%=========== 3. Present food  and collect response =============%
Screen('FillRect',PTBParams.win,[0,0,0],StartButtonPosition);
Screen('DrawTexture',PTBParams.win, PTBParams.FoodPic, [], FoodPicPosition);

% Now that we've drawn the food and money, display them
FoodOn = Screen(PTBParams.win,'Flip',[],1);

% collect mouse-track data for as long as they need to decide
[ChoiceX,ChoiceY,ChoiceTime] = mouseTrack(10, 1, PTBParams, [YesButtonPosition; NoButtonPosition]);

%================= 4. Determine display for outcome period ===============%

Choice = sign(ChoiceX(end)-PTBParams.ctr(1));

if PTBParams.RLOrder
    Choice = -1 * Choice;
end
% Module 11: Draw a highlighted version of the button they chose
% Code hint 1: it may help to use an if statement that depends on the value
% of the 'Choice' variable

if Choice == 1
    Screen('DrawTexture',PTBParams.win, PTBParams.YesButtonHighlighted, [], YesButtonPosition);
else
    Screen('DrawTexture',PTBParams.win, PTBParams.NoButtonHighlighted, [], NoButtonPosition);
end

% Display the highlighted button
ChoiceMade = Screen(PTBParams.win,'Flip');    
ChoiceRT = ChoiceTime(end);

% After 250 ms, display blank screen
Screen(PTBParams.win,'Flip',ChoiceMade + .25);

if PTBParams.RLOrder % for right-left flipped subjects
    ChoiceX = -1 * ChoiceX; 
end

TrialData.FoodOnTrial = FoodOnTrial;
TrialData.InstructionOnTrial = Instruction;
TrialData.Choice = Choice;
TrialData.ChoiceX = ChoiceX;
TrialData.ChoiceY = ChoiceY;
TrialData.ChoiceTime = ChoiceTime; 

% To avoid memory issues, we close the texture associated with the food
% picture now that we are done using it
Screen('Close',PTBParams.FoodPic);
WaitSecs(.5);

    