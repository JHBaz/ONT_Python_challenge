#!/usr/bin/env python
# coding: utf-8
import numpy as np
from PIL import Image


#magic numbers

class binaryImage:
    def __init__(self):
        self.datadir = 'data/'

    def convert_array(self, binaryData):
        data = np.fromfile(self.datadir + binaryData + '.bin', dtype='uint8', count=-1, sep='', offset=0)
        newdata = []
        for x in data:
            if (x <= 120):
                newdata.append(255)
            else:
                newdata.append(0)
        dataArray = np.array(newdata)

        reshaped_data = dataArray.reshape(130, 316)
        reshaped_data = reshaped_data.astype(np.uint8)

        return reshaped_data

    def bin_to_Image(self, binaryData):
        reshaped_data = self.convert_array(binaryData)
        img = Image.fromarray(reshaped_data)
        img.save('Images/' + str(binaryData) + '.png')
        #save some kind of reference for comparison

   
#one = binaryImage()
#one.bin_to_Image('1')

#(rows, columns, channels) for grey 
#for i in range(len(binaryData)):
 #   for j in range(binaryData.shape[0,1,]):
  #      binaryData.

#how to get co ordinates of contigous pixels?
#slice numpy array print coordinates