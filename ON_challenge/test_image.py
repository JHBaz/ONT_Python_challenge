#!/usr/bin/env python
# coding: utf-8

import unittest 
from acquire_image import binaryImage

class TestbinaryImage(unittest.TestCase):
    #unittests should be stateless between runs
    #given different input can elicit same output due to thresholds, so no assertFalse used
    def test_acquire_array(self):
        bindata = binaryImage()
        fileName = '1'
        self.assertEqual(bindata.convert_to_array(fileName).all(), bindata.convert_to_array(fileName).all(), 'reshaped array should be equal')

    def test_acquire_image(self):
        bindata = binaryImage()
        fileName = '1'
        self.assertEqual(bindata.bin_to_Image(fileName), bindata.bin_to_Image(fileName), 'img should be equal')
  
    #def test_cartesian_coordinates(self):
     #   self.assertEqual(binaryImage.get_contiguous_cartesian(),) #split function again? 
      #  pass


if __name__ == '__main__':
    unittest.main()

