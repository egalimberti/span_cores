from collections import deque

from decomposition.subroutines.commons import *
from decomposition.subroutines.subroutine import subroutine
from utilities.time_measure import ExecutionTime
from utilities.print_console import print_end_algorithm


def naive_maximal(temporal_graph, print_file):
    # start of the algorithm
    execution_time = ExecutionTime()
    processed_nodes = 0

    # cores
    cores = {}
    maximal_cores = {}

    # initialize the queue of intervals
    intervals_queue = deque()
    # initialize the dict of ancestors
    ancestors = {}
    # add each singleton interval to the queue
    for timestamp in temporal_graph.timestamps_iterator:
        intervals_queue.append(get_interval(timestamp))

    # dict counting the number of descendants in the queue
    descendants_count = {}

    # while the queue is not empty
    while len(intervals_queue) > 0:
        # remove an interval from the queue
        interval = intervals_queue.popleft()

        # get the nodes from which start the computation
        nodes = get_ancestors_intersection(interval, ancestors, cores, temporal_graph, descendants_count)

        # if nodes is not empty
        if len(nodes) > 0:
            # store the results of the subroutine to interval_cores
            processed_nodes += len(nodes)
            interval_cores = subroutine(temporal_graph, nodes, interval, in_memory=True)

            # if there are cores in the interval
            if len(interval_cores[0]) > 0:
                # store the first to cores
                cores[interval] = {1: interval_cores[0][1]}
                # add its descendant intervals to the queue
                add_descendants_to_queue(interval, temporal_graph, intervals_queue, ancestors, descendants_count)

                # add the maximal core to maximal
                maximal_cores[interval] = (interval_cores[1], interval_cores[0][interval_cores[1]])
                # delete the maximal cores of the ancestor intervals if needed
                try:
                    for ancestor_interval in ancestors[interval]:
                        if ancestor_interval in maximal_cores and maximal_cores[ancestor_interval][0] == interval_cores[1]:
                            maximal_cores.pop(ancestor_interval)
                except KeyError:
                    pass
            else:
                cores[interval] = interval_cores[0]

    # print the output file
    if print_file is not None:
        print_file.print_maximal_cores(maximal_cores)

    # end of the algorithm
    execution_time.end_algorithm()

    # print algorithm's results
    print_end_algorithm(execution_time.execution_time_seconds, len(maximal_cores), processed_nodes)
