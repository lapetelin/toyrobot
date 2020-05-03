# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:45:11 2020

@author: Petelin
"""

"""
def test_sum():
    assert sum([1,3,2]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    
    print('everything passed')
"""

# # unittest method
import unittest
from toyrobot import Robot

# class TestSum(unittest.TestCase): # inherits from TestCase class
    
#     def test_sum (self):
#         self.assertEqual(sum([1,2,3]), 6, "Should be 6")
    
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1,2,2)), 6, 'Should be 6')
        
# if __name__ == '__main__':
#     unittest.main()


# # nose
# import nose2

# import pytest
# # Using pytest
# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"


class TestPlacement(unittest.TestCase): # inherits from TestCase class
    
    def test_position(self):
        steve = Robot()
        steve.place(0,0)
        self.assertEqual(steve.position, (0,0), 'robot is in the wrong position')
    
    def test_left(self):
        steve = Robot()
        steve.place(0,0,'S')
        steve.left()
        
        self.assertEqual(steve.facing, 'E', 'robot should face east from south')
        
if __name__ == '__main__':
    unittest.main()
