from collections import defaultdict

from decomposition.subroutines.commons import get_interval
from subroutines.subroutine import subroutine
from utilities.time_measure import ExecutionTime
from utilities.print_console import print_end_algorithm


def maximal(temporal_graph, print_file):
    # measures
    number_of_maximal_cores = 0
    processed_nodes = 0

    # start of the algorithm
    execution_time = ExecutionTime()

    # structures for the maximal cores
    j_maximal_index = [0 for _ in temporal_graph.timestamps_iterator]  # end of interval, maximum k

    # for each timestamp i
    for i in temporal_graph.timestamps_iterator:
        # edges intersection and differences
        intersection = set(temporal_graph.edge_sets[i])
        differences = []

        # while the interval exists
        j = i + 1
        while j < temporal_graph.number_of_timestamps:
            # compute the new intersection
            temp_intersection = intersection & set(temporal_graph.edge_sets[j])

            # break if it is empty
            if len(temp_intersection) == 0:
                break

            # update the structures
            differences.append(tuple(intersection - temp_intersection))
            intersection = temp_intersection
            j += 1
        differences.append(tuple(intersection))

        # adjacency list and nodes divided by degree
        adjacency_list = defaultdict(list)
        nodes_by_degree = [[]]

        # minimum and maximal indexes
        minimum_index = 1
        maximal_index = 0

        # for every interval starting from timestamp i
        j -= 1
        while j >= i:
            # get the [i, j] interval
            interval = get_interval(i, j)

            # add the edges
            for edge in differences[j - i]:
                adjacency_list[edge[0]].append(edge[1])
                adjacency_list[edge[1]].append(edge[0])
                try:
                    nodes_by_degree[len(adjacency_list[edge[0]])].append(edge[0])
                except IndexError:
                    nodes_by_degree.append([edge[0]])
                try:
                    nodes_by_degree[len(adjacency_list[edge[1]])].append(edge[1])
                except IndexError:
                    nodes_by_degree.append([edge[1]])

            # compute the core decomposition for [i, j]
            if len(nodes_by_degree) > minimum_index and len(nodes_by_degree[minimum_index]) > minimum_index:
                processed_nodes += len(nodes_by_degree[minimum_index])
                subroutine_result = subroutine(adjacency_list, set(nodes_by_degree[minimum_index]))
                new_maximal_index = subroutine_result[0]
                new_maximal_core = subroutine_result[1]

                # add the new maximal core to the solution
                if new_maximal_index > maximal_index:
                    maximal_index = new_maximal_index
                    if new_maximal_index > j_maximal_index[j]:
                        minimum_index = new_maximal_index + 1
                        number_of_maximal_cores += 1
                        j_maximal_index[j] = new_maximal_index
                        if print_file is not None:
                            print_file.print_core(interval, new_maximal_index, new_maximal_core)

            # decrement j
            j -= 1

    # end of the algorithm
    execution_time.end_algorithm()

    # print algorithm results
    print_end_algorithm(execution_time.execution_time_seconds, number_of_maximal_cores, processed_nodes)
