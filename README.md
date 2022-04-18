# ONT_Python_challenge
 Image handling project

ON_challenge directory contains 3 python files which respond to '.bin' files added to data directory (which is also in ON_challenge dir). 

# How to run the program:
from terminal run 'event_handler.py' 

add .bin files to data directory. 

--> X.png will be added in the Images dir. 

--> Contiguous regions of white pixels will be saved in a .txt file in format [y x]

# How to run tests
from terminal run 'test_image.py' 


# TODO / further thoughts
- Is volTRAX multi CPU? How much memory on device, is there a better way to compress these files? 
- Must be executed on device for portability? Connect to network when docked? (transfer of files) 
- Assess time complexity of coordinate function, O(n * m), as input is fixed => O(1)?
- is there further testing could do?
- How many .bin file can handle before stack overflow? Create auto array generator to test this?
