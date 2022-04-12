#!/usr/bin/env python
# coding: utf-8

import unittest 
from acquire_image import binaryImage

class TestbinaryImage(unittest.TestCase):
    #unittests should be statless between runs --> what does this mean?
    #want to compare reshaped data or compare output files, though could be diff re shaped array, the image could be the same because of the threhold values?
    def test_acquire_image(self):
        print('Checking if output is same given same input')
        self.assertEqual(binaryImage.convert_to_array(), binaryImage.bin_to_Image())
        #what other tests could implement?
        #self.assertFalse()

    
    def test_cartesian_coordinates(self):
        self.assertEqual(binaryImage.get_contiguous_cartesian(),) #split function again? 
        pass

if __name__ == '__main__':
    unittest.main()

