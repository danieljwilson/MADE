% submit job to the cluster
pathtofile = mfilename('fullpath');
homepath = pathtofile(1:(regexp(pathtofile,'scripts')-1));

modelid = input('Model ID: ', 's');
%% get subject info and create submission info for each node
cd(homepath)
load('subjNameList.mat'); % subject IDs for each study

%% schedule tasks
% sched=findResource('scheduler', 'configuration', 'NeuroEcon.local');
sched=parcluster('scheduler', 'configuration', 'NeuroEcon.local');

pjob=createJob(sched);
set(sched, 'SubmitArguments', '-l walltime=168:00:00')
set(pjob,'PathDependencies',{homepath, [homepath 'scripts/'], '/home/chutcher/matlabextras'}) 
for s = 1:length(subjNameList)
     eval(['createTask(pjob, @' ...
           ['fitDDMFromSim_' modelid] ...
           ',2,{''' subjNameList{s} '''});'])
end
t = get(pjob, 'Tasks');
set(t, 'CaptureCommandWindowOutput', true)

submit(pjob)
waitForState(pjob)

results = getAllOutputArguments(pjob);

%% check for errors
nErrors = 0;
idError = [];
for i = 1:length(t)
    if ~isempty(t(i).ErrorMessage)
        nErrors = nErrors+1;
        idError = [idError i];
    end
end

%% housecleaning: delete job info if no errors
if nErrors == 0    
    dirname = pjob.Name;
    pause(2)
    unix(['rm -r ' homepath 'jobdata/' dirname '*']);
    fprintf('\nJob successfully completed.\n\n')
else
    fprintf('Errors were detected! History of first error: \n\n')
    t(idError(1))
end