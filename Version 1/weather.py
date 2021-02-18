import random
import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
import os
import math
import numpy as np
import time

# Change direct to program's folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Reads the CSV
df = pandas.read_csv("weather.csv")
# Main Features to look for
features = ["Date.Month", "Date.Week of", "Data.Temperature.Avg Temp", "Data.Temperature.Max Temp", "Data.Temperature.Min Temp", "Data.Wind.Direction", "Data.Wind.Speed"]
# Set features to find
X = df[features]
# Get whether or not to precipitate
y = df["isRain"]
# Create decision tree
dtree = DecisionTreeClassifier().fit(X, y)


class predictWeather(object):
    def __init__(self, m, d, at, mat, mit, wd, ws):
        self.m = m
        self.d = d
        self.at = at
        self.mat = mat
        self.mit = mit
        self.wd = wd
        self.ws = ws

    def run(self):
        return dtree.predict([[self.m, self.d, self.at, self.mat, self.mit, self.wd, self.ws]])
