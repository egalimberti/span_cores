from time import time


class ExecutionTime:

    def __init__(self):
        # execution time
        self.execution_time_milliseconds = 0
        self.execution_time_seconds = 0

        # start to measure the execution time
        self.start_algorithm()

    def start_algorithm(self):
        # start the algorithm
        self.execution_time_milliseconds -= self.current_milliseconds()

    def end_algorithm(self):
        # end the algorithm
        self.execution_time_milliseconds += self.current_milliseconds()

        # convert the milliseconds in seconds
        self.execution_time_seconds = self.execution_time_milliseconds / 1000.0

    @staticmethod
    def current_milliseconds():
        return int(round(time() * 1000))
