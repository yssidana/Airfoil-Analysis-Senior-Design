#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:33:28 2020

@author: Yash
"""

import numpy as np
import matplotlib.pyplot as plt
import pyxfoil
from statistics import mode
import math
import mses


#airfoils = range(1,34)
#airfoils = list(map(str,airfoils))
datadir = "Data1"
c = 1
airfoils = '1'
tline = 3
geoms = {}
for f in airfoils:
    geoms[f] = {}
    geoms[f]['x'],geoms[f]['z'] = c * np.loadtxt('{}/{}/{}.dat'.format(datadir,f,f),unpack=True,skiprows=tline)

x_mses_new, y_mses_new = mses.MsesMerge(geoms['1']['x'][0:int(len(geoms['1']['x'])/2)],geoms['1']['x'][int(len(geoms['1']['x'])/2):],geoms['1']['z'][int(len(geoms['1']['z'])/2):],geoms['1']['z'][0:int(len(geoms['1']['z'])/2)])

data = []