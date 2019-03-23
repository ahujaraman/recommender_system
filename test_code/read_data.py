# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:56:30 2019

@author: raman
"""



import pandas as pd
import numpy as np
import itertools


movie = pd.read_csv('D:/ASU/SWM_NOTES/Project/ml-1m/ml-1m/movies.dat', sep='::', skiprows=1)
print(movie)