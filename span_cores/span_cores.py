import argparse

from temporal_graph.temporal_graph import TemporalGraph
from decomposition.decomposition import decomposition
from maximal.naive_maximal import naive_maximal
from maximal.maximal import maximal
from decomposition.naive_decomposition import naive_decomposition
from utilities.print_file import PrintFile
from utilities.print_console import print_dataset_name, print_dataset_info

if __name__ == '__main__':
    # create a parser
    parser = argparse.ArgumentParser(description='Mining (maximal) span-cores from temporal networks')
    # arguments
    parser.add_argument('d', help='dataset')
    parser.add_argument('a', help='algorithm')
    # options
    parser.add_argument('--ver', dest='ver', action='store_true', default=False, help='verbose')

    # read the arguments
    args = parser.parse_args()

    # create the output file if the --ver option is provided
    if args.ver:
        print_file = PrintFile(args.d + '_' + args.a)
    else:
        print_file = None

    # create the input graph and print its name
    temporal_graph = TemporalGraph(args.d)
    print_dataset_name(args.d)

    # run the selected algorithm
    if args.a == 'nsc':
        print '-------- Naive-span-cores ---------'
        naive_decomposition(temporal_graph, print_file)
    elif args.a == 'sc':
        print '------------ Span-cores -----------'
        decomposition(temporal_graph, print_file)
    elif args.a == 'nmsc':
        print '----- Naive-maximal-span-cores ----'
        naive_maximal(temporal_graph, print_file)
    elif args.a == 'msc':
        print '-------- Maximal-span-cores -------'
        maximal(temporal_graph, print_file)
    # dataset info
    else:
        print '--------------- Info --------------'
        print_dataset_info(temporal_graph)
