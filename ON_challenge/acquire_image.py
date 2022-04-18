#!/usr/bin/env python
# coding: utf-8

import numpy as np
from PIL import Image
import os
import filecmp

class binaryImage:
    def __init__(self):
        self.datadir = 'data/'
        self.xydir = 'xy_contiguous/'
        self.previous_fileName = None

    def convert_to_array(self, binaryData):
        # This function converts the binary file into a 130 x 316 np array. 
        data = np.fromfile(self.datadir + binaryData + '.bin', dtype='uint8', count=-1, sep='', offset=0)
        newdata = []
        for i in data: # input should always be fixed (316 x 130 = 41080 unint8)
            if i <= 120:
                newdata.append(255)
            else:
                newdata.append(0)
        dataArray = np.array(newdata)

        reshaped_data = dataArray.reshape(130, 316)
        reshaped_data = reshaped_data.astype(np.uint8)

        return reshaped_data

    def bin_to_Image(self, binaryData):
        # Function that creates a .png image of the .bin file
        if os.path.exists(self.datadir + binaryData + '.bin') == False: # checks if file exists
            return

        # Error handling for case where no previously set fileName
        if (self.previous_fileName == None):
            self.previous_fileName = binaryData
        
        # calls function to check if file contents are the same.
        if (self.previous_fileName != binaryData):
            if(self.is_file_contents_same(binaryData)):
                # delete the successive file from Data dir
                os.remove(self.datadir + binaryData + '.bin')
                return

        reshaped_data = self.convert_to_array(binaryData)
        img = Image.fromarray(reshaped_data)
        img.save('Images/' + str(binaryData) + '.png')
        self.previous_fileName = binaryData
        return img

    def get_contiguous_cartesian(self, binaryData):
        # Function that gets the coordinates of contiguous white (255) regions of the np array
        if os.path.exists(self.datadir + binaryData + '.bin') == False: # checks if the binary file exists
            return
        if os.path.exists(self.xydir + binaryData + '.txt') == True: # checks if .txt file exists already, if true update this 
            os.remove(self.xydir + binaryData + '.txt')

        reshaped_data = self.convert_to_array(binaryData)
        whitepixels = np.argwhere(reshaped_data == 255)

        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        xy_cordinates = []
        for whitepixel in whitepixels:
            for direction in directions: 
                coordinate = np.add(whitepixel, direction)
                coordinate = list(coordinate)
                if coordinate[0] > 129 or coordinate[0] < 0:
                    continue
                if coordinate[1] > 315 or coordinate[1] < 0:
                    continue
                if reshaped_data[coordinate[0]][coordinate[1]] == 255:
                    whitepixel[0],whitepixel[1] = whitepixel[1],whitepixel[0] #switches yx --> xy

                    #saves xy co ordinates to .txt file, with name of the bin file as the name of the text file
                    with open(self.xydir+ str(binaryData) + '.txt',"a") as file:
                        file.write(str(whitepixel)+ '\n')
                        file.close()
                    np.append(xy_cordinates, whitepixel)

                    break
        return xy_cordinates
        
    def is_file_contents_same(self, binaryData):
        # function that compares file contents 
        prevFile = self.datadir + self.previous_fileName + '.bin'
        currentFile = self.datadir + binaryData + '.bin'
        return filecmp.cmp(prevFile, currentFile, shallow=False)


        







        
