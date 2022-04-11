# ONT_Python_challenge
 Image handling project

ON_challenge directory contains 3 python files which respond to '.bin' files added to data directory (which is also in ON_challenge dir). 

#How to run the program:
from terminal run 'python3 event_handler.py' or however python run on native machine. 

add .bin files to data directory. 

X.png will be added in the Images dir. 

#TODO
- update event handler to only call '.bin' files 
- implement functionality in test class, using unittest
- Create a class which randomly generates uniform sized binary images/ arrays to test scalability?

Pseudo code:
- contiguous functionality: thinking this best by creating a cross hair that is looped through the reshaped array. Then use np.where() function to get co ordinates... or use pd df to use columns and indicies?
- Further tests for contiguous function: e.g compare outputs, see if the same? 
- How to compare succesive files at efficiently w/o analysing them: .cmp to compare files memory size, then if equal, compre binary data or array for exact matches. Delete the latter one... Need to somehow remember the previous files data... to it at the class level??
