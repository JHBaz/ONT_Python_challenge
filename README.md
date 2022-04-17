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


# TODO
- is volTRAX multi CPU? must be executed on device for portability? Connect to network when docked? Need to ressearch further. 
- assess time complexity of coordinate function, as input is fixed => O(n), O(1)?
- is there further testing could do?
- How many .bin file can handle before stack overflow? Create auto array generator to test this?
