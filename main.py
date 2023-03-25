from evo import Evo
from agents import *
from objectives import *


def main():
    # import test files and initialize tracking dataframe
    test1 = pd.read_csv('test1.csv', header=None).to_numpy()
    test2 = pd.read_csv('test2.csv', header=None).to_numpy()
    test3 = pd.read_csv('test3.csv', header=None).to_numpy()
    test_df = pd.DataFrame([['Overallocation'], ['Conflicts'], ['Undersupport'], ['Unwilling'], ['Unpreferred']],
                           columns=['Objectives'])

    # run all objectives on each of the three tests and track the results
    for idx, test in enumerate([test1, test2, test3]):
        test_df['Test' + str(idx + 1)] = [overallocation(test), conflicts(test),
                                          undersupport(test), unwilling(test),
                                          unpreferred(test)]
    # output to csv
    test_df.to_csv('objective_tests.csv')

    # Create framework
    E = Evo()

    # Register some objectives
    E.add_fitness_criteria("overallocation", overallocation)
    E.add_fitness_criteria("conflicts", conflicts)
    E.add_fitness_criteria("undersupport", undersupport)
    E.add_fitness_criteria("unwilling", unwilling)
    E.add_fitness_criteria("unpreferred", unpreferred)

    # Register some agents
    E.add_agent("agent_overallocation", agent_overallocation, k=1)
    E.add_agent("agent_undersupport", agent_undersupport, k=1)
    E.add_agent("agent_unwilling", agent_unwilling, k=1)
    E.add_agent("agent_unpreferred", agent_unpreferred, k=1)

    # Seed the population with an initial random solution
    test1, test2, test3 = pd.read_csv('test1.csv', header=None).to_numpy(), \
        pd.read_csv('test2.csv', header=None).to_numpy(), pd.read_csv('test3.csv', header=None).to_numpy()
    # N = 50
    # L = [rnd.randrange(1, 99) for _ in range(N)]
    E.add_solution(test1)
    E.add_solution(test2)
    E.add_solution(test3)
    # print(E)

    # Run the evolver
    E.evolve(10000, 100, 100)

    # Print final results
    print(E)

    # convert the results to a dataframe
    obj_df = pd.DataFrame(
        columns=["Groupname", "Solution", "Overallocation", "Conflicts", "Undersupport", "Unwilling", "Unpreferred"])
    solution_lst = []
    overallocate_list = []
    conflict_list = []
    undersupport_list = []
    unwilling_list = []
    unpreferred_list = []
    for key, value in zip(list(E.pop.keys()), list(E.pop.values())):
        solution_lst.append(value)
        overallocate_list.append(key[0][1])
        conflict_list.append(key[1][1])
        undersupport_list.append(key[2][1])
        unwilling_list.append(key[3][1])
        unpreferred_list.append(key[4][1])

    # fill and output dataframe
    obj_df['Solution'] = solution_lst
    obj_df['Overallocation'] = overallocate_list
    obj_df['Conflicts'] = conflict_list
    obj_df['Undersupport'] = undersupport_list
    obj_df['Unwilling'] = unwilling_list
    obj_df['Unpreferred'] = unpreferred_list
    len_df = len(obj_df)
    obj_df['Groupname'] = ['bej'] * len_df
    obj_df.to_csv('summary_table.csv')


if __name__ == '__main__':
    main()
