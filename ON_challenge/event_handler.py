#!/usr/bin/env python
# coding: utf-8

from acquire_image import binaryImage
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from pathlib import Path
from threading import Thread

bindata = binaryImage()
# not in function as called every time file created ---> doesnt reset state of the object

def on_created_get_File(event):
    # Function that gets the fileNumber as arguments for the methods in Image class
    source_path = event.src_path
    fileNumber = Path(source_path).stem
    
    bindata.bin_to_Image(fileNumber) # Calls to save image
    
    # Seperate thread for contiguous co ordinate finding.
    thread= Thread(target=bindata.get_contiguous_coordinates(fileNumber))
    thread.daemon= True
    thread.start()

if __name__ == "__main__":
    # if called as main program:
    my_event_handler = PatternMatchingEventHandler(patterns=['*.bin'], ignore_patterns=None, ignore_directories=False, case_sensitive=True)
    my_event_handler.on_created = on_created_get_File
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path='./data', recursive=True)
    my_observer.start() # creates a new thread
    
    while True:
        time.sleep(1)


