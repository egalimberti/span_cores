from array import array

from commons import add_core_to_solution


def subroutine(temporal_graph, nodes, interval, print_file=None, number_of_cores=None, in_memory=False):
    # cores dict
    cores = {}
    # maximum index
    maximum_index = [0]

    # neighbors in the intersection graph
    intersection_neighbors = {}

    # interval iterator
    interval_iterator = xrange(interval[0] + 1, interval[1] + 1)

    # degree of each node in the specified interval
    delta = {}
    # for each node
    for node in nodes:
        # compute the degree in the specified interval
        neighbors = nodes & set(temporal_graph.adjacency_list[node][interval[0]])
        for timestamp in interval_iterator:
            neighbors &= set(temporal_graph.adjacency_list[node][timestamp])

        # add it to delta
        delta[node] = len(neighbors)

        # add the neighbors to intersection_neighbors
        intersection_neighbors[node] = array('i', neighbors)

    # sets of nodes divided by degree
    delta_sets = [set() for _ in xrange(max(delta.itervalues()) + 1)]
    # for each node
    for node in nodes:
        # put the node in the set corresponding to its degree
        delta_sets[delta[node]].add(node)

    # for each set in delta_sets
    for index, delta_set in enumerate(delta_sets):
        # while the set is not empty
        while len(delta_set) > 0:
            # remove a node from the set and from nodes
            node = delta_set.pop()
            nodes.remove(node)

            # for each neighbor in nodes
            for neighbor in intersection_neighbors[node]:
                if neighbor in nodes and delta[neighbor] > index:
                    # update its delta_set
                    delta_sets[delta[neighbor]].remove(neighbor)
                    delta_sets[delta[neighbor] - 1].add(neighbor)

                    # update its degree
                    delta[neighbor] -= 1

        # add the core to the solution
        add_core_to_solution(interval, index + 1, nodes, cores, delta_sets, maximum_index, print_file, number_of_cores, in_memory)

    return cores, maximum_index[0]
