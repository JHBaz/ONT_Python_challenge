#!/usr/bin/env python
# coding: utf-8
from operator import index
import numpy as np
from PIL import Image
import pandas as pd

#magic numbers
class binaryImage:
    def __init__(self):
        self.datadir = 'data/'

    def convert_to_array(self, binaryData):
        data = np.fromfile(self.datadir + binaryData + '.bin', dtype='uint8', count=-1, sep='', offset=0)
        newdata = []
        for i in data:
            if (i <= 120):
                newdata.append(255)
            else:
                newdata.append(0)
        dataArray = np.array(newdata)

        reshaped_data = dataArray.reshape(130, 316)
        reshaped_data = reshaped_data.astype(np.uint8)

        return reshaped_data

    def bin_to_Image(self, binaryData):
        reshaped_data = self.convert_to_array(binaryData)
        img = Image.fromarray(reshaped_data)
        img.save('Images/' + str(binaryData) + '.png')
        return img
        #save some kind of reference for comparison?
    
    def get_contiguous_cartesian(self, binaryData):
        reshaped_data = self.convert_to_array(binaryData)
        df = pd.DataFrame(reshaped_data)
        print(df)
        #contig_xy = []?
        #for i in df:
            #if (i = 255):
                





            #np.where(condition, X, Y)
            #Contiguous_xy = np.where(i <= 120, , None )
        #detect contiguous regions of white pixels
        #output to .txt file 
        #plot using seaborn
        #return co ordinates? 
           

    #def contiguous_cartesian_to_text(self):
        #return coordinates in text file ?
        #pass
        