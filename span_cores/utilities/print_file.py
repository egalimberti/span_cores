from os import getcwd
from os.path import dirname


class PrintFile:

    def __init__(self, dataset_path):
        # create the output file
        self.core_decomposition_file = open(dirname(getcwd()) + '/output/' + dataset_path + '.txt', 'w')

    def print_core(self, interval, k, nodes):
        # sort the nodes of the core
        sorted_nodes = list(nodes)
        sorted_nodes.sort()
        # write the core to the output file
        self.core_decomposition_file.write(str(interval).replace('(', '[').replace(')', ']') + '\t' + str(k) + '\t' + str(sorted_nodes).replace('[', '').replace(']', '') + '\n')

    def print_maximal_cores(self, maximal_cores):
        # for each interval
        for interval, core in sorted(maximal_cores.iteritems()):
            # print the maximal core
            self.print_core(interval, core[0], core[1])
