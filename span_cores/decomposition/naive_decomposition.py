from collections import deque

from subroutines.commons import *
from subroutines.subroutine import subroutine
from utilities.time_measure import ExecutionTime
from utilities.print_console import print_end_algorithm


def naive_decomposition(temporal_graph, print_file):
    # measures
    number_of_cores = [0]
    processed_nodes = 0

    # start of the algorithm
    execution_time = ExecutionTime()

    # cores
    cores = {}

    # initialize the queue of intervals
    intervals_queue = deque()
    # initialize the set of intervals in the queue
    intervals = set()
    # add each singleton interval to the queue
    for timestamp in temporal_graph.timestamps_iterator:
        interval = get_interval(timestamp)
        intervals_queue.append(interval)
        intervals.add(interval)

    # while the queue is not empty
    while len(intervals_queue) > 0:
        # remove an interval from the queue
        interval = intervals_queue.popleft()
        intervals.remove(interval)

        # store the results of the subroutine to cores
        processed_nodes += temporal_graph.number_of_nodes
        cores[interval] = subroutine(temporal_graph, set(temporal_graph.nodes_iterator), interval, print_file=print_file, number_of_cores=number_of_cores)[0]

        # if there are cores in the interval
        if len(cores[interval]) > 0:
            # get its descendant intervals
            descendant_intervals = get_descendant_intervals(interval, temporal_graph)
            # for each descendant interval
            for descendant_interval in descendant_intervals:
                # if the descendant interval has not already been found
                if descendant_interval not in intervals:
                    # add the descendant interval to the queue
                    intervals_queue.append(descendant_interval)
                    intervals.add(descendant_interval)

    # end of the algorithm
    execution_time.end_algorithm()

    # print algorithm's results
    print_end_algorithm(execution_time.execution_time_seconds, number_of_cores[0], processed_nodes)
