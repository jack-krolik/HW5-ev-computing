import pandas as pd
import csv
import numpy as np
from variables import TaVariables


def overallocation(solution):
    """ finds the number of overallocations in a solution
    input: solution (np.array): the solution array
    """
    # access max assigned
    max_assigned = TaVariables.max_assigned

    # count number of overallocations
    overallocated_lst = [sum(lst) - max_assignment for lst, max_assignment in zip(solution.tolist(), max_assigned)
                         if sum(lst) > max_assignment]

    return sum(overallocated_lst)


def conflicts(solution):
    """ finds the number of conflicts in a solution
    input: solution (np.array): the solution array
    """
    # access times
    times = TaVariables.times

    # find and count number of conflicts
    conflict_combs = np.where(solution == 1, times, 0).tolist()
    conflict_list = [[_ for _ in lst if _ != 0] for lst in conflict_combs]
    conflict_set = [set([_ for _ in lst if _ != 0]) for lst in conflict_list]
    num_conflicts = [1 for c_lst, c_set in zip(conflict_list, conflict_set) if len(c_lst) != len(c_set)]

    return sum(num_conflicts)


def undersupport(solution):
    """ finds the number of undersupport instances in a solution
    input: solution (np.array): the solution array
    """
    # access minimum support
    minimum_support = TaVariables.minimum_support

    # count number of undersupport instances
    undersupport_lst = [min - sum(lst) for lst, min in zip(solution.T.tolist(), minimum_support) if sum(lst) < min]

    return sum(undersupport_lst)


def unwilling(solution):
    """ finds the number of unwilling instances in a solution
    input: solution (np.array): the solution array
    """
    # access preferences
    prefs = TaVariables.prefs

    # count number of unwilling instances
    unwilling_lst = np.where((solution == 1) & (prefs == 'U'), 1, 0).tolist()
    unwilling_count = [sum(lst) for lst in unwilling_lst]

    return sum(unwilling_count)


def unpreferred(solution):
    """ finds the number of unpreferred instances in a solution
    input: solution (np.array): the solution array
    """
    # access preferences
    prefs = TaVariables.prefs

    # count number of unpreferred instances
    willing_lst = np.where((solution == 1) & (prefs == 'W'), 1, 0).tolist()
    willing_count = [sum(lst) for lst in willing_lst]

    return sum(willing_count)


