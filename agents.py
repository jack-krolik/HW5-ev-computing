import pandas as pd
import random as rnd
import numpy as np
from objectives import overallocation, undersupport, unwilling

def agent_overallocation(solution, max_assigned):
    idx = 0
    for ta_row, max_a in zip(solution, max_assigned):

        if sum(ta_row) > max_a:

            random_int = rnd.randint(0, len(ta_row) - 1)

            while ta_row[random_int] != 1:
                random_int = rnd.randint(0, len(ta_row) - 1)

            ta_row[random_int] = 0
            solution[idx, :] = ta_row

        idx += 1

    return solution

    # while True:
    #     rnd_row_val = rnd.randint(0, solution.shape[0] - 1)
    #     rnd_col_val = rnd.randint(0, solution.shape[1] - 1)
    #
    #     if solution[rnd_row_val, rnd_col_val] == 1:
    #         solution[rnd_row_val, rnd_col_val] = 0
    #         break
    #
    # return solution

def agent_conflicts(solution):
    pass

def agent_undersupport(solution, min_sup):
    solution_temp = solution.T
    idx = 0
    for section_row, min_s in zip(solution_temp, min_sup):

        if sum(section_row) < min_s:

            random_int = rnd.randint(0, len(section_row) - 1)

            while section_row[random_int] != 0:
                random_int = rnd.randint(0, len(section_row) - 1)

            section_row[random_int] = 1
            solution_temp[idx, :] = section_row

        idx += 1

    return solution_temp.T

def agent_unwilling(solution, prefs):

    # new_sol = np.where((solution == 1) & (prefs == 'W'), 0, 1)
    idx1 = 0
    for ta_row, pref_row in zip(solution, prefs):
        idx2 = 0
        for assignment, pref in zip(ta_row, pref_row):
            if assignment == 1 and pref == 'W':
                ta_row[idx2] = 0

                idx2 += 1

        solution[idx1, :] = ta_row

        idx1 += 1





ta = pd.read_csv('tas.csv')

sections = pd.read_csv('sections.csv')

max_assign = ta['max_assigned'].values

min_support = sections['min_ta'].values

preferences = ta.loc[:, '0':].values

test1, test2, test3 = pd.read_csv('test1.csv', header=None).to_numpy(), \
    pd.read_csv('test2.csv', header=None).to_numpy(), pd.read_csv('test3.csv', header=None).to_numpy()

# print(overallocation(test1, max_assign))
# print(overallocation(agent_overallocation(test1, max_assign), max_assign))
# print(undersupport(test1, min_support))
# print(undersupport(agent_undersupport(test1, min_support), min_support))
print(unwilling(test1, preferences))
print(unwilling(agent_unwilling(test1, preferences), preferences))
