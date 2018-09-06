from array import array


def subroutine(adjacency_list, nodes):
    # cores dict
    cores = {}

    # degree of each node
    delta = {node: len(set(adjacency_list[node]) & nodes) for node in nodes}

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
            for neighbor in adjacency_list[node]:
                if neighbor in nodes and delta[neighbor] > index:
                        # update its delta_set
                        delta_sets[delta[neighbor]].remove(neighbor)
                        delta_sets[delta[neighbor] - 1].add(neighbor)

                        # update its degree
                        delta[neighbor] -= 1

        # add the core to the solution
        if len(nodes) > 0:
            maximum_index = index + 1
            cores[maximum_index] = array('i', nodes)

    # return the maximal core
    try:
        return maximum_index, cores[maximum_index]
    except UnboundLocalError:
        return 0, array('i')
