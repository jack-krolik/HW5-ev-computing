import pandas as pd
import random as rnd
import numpy as np


class TaVariables():
    """
    Class for exporting ta attributes
    """

    # dataframe for ta csv and sections csv
    ta = pd.read_csv('tas.csv')
    sections = pd.read_csv('sections.csv')

    # max number of sections ta can be assigned to as a list
    max_assigned = ta['max_assigned'].values

    # weekday and time of each section as a numpy array
    times = sections['daytime'].to_numpy()

    # minimum # of tas needed for each section as a list
    minimum_support = sections['min_ta'].values

    # the preferences of each ta as a list
    prefs = ta.loc[:, '0':].values

