# Importing the sys module will allow us to fetch max size attributes to deal with infinite values
# for our task. It also give us access to parameters and other functionalities specific to the system.

import sys

# GLobal Variable
# By default these variable are visible from any function (unless shadowed by locals).
graph = [[0, 7, sys.maxsize, 8],
        [sys.maxsize, 0, 5, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, 2],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]]


# Declaring Floyd Recursive Function
def get_floyd_recursive_solution(val):

    """
    This function will check the shortest path between vertices

    :Parameters: We declare function listing their parameters "val", then call them passing argument "graph", which is our 2D matrix graph.
    :return Value: The shortest path is returned to the calling code.

    """ 

# Local Variables
    ln = len(val)
    NO_PATH = sys.maxsize
    distances = [[val[a][b] for b in range(ln)] for a in range(ln)]
    

# Declaring a nested Method to find the shortest deistance 
    def check_floyd_recursive(distances, k, a, b):
        
        """
            We are using Recursion programming pattern that is useful in this situation to find the distance between vertices
            a and b using intermediate vertex k
                1) The parameter "distance" will give the distances between all pairs of vertices.
                2) The parameters "k" "a" "b" are intermediate, starting and ending vertices. 
                3) Following the intermediate vertex k the shortest path between vertices a and b will "return" 
        """

        # Condition to check if there is no intermediate vertex to use.
        while k == ln:
            return distances[a][b] 
        
        # We have created two variables to run recursive computing to find the shortest distance between two vertices “a” and “b”
        k_abs = check_floyd_recursive(distances, k + 1, a, b)
        k_aval = (check_floyd_recursive(distances, k + 1, a, k) + check_floyd_recursive(distances, k + 1, k, b))


        if k_aval < NO_PATH:
            distances[a][b] = min(k_abs, k_aval)
        return distances[a][b]

    for k in range(ln):
        for a in range(ln):
            for b in range(ln):
                check_floyd_recursive(distances, k, a, b)

    return distances


outcome = get_floyd_recursive_solution(graph)

print(outcome)


