import pandas as pd
import random as rnd
import numpy as np
from objectives import overallocation, undersupport, unwilling
from variables import TaVariables


def agent_overallocation(solutions, **kwargs):
    """ fixes an instance of an overallocation
    input: solutions (list of np.array): the list of solutions
    """
    # access the first solution in the list and shape it
    solution = solutions[0]
    solution = np.array(solution).reshape(43, -1)

    # access max assigned values
    max_assigned = TaVariables.max_assigned

    # find rows with overallocations
    maxed_tas = [idx for idx, (ta_row, max_assignment) in
                 enumerate(zip(solution.tolist(), max_assigned)) if sum(ta_row) > max_assignment]

    # select a random section and deallocate it
    random_sec = [rnd.randint(0, solution.shape[1] - 1) for _ in maxed_tas]
    solution[maxed_tas, random_sec] = 0

    return solution


def agent_undersupport(solutions):
    """ fixes an instance of an undersupport
    input: solutions (list of np.array): the list of solutions
    """
    # access the first solution in the list and shape it
    solution = solutions[0]
    solution = np.array(solution).reshape(43, -1)

    # access minimum support values
    minimum_support = TaVariables.minimum_support

    # find sections that are undersupported
    sections_undersupported = [idx for idx, (sec_row, sup) in enumerate(zip(solution.T.tolist(), minimum_support))
                               if sum(sec_row) < sup]

    # select a random section and assign a TA to work on it
    random_tas = [rnd.randint(0, solution.shape[0] - 1) for _ in sections_undersupported]
    solution[random_tas, sections_undersupported] = 1

    return solution


def agent_unwilling(solutions, **kwargs):
    """ fixes an instance where a TA is assigned an unwilling section
    input: solutions (list of np.array): the list of solutions
    """
    # access the first solution in the list and shape it
    solution = solutions[0]
    solution = np.array(solution).reshape(43, -1)

    # access preferences
    prefs = TaVariables.prefs

    # find sections with unwilling TAs
    conflict_index = [
        [idx for idx, (pref, assignment) in enumerate(zip(pref_row, ta_row)) if (pref == 'U') and (assignment == 1)]
        for pref_row, ta_row in zip(prefs, solution)]
    ta_index = [i for i, lst in enumerate(conflict_index) if len(lst) > 0]

    # select a random section and fix the unwilling error
    random_sec = [np.random.choice(conflict_index[i]) for i in ta_index]
    solution[ta_index, random_sec] = 0

    return solution


def agent_unpreferred(solutions, **kwargs):
    """ fixes an instance where a TA is assigned an unpreferred section
    input: solutions (list of np.array): the list of solutions
    """
    # access the first solution in the list and shape it
    solution = solutions[0]
    solution = np.array(solution).reshape(43, -1)

    # access preferences
    prefs = TaVariables.prefs

    # find all unpreferred sections assigned to TAs
    conflict_index = [
        [idx for idx, (pref, assignment) in enumerate(zip(pref_row, ta_row)) if (pref == 'W') and (assignment == 1)]
        for pref_row, ta_row in zip(prefs, solution)]
    ta_index = [i for i, lst in enumerate(conflict_index) if len(lst) > 0]

    # select a random section and solve the unpreferred issue
    random_sec = [np.random.choice(conflict_index[i]) for i in ta_index]
    solution[ta_index, random_sec] = 0

    return solution
