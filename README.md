# ONT_Python_challenge
 Image handling project

ON_challenge directory contains 3 python files which respond to '.bin' files added to data directory (which is also in ON_challenge dir). 

# How to run the program:
From terminal run 'event_handler.py' 

Add .bin files to data directory. 

--> X.png will be added in the Images dir 

--> X.txt of contiguous regions will be added to xy_contiguous dir (format [x y] of the np 316 x 130 array) 

# How to run tests
From terminal run 'test_image.py'

# Further thoughts 
- Assess time complexity of coordinate function in 'acquire_image.py', O(n * m), but as input is fixed => O(1)?
- How many .bin files can handle before stack overflow?
