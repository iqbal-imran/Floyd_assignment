import sys
from floyd import get_floyd_recursive_solution

# Global variables
graph = [[0, 7, sys.maxsize, 8],
         [sys.maxsize, 0, 5, sys.maxsize],
         [sys.maxsize, sys.maxsize, 0, 2],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0]]

outcome = [[0, 7, 12, 8],
        [sys.maxsize, 0, 5, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, 2],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]]


def test_floyd_recursive():
    
    distances = get_floyd_recursive_solution(graph)

    assert distances == outcome

    

