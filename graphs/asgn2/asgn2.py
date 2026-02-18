from dataclasses import dataclass, field
import unittest

@dataclass
class Vertex:
    """
    Class for vertices, you can add more attributes, and functions
    """
    id : int
    visited = False
    previsit = 0
    postvisit = 0
    visiting = False
    adjacencyList : list["Vertex"] = field(default_factory=list)

@dataclass
class Graph:
    """
    Class for the graph, you can add more attributes, and functions
    """
    clock = 0
    cycles = False
    vertices : list[Vertex] = field(default_factory=list)

    def create(self, input: list[list[int]]):
        for i in range(len(input)):
            self.vertices.append(Vertex(i))

        for i in range(len(input)):
            for pre in input[i]:
                self.vertices[pre].adjacencyList.append(self.vertices[i])
        self.dfs()
                
    def explore(self, v : Vertex):
        v.visiting = True
        v.visited = True
        v.previsit = self.clock
        self.clock += 1

        for u in v.adjacencyList:
            if not u.visited:
                self.explore(u)
            elif u.visited and u.visiting:
                self.cycles = True

        v.visiting = False
        v.postvisit = self.clock
        self.clock += 1

    def dfs(self):
        for v in self.vertices:
            if not v.visited:
                self.explore(v)

    def has_order(self) -> bool:
        return not self.cycles

    def get_order(self) -> list[int]:
        if self.cycles:
            return []
        
        finished = []

        for v in self.vertices:
            finished.append((v.postvisit, v.id))
            
        finished.sort(reverse=True)
        order = []

        for x, course in finished:
            order.append(course)
        return order
    


class TestCourseSchedule(unittest.TestCase):

    def test_example(self):
        input = [[2], [0], []]
        result = Graph()
        result.create(input)
        self.assertEqual(result.has_order(), True)
        
if __name__ == "__main__":
    unittest.main()

# completed