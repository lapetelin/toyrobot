# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:34:42 2020

@title: toyrobot.py
@author: Petelin
"""
import mypy
import unittest



class Table():
    
    def __init__(self, xsize=0, ysize=0):
        self.xmax=xsize
        self.ymax=ysize
        self.robot = None
        

class Robot():
    
    def __init__(self):
        self.position = None
        self.facing = 'None'
        
    def place(self, x=0, y=0, f='N'):
        self.position = (x,y)
        self.facing = f
    
    def left(self):
        if self.facing == 'S':
            self.facing = 'E'
        elif self.facing == 'N':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'S'
        elif self.facing == 'E':
            self.facing = 'N'
        
    def right(self):
        if self.facing == 'S':
            self.facing = 'W'
        elif self.facing == 'N':
            self.facing = 'E'
        elif self.facing == 'W':
            self.facing = 'N'
        elif self.facing == 'E':
            self.facing = 'S'
