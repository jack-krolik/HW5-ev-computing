import pandas as pd
import random as rnd
import numpy as np
from objectives import overallocation, undersupport, unwilling

def agent_overallocation(solution, max_assigned_lst):

    maxed_tas = [idx for idx, (ta_row, max_assigned) in
                               enumerate(zip(solution.tolist(), max_assigned_lst)) if sum(ta_row) > max_assigned]

    random_sec = [rnd.randint(0, solution.shape[1] - 1) for _ in maxed_tas]

    solution[maxed_tas, random_sec] = 0

    return solution



def agent_conflicts(solution):
    pass

def agent_undersupport(solution, min_sup):

    sections_undersupported = [idx for idx, (sec_row, sup) in enumerate(zip(solution.T.tolist(), min_sup))
                               if sum(sec_row) < sup]
    random_tas = [rnd.randint(0, solution.shape[0] - 1) for _ in sections_undersupported]

    solution[random_tas, sections_undersupported] = 1


    return solution


def agent_unwilling(solution, prefs):
    pass







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
# print(unwilling(test1, preferences))
# print(unwilling(agent_unwilling(test1, preferences), preferences))

print(overallocation(test1, max_assign))
print(overallocation(agent_overallocation(test1, max_assign), max_assign))

# for i in range(1, 1000):
#     sol = agent_undersupport(sol, min_support)
# print(undersupport(sol, min_support))
