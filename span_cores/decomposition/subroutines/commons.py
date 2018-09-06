from array import array


def get_interval(start, end=None):
    if end is None:
        end = start

    return start, end


def get_descendant_intervals(interval, temporal_graph):
    descendant_intervals = []

    if interval[0] > 0:
        descendant_intervals.append(get_interval(interval[0] - 1, interval[1]))

    if interval[1] < temporal_graph.number_of_timestamps - 1:
        descendant_intervals.append(get_interval(interval[0], interval[1] + 1))

    return descendant_intervals


def add_descendants_to_queue(interval, temporal_graph, intervals_queue, ancestors, descendants_count):
    # get the descendant intervals
    descendant_intervals = get_descendant_intervals(interval, temporal_graph)

    # for each descendant interval
    for descendant_interval in descendant_intervals:
        try:
            # update the list of its ancestors
            ancestors[descendant_interval].append(interval)
            # add the descendant interval to the queue
            intervals_queue.append(descendant_interval)

            # if the descendant interval has not already been found
        except KeyError:
            # create the list of ancestors
            ancestors[descendant_interval] = [interval]

        try:
            # increment the number of descendants
            descendants_count[interval] += 1

            # if this is the first descendant
        except KeyError:
            # initialize descendants_count for interval
            descendants_count[interval] = 1


def get_ancestors_intersection(interval, ancestors, cores, temporal_graph, descendants_count):
    try:
        intersection = set(cores[ancestors[interval][0]][1]) & set(cores[ancestors[interval][1]][1])

        for ancestor_interval in ancestors[interval]:
            decrement_descendants_count(ancestor_interval, descendants_count, cores)

        return intersection
    except KeyError:
        return set(temporal_graph.nodes_iterator)


def decrement_descendants_count(interval, descendants_count, cores):
    descendants_count[interval] -= 1

    if descendants_count[interval] == 0:
        del descendants_count[interval]
        del cores[interval]


def add_core_to_solution(interval, k, nodes, cores, delta_sets, maximum_index, print_file, number_of_cores, in_memory):
    # if the core exists
    if len(nodes) > 0:
        # add it to the solution set
        if in_memory or k == 1:
            cores[k] = array('i', nodes)

        if print_file is not None:
            try:
                unique = len(delta_sets[k]) > 0
            except IndexError:
                unique = True

            if unique:
                print_file.print_core(interval, k, nodes)

        # update the maximum index
        maximum_index[0] += 1

        if number_of_cores is not None:
            number_of_cores[0] += 1
