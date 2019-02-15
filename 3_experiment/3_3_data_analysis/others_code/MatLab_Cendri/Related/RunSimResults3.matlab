
>> SimData.inputvals(1)

ans =

   2.0000e-04

>> SimData.simFile

ans =

/psyhome/u5/wilso603/MADE01/Simulations/1_170828/Sim_0.000200.mat

>> SimData.params

ans(:,:,1) = 

  Columns 1 through 4

    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]

  Columns 5 through 8

    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]    [1x1 struct]

 

  Columns 9 through 11

    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]
    [1x1 struct]    [1x1 struct]    [1x1 struct]

>> SimData.params{1,1,1}

ans = 

        startvar: 0
       nondecvar: 0
        driftvar: 0
       driftvar2: 0
           MaxRT: 10
     RespOptions: {[0]  [1]}
       precision: 0.0100
               s: 0.1000
       inputvals: 2.0000e-04
           upper: 0.0200
    collapseRate: 0
       startBias: -0.3000

>> SimData.params{1,1,2}

ans = 

        startvar: 0
       nondecvar: 0
        driftvar: 0
       driftvar2: 0
           MaxRT: 10
     RespOptions: {[0]  [1]}
       precision: 0.0100
               s: 0.1000
       inputvals: 2.0000e-04
           upper: 0.0200
    collapseRate: 0
       startBias: -0.2500

>> SimData.params{5,1,2}

ans = 

        startvar: 0
       nondecvar: 0
        driftvar: 0
       driftvar2: 0
           MaxRT: 10
     RespOptions: {[0]  [1]}
       precision: 0.0100
               s: 0.1000
       inputvals: 2.0000e-04
           upper: 0.1000
    collapseRate: 0
       startBias: -0.2500

>> SimData.ProbMat{5,1,2}

ans =

  Columns 1 through 7

    0.0110    0.0649    0.0644    0.0572    0.0479    0.0416    0.0391
    0.0001    0.0041    0.0135    0.0210    0.0233    0.0271    0.0251

  Columns 8 through 14

    0.0336    0.0262    0.0264    0.0227    0.0179    0.0178    0.0175
    0.0253    0.0228    0.0230    0.0187    0.0169    0.0168    0.0144

  Columns 15 through 21

    0.0139    0.0131    0.0099    0.0094    0.0096    0.0073    0.0079
    0.0125    0.0117    0.0117    0.0087    0.0090    0.0075    0.0068

  Columns 22 through 28

    0.0052    0.0053    0.0052    0.0051    0.0041    0.0039    0.0034
    0.0058    0.0058    0.0041    0.0041    0.0033    0.0029    0.0028

  Columns 29 through 35

    0.0031    0.0033    0.0025    0.0016    0.0018    0.0024    0.0009
    0.0036    0.0028    0.0027    0.0021    0.0015    0.0017    0.0016

  Columns 36 through 42

    0.0017    0.0008    0.0013    0.0011    0.0008    0.0006    0.0007
    0.0013    0.0007    0.0014    0.0014    0.0005    0.0006    0.0015

  Columns 43 through 49

    0.0003    0.0005    0.0005    0.0005    0.0005    0.0007    0.0003
    0.0005    0.0008    0.0007    0.0003    0.0003    0.0003    0.0005

  Columns 50 through 56

    0.0005    0.0003    0.0002    0.0001    0.0001    0.0004         0
    0.0003    0.0003    0.0005    0.0005    0.0004    0.0003         0

  Columns 57 through 63

    0.0001    0.0002    0.0001    0.0002    0.0001         0    0.0001
    0.0001         0         0    0.0001    0.0001    0.0001    0.0002

  Columns 64 through 70

    0.0001         0    0.0003    0.0001    0.0001         0         0
         0         0         0    0.0001         0         0    0.0001

  Columns 71 through 77

    0.0001    0.0001         0    0.0002    0.0001         0         0
    0.0001         0    0.0001         0         0         0         0

  Columns 78 through 84

         0         0         0         0         0         0         0
         0    0.0001         0         0         0         0         0

  Columns 85 through 91

         0         0         0         0         0         0         0
         0         0         0         0         0         0         0

  Columns 92 through 98

         0         0         0         0         0         0         0
         0         0         0         0         0         0         0

  Columns 99 through 101

         0         0         0
         0         0         0

>> plot(SimData.ProbMat{5,1,2}(1,:))
>> hold on;
>> plot(SimData.ProbMat{5,1,2}(2,:), 'r')
>> SimData.params{5,1,2}

ans = 

        startvar: 0
       nondecvar: 0
        driftvar: 0
       driftvar2: 0
           MaxRT: 10
     RespOptions: {[0]  [1]}
       precision: 0.0100
               s: 0.1000
       inputvals: 2.0000e-04
           upper: 0.1000
    collapseRate: 0
       startBias: -0.2500

>> figure()
>> plot(SimData.ProbMat{5,1,12}(1,:))
>> hold on;
>> plot(SimData.ProbMat{5,1,12}(2,:),'r')
>> figure();
>> plot(SimData.ProbMat{5,1,7}(1,:))
>> hold on; plot(SimData.ProbMat{5,1,7}(2,:),'r')
>> figure();
>> plot(SimData.ProbMat{5,7,7}(1,:))
>> hold on; plot(SimData.ProbMat{5,7,7}(1,:),'r')
>> plot(SimData.ProbMat{5,7,7}(1,:))
>> hold on; plot(SimData.ProbMat{5,7,7}(2,:),'r')
>> figure
>> plot(SimData.ProbMat{5,7,7}(1,:))
>> hold on; plot(SimData.ProbMat{5,7,7}(2,:),'r')
>> figure
>> plot(SimData.ProbMat{5,1,7}(1,:))
>> hold on; plot(SimData.ProbMat{5,1,7}(2,:),'r')
>> figure;
>> plot(SimData.ProbMat{13,1,7}(1,:))
Index exceeds matrix dimensions.
 
>> plot(SimData.ProbMat{12,1,7}(1,:))
>> hold on;
>> plot(SimData.ProbMat{12,1,7}(2,:),'r')
>> sum(SimData.ProbMat{12,1,7}(1,1:100))

ans =

    0.4166

>> sum(SimData.ProbMat{12,1,7}(2,1:100))

ans =

    0.4176

>> load('/Users/djw/Downloads/Sim_0.092400.mat')
>> sum(SimData.ProbMat{12,1,7}(1,1:100))

ans =

    0.0117

>> sum(SimData.ProbMat{12,1,7}(2,1:100))

ans =

    0.9855