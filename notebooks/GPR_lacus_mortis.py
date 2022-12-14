import math
import numpy as np
import pandas as pd
import csv
import keras
import tensorflow
from keras import layers
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.gaussian_process import GaussianProcessRegressor
import scipy.optimize
from sklearn.gaussian_process.kernels import Matern

import GPy

import os
import re
import datetime

os.chdir("/u/paige/asinha/T-BOL/")

# extract Lacus Mortis temperature profiles (.xyz files)
files = ['lacus_mortis-tb-' + str(format(num, '03')) + '.xyz' for num in range(1,241)]

"""
# extract all .xyz files in raw data query folder
files = []

for f in os.listdir():
    if re.search('.xyz', f):
        results += [each for each in os.listdir() if each.endswith('.xyz')]
"""

def extract(file):
    """ function to extract lat-lon coordinates (X, Y) and temperature value (Z) from the .xyz files """
    X, Y, Z = [], [], []
    f = open(file, 'r')
    for row, line in enumerate(f):
        values = line.strip().split('\t')
        X.append(float(values[0]))
        Y.append(float(values[1]))
        Z.append(float(values[2]))
    data = [X, Y, Z]
    return data

data = [extract(fileX) for fileX in files]

X = [0.1*jj - 0.05 for jj in range(1,len(data)+1)]

x_fit = np.linspace(0, 24, 121)
x_fit = x_fit[0:-1] # removed hour 24 = hour 0 (added later with padding)
x_raw, x_gpr = [], []

""" loop to interplote the raw data (x_raw) using GPR and to store the interpolated data (x_train) """
# assumes each file has the same number of pixels
for ii in range(len(data[0][0])):
    Y = [data[jj][2][ii] for jj in range(0, len(data))]
    x_raw.append(np.array(Y))
    mask = [index for index, val in enumerate(Y) if not np.isnan(val)]
    x, y = [], []
    for m in mask:
        x.append(X[m])
        y.append(Y[m])
    kernel = GPy.kern.Matern32(1, lengthscale = 6.0, variance = 100.0)
    gpr = GPy.models.GPRegression(np.array(x).reshape(-1,1), np.array(y).reshape(-1,1), kernel)
    gpr.constrain_positive()
    gpr.optimize()
    y_pred = gpr.predict(x_fit.reshape(-1,1))
    x_gpr.append(np.transpose(y_pred[0]))
    x_gpr[ii] = x_gpr[ii][0]

x_gpr_dump = np.asarray(x_gpr)

""" TO DO: SAVE WITH RUN-TIME DATETIME FOR DATA VERSIONING """
os.chdir("/u/paige/asinha/projectdir/")
np.savetxt('GPR-lacus-mortis.csv', x_gpr_dump, fmt = '%1.3f')
