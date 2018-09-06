from collections import deque

from subroutines.commons import *
from subroutines.subroutine import subroutine
from utilities.time_measure import ExecutionTime
from utilities.print_console import print_end_algorithm


def decomposition(temporal_graph, print_file):
    # measures
    number_of_cores = [0]
    processed_nodes = 0

    # start of the algorithm
    execution_time = ExecutionTime()

    # cores
    cores = {}

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
            # store the results of the subroutine to cores
            processed_nodes += len(nodes)
            cores[interval] = subroutine(temporal_graph, nodes, interval, print_file=print_file, number_of_cores=number_of_cores)[0]

            # if there are cores in the interval
            if len(cores[interval]) > 0:
                # add its descendant intervals to the queue
                add_descendants_to_queue(interval, temporal_graph, intervals_queue, ancestors, descendants_count)

    # end of the algorithm
    execution_time.end_algorithm()

    # print algorithm's results
    print_end_algorithm(execution_time.execution_time_seconds, number_of_cores[0], processed_nodes)
