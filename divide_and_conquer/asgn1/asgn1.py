import unittest

class Skyline:
    def solve(self, buildings: list[list[int]]) -> list[list[int]]:
        if len(buildings) == 0: 
            return []
        if len(buildings) == 1:
            left = buildings[0][0]
            right = buildings[0][1]
            height = buildings[0][2]
            return [[left,height],[right,0]]

        mid = len(buildings) // 2
        return self.Merge(
            self.solve(buildings[:mid]),
            self.solve(buildings[mid:])
        )

    #Merge Sort Pattern 
    def Merge(self, A1, A2):
        if len(A1) == 0:return A2
        if len(A2) == 0:return A1
        i = 0
        j = 0
        h1 = 0
        h2 = 0
        new = []

        while (i < len(A1)) and (j < len(A2)):
            if A1[i][0] < A2[j][0]:
                x = A1[i][0]
                h1 = A1[i][1]
                i += 1
            elif A2[j][0] <A1[i][0]:
                x = A2[j][0]
                h2 = A2[j][1]
                j += 1
            else:
                x = A1[i][0]
                h1 = A1[i][1]
                h2 = A2[j][1]
                i += 1
                j += 1

            self.pointAdd(new, x, max(h1, h2))

        while i < len(A1):
            self.pointAdd(new, A1[i][0], A1[i][1])
            i += 1

        while j < len(A2):
            self.pointAdd(new, A2[j][0], A2[j][1])
            j += 1

        return new
    
    #helper function
    def pointAdd(self, skyline,x,h):
        if len(skyline) == 0:       
            skyline.append([x, h])

        elif x == skyline[-1][0] :
            skyline[-1][1] = h

        elif h != skyline[-1][1]  :
            skyline.append([x, h])


    
class TestSkyline(unittest.TestCase):
    def setUp(self):
        self.skyline = Skyline()
    def test_no_buildings(self):
        buildings = []
        expected = []
        self.assertEqual(self.skyline.solve(buildings), expected)
    def test_one_building(self):
        buildings = [[2, 9, 10]]
        expected = [[2, 10], [9, 0]]
        self.assertEqual(self.skyline.solve(buildings), expected)
    def test_leetcode_sample(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24,8]]
        expected = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        self.assertEqual(self.skyline.solve(buildings), expected)

if __name__ == '__main__':
    unittest.main()

# completed