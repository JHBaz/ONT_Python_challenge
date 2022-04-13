#!/usr/bin/env python
# coding: utf-8
from distutils import text_file
from fileinput import filename
import numpy as np
from numpy import savetxt
from PIL import Image
import pandas as pd
import os
import filecmp
#import networkx as nx 
from scipy import sparse
import re 

class binaryImage:
    def __init__(self):
        #magic numbers
        self.datadir = 'data/'
        self.previous_fileName = None

    def convert_to_array(self, binaryData):
        data = np.fromfile(self.datadir + binaryData + '.bin', dtype='uint8', count=-1, sep='', offset=0)
        newdata = []
        for i in data:
            if i <= 120:
                newdata.append(255)
            else:
                newdata.append(0)
        dataArray = np.array(newdata)

        reshaped_data = dataArray.reshape(130, 316)
        reshaped_data = reshaped_data.astype(np.uint8)

        return reshaped_data

    def bin_to_Image(self, binaryData):
        if os.path.exists(self.datadir + binaryData + '.bin') == False:
            return
        #check file names equal or not. will skip next if statement
        #Error handling for case where no previously set fileName
        if (self.previous_fileName == None):
            self.previous_fileName = binaryData

        if (self.previous_fileName != binaryData):
            if(self.is_file_contents_same(binaryData)):
                #delete the successive file from Data dir
                os.remove(self.datadir + binaryData + '.bin')
                return

        reshaped_data = self.convert_to_array(binaryData)
        img = Image.fromarray(reshaped_data)
        img.save('Images/' + str(binaryData) + '.png')
        self.previous_fileName = binaryData
        return img
    
    def is_file_contents_same(self, binaryData):
        prevFile = self.datadir + self.previous_fileName + '.bin'
        currentFile = self.datadir + binaryData + '.bin'
        return filecmp.cmp(prevFile, currentFile, shallow=False)

    def get_contiguous_cartesian(self, binaryData):
        if os.path.exists(self.datadir + binaryData + '.bin') == False:
            return
        reshaped_data = self.convert_to_array(binaryData)
        sdata = sparse.csr_matrix(reshaped_data)
        sdata.maxprint = sdata.count_nonzero()
        with open('xy/' + str(binaryData) + '.txt',"w") as file:
            file.write(str(sdata))
            file.close()
        return str(sdata)