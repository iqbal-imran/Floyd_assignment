import sys

# Global variable
graph = [[0, 7, sys.maxsize, 8],
         [sys.maxsize, 0, 5, sys.maxsize],
         [sys.maxsize, sys.maxsize, 0, 2],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0]]

def get_floyd_iterative(graph):
    
    ln = len(graph)
    distances = [[graph[a][b] for b in range(ln)] for a in range(ln)]

    for k in range(ln):
        for a in range(ln):
            for b in range(ln):
                if distances[a][k] != sys.maxsize and distances[k][b] != sys.maxsize:
                    distances[a][b] = min(distances[a][b], distances[a][k] + distances[k][b])
    
    return (distances)

print(get_floyd_iterative(graph))
