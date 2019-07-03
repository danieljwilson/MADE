pathtofile = mfilename('fullpath');
homepath = pathtofile(1:(regexp(pathtofile,'Analysis')-1));

model = input('Which model should we run?', 's');
scriptToRun = ['fitDDMFromSim_' model];
%% get subject info and create submission info for each node
cd(homepath)
load('subjNameList.mat'); % subject IDs for each study

%% schedule tasks
clu=parcluster('default_jobmanager');

pjob=createJob(clu);
set(pjob,'AdditionalPaths',{[homepath 'Analysis'],'/psyhome/u7/hutchers/matlabextras/'})
for s = 1:length(subjNameList)
     eval(['createTask(pjob, @' ...
           scriptToRun ...
           ', 2,{''' subjNameList{s} '''});'])
end
t = get(pjob,'Tasks');
submit(pjob)
wait(pjob,'finished')

results = fetchOutputs(pjob);

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

finished_jobs = findJob(clu,'State','finished','Username','hutchers');
delete(finished_jobs);