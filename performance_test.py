import timeit
import sys

from floyd_iterative import get_floyd_iterative
from floyd import get_floyd_recursive_solution

# Golbal Variables

limit = 500    # We can change the value to get the differnt result each time we run

graph = [[0, 7, sys.maxsize, 8],
         [sys.maxsize, 0, 5, sys.maxsize],
         [sys.maxsize, sys.maxsize, 0, 2],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0]]


# declaring show_performance test function
def show_performance_test():
    get_floyd_recursive_solution(graph)
    get_floyd_iterative(graph)

recursive = timeit.timeit(show_performance_test, number=limit)
iterative = timeit.timeit(show_performance_test, number=limit)

# Printing total duration took by both methods changing value using "limit" variable
print(f"Floyd Recursive Method took {recursive} sec to execute")
print(f"Floyd Iterative Method took {iterative} sec to execute")
