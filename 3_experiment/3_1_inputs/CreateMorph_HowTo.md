# Steps to Create Morph

### 1. Select Images

a. Find the two imags you are interested in morphing between.

* Width should be 600
* Height can be whatever you like, I have used 422. In order to see the full image in the processing window make sure the height is twice the height of your image (`size(1200, 844, P2D);`)

b. Put these in `FaceMorph/data`.

### 2. Update Code

a. Update the images:

```// Load the images
  a = loadImage("CFD-WF-003-003-N_small.jpg");
  b = loadImage("CFD-WF-026-002-N_small.jpg");
```

b. Specify the folder they will be saved to (below it is `attractive_unattractive`) as well as the root of the file name:

```save("attractive_unattractive/face_f_au_1_" + nf(img_count,3) + ".jpg");```

c. Comment out this line in **setup**:

 `morph.loadPoints();`, 

This allows you to specify the match points in the two images.

### 3. Set and Save Image Match Points

a. Run `FaceMorph.pde`. Just wait until the automorph finishes (takes a few seconds), then you will be shown a 50/50 morph

b. select matching points. Be accurate as this will determine how well your morph works. When done, press `s` to save the points.

### 4. Update Code

a. Uncomment  `morph.loadPoints();` in **setup**.

### 5. Run

a.  Run `FaceMorph.pde`.

This will save 101 morphed images (from 0% to 100% morph) into the folder you have specified.