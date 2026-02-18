Added Atrributes (they are declared within their class):
    class Vertex:
        + visited = False 
        + previsit = 0 
        + postvisit = 0
        + visiting = False // This is to keep track of recursion
    
    class Graph:
        + clock = 0
        + cycles = False // just a boolean for if there is a cycle

