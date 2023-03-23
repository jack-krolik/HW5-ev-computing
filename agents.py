import pandas as pd
import random as rnd
import numpy as np
from objectives import overallocation, undersupport, unwilling
from variables import TaVariables

def agent_overallocation(solutions, **kwargs):
    solution = solutions[0]

    solution = np.array(solution).reshape(43, -1)

    max_assigned = TaVariables.max_assigned

    maxed_tas = [idx for idx, (ta_row, max_assignment) in
                               enumerate(zip(solution.tolist(), max_assigned)) if sum(ta_row) > max_assignment]

    random_sec = [rnd.randint(0, solution.shape[1] - 1) for _ in maxed_tas]

    solution[maxed_tas, random_sec] = 0

    return solution



def agent_conflicts(solutions):
    pass

def agent_undersupport(solutions, **kwargs):
    solution = solutions[0]
    solution = np.array(solution).reshape(43, -1)

    minimum_support = TaVariables.minimum_support
    sections_undersupported = [idx for idx, (sec_row, sup) in enumerate(zip(solution.T.tolist(), minimum_support))
                               if sum(sec_row) < sup]
    random_tas = [rnd.randint(0, solution.shape[0] - 1) for _ in sections_undersupported]

    solution[random_tas, sections_undersupported] = 1


    return solution


def agent_unwilling(solutions, **kwargs):
    solution = solutions[0]
    solution = np.array(solution).reshape(43, -1)

    prefs = TaVariables.prefs
    conflict_index = [
        [idx for idx, (pref, assignment) in enumerate(zip(pref_row, ta_row)) if (pref == 'U') and (assignment == 1)]
        for pref_row, ta_row in zip(prefs, solution)]

    ta_index = [i for i, lst in enumerate(conflict_index) if len(lst) > 0]

    random_sec = [np.random.choice(conflict_index[i]) for i in ta_index]

    solution[ta_index, random_sec] = 0

    return solution






