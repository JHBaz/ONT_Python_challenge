#!/usr/bin/env python
# coding: utf-8

import unittest 
from acquire_image import binaryImage

class TestbinaryImage(unittest.TestCase):
    
    #given different input can elicit same output due to thresholds, so no assertFalse used
    def test_convert_to_array(self):

        bindata = binaryImage()
        fileName = '1'
        self.assertEqual(bindata.convert_to_array(fileName).all(), bindata.convert_to_array(fileName).all(), 'reshaped array should be equal')

    def test_bin_to_image(self):
        bindata = binaryImage()
        fileName = '1'
        self.assertEqual(bindata.bin_to_Image(fileName), bindata.bin_to_Image(fileName), 'img should be equal')
  
    def test_contiguous_coordinates(self):
        bindata = binaryImage()
        fileName = '1'
        self.assertEqual(bindata.get_contiguous_coordinates(fileName), bindata.get_contiguous_coordinates(fileName), 'xy coordinates should be equal')
        
if __name__ == '__main__':
    unittest.main()

