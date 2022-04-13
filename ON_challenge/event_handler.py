#!/usr/bin/env python
# coding: utf-8

from acquire_image import binaryImage
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from pathlib import Path


#code reusability
bindata = binaryImage()
#not in function as called every time file created ---> doesnt reset state of the object
#use to compare successive files?
def on_created_get_File(event):
    source_path = event.src_path
    fileNumber = Path(source_path).stem
    #if file contnents = previous bindata:
        #delete file 
        #os.remove()
    #else:

    #Concurrency...?
    bindata.bin_to_Image(fileNumber)
    bindata.get_contiguous_cartesian(fileNumber)
    
if __name__ == "__main__":
    #if something crashed, this moves to except
    my_event_handler = PatternMatchingEventHandler(patterns=['*.bin'], ignore_patterns=None, ignore_directories=False, case_sensitive=True)
    my_event_handler.on_created = on_created_get_File
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path='./data', recursive=True)
    my_observer.start() # creates a new thread
    
    while True:
        time.sleep(1) #keeps main thread running 
