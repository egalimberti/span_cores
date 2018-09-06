from sys import platform
from resource import getrusage, RUSAGE_SELF


def memory_usage_resource():
    # denominator for MB
    rusage_denominator = 1024
    # if the OS is MAC OSX
    if platform == 'darwin':
        # adjust the denominator
        rusage_denominator *= rusage_denominator

    # return the memory usage
    return getrusage(RUSAGE_SELF).ru_maxrss / rusage_denominator
