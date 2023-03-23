import pandas as pd
import random as rnd
import numpy as np


class TaVariables():
    ta = pd.read_csv('tas.csv')
    sections = pd.read_csv('sections.csv')
    max_assigned = ta['max_assigned'].values
    times = sections['daytime'].to_numpy()
    minimum_support = sections['min_ta'].values
    prefs = ta.loc[:, '0':].values