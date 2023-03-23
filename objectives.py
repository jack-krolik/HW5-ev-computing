import pandas as pd
import csv
import numpy as np
from variables import TaVariables

def overallocation(solution, **kwargs):
    max_assigned = TaVariables.max_assigned
    print(type(max_assigned))
    overallocated_lst = [sum(lst) - max_assignment for lst, max_assignment in zip(solution.tolist(), max_assigned)
                         if sum(lst) > max_assignment]

    return sum(overallocated_lst)


def conflicts(solution, **kwargs):

    times = TaVariables.times
    conflict_combs = np.where(solution == 1, times, 0).tolist()

    conflict_list = [[_ for _ in lst if _ != 0] for lst in conflict_combs]
    conflict_set = [set([_ for _ in lst if _ != 0]) for lst in conflict_list]

    num_conflicts = [1 for c_lst, c_set in zip(conflict_list, conflict_set) if len(c_lst) != len(c_set)]

    return sum(num_conflicts)


def undersupport(solution, **kwargs):

    minimum_support = TaVariables.minimum_support
    undersupport_lst = [min - sum(lst) for lst, min in zip(solution.T.tolist(), minimum_support) if sum(lst) < min]

    return sum(undersupport_lst)


def unwilling(solution, **kwargs):

    prefs = TaVariables.prefs
    unwilling_lst = np.where((solution == 1) & (prefs == 'U'), 1, 0).tolist()

    unwilling_count = [sum(lst) for lst in unwilling_lst]

    return sum(unwilling_count)


def unpreferred(solution, **kwargs):

    prefs = TaVariables.prefs
    willing_lst = np.where((solution == 1) & (prefs == 'W'), 1, 0).tolist()

    willing_count = [sum(lst) for lst in willing_lst]

    return sum(willing_count)


