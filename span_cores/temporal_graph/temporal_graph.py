from os import getcwd
from os.path import dirname
from array import array
import gc


class TemporalGraph:

    def __init__(self, dataset_path):
        # ****** instance variables ******
        # adjacency list
        self.adjacency_list = None
        # edge sets
        self.edge_sets = None

        # measures
        self.number_of_timestamps = None
        self.number_of_nodes = None
        self.number_of_edges = None

        # iterators
        self.timestamps_iterator = None
        self.nodes_iterator = None

        # dataset path
        self.dataset_path = dataset_path

        # ****** initialization ******
        # read the graph from the specified path
        self.load_dataset(dataset_path)

        # collect garbage
        gc.collect()

    def load_dataset(self, dataset_path):
        # open the file
        try:
            dataset_file = open(dirname(getcwd()) + '/datasets/' + dataset_path + '.txt')
        except IOError:
            dataset_file = open(dirname(dirname(getcwd())) + '/datasets/' + dataset_path + '.txt')

        # read the first line of the file
        first_line = dataset_file.readline()
        split_first_line = first_line.split(' ')

        # set measures
        self.number_of_timestamps = int(split_first_line[0])
        self.number_of_nodes = int(split_first_line[1])
        self.number_of_edges = int(split_first_line[2])

        # set iterators
        self.timestamps_iterator = xrange(self.number_of_timestamps)
        self.nodes_iterator = xrange(self.number_of_nodes)

        # create the adjacency list
        self.adjacency_list = tuple(tuple(array('i') for _ in self.timestamps_iterator) for _ in self.nodes_iterator)
        # create the edge sets
        self.edge_sets = [[] for _ in self.timestamps_iterator]

        # for each line of the file
        for line in dataset_file:
            # split the line
            split_line = line.split(' ')
            timestamp = int(split_line[0])
            from_node = int(split_line[1])
            to_node = int(split_line[2])

            # add the undirected edge
            self.add_edge(from_node, to_node, timestamp)

        # for each timestamp
        for timestamp in self.timestamps_iterator:
            # convert the set of edges in a tuple
            self.edge_sets[timestamp] = tuple(self.edge_sets[timestamp])
        self.edge_sets = tuple(self.edge_sets)

    def add_edge(self, from_node, to_node, timestamp):
        # if the edge is not a self-loop
        if from_node != to_node:
            # add the edge into the adjacency list
            self.adjacency_list[from_node][timestamp].append(to_node)
            self.adjacency_list[to_node][timestamp].append(from_node)
            # add the edge into the sets
            self.edge_sets[timestamp].append((from_node, to_node))

    # ****** edges ******
    def get_number_of_edges(self, timestamp):
        return sum([len(neighbors[timestamp]) for neighbors in self.adjacency_list]) / 2
