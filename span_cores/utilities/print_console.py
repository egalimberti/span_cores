from __future__ import division

from memory_measure import memory_usage_resource


def print_dataset_name(dataset_path):
    print '------------- Dataset -------------'
    print 'Name: ' + dataset_path.split('/')[0]


def print_dataset_info(temporal_graph):
    print '|V|: ' + str(temporal_graph.number_of_nodes)
    print '|E|: ' + str(temporal_graph.number_of_edges)
    print '|T|: ' + str(temporal_graph.number_of_timestamps)


def print_end_algorithm(execution_time_seconds, number_of_cores, processed_nodes):
    print 'output span-cores:  ' + str(number_of_cores)
    print 'time (s):           ' + str(execution_time_seconds)
    print 'memory (MB):        ' + str(memory_usage_resource())
    print 'processed vertices: ' + str(processed_nodes)
