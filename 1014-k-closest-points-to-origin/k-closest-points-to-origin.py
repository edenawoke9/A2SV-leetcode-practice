import math

class Solution(object):
    def kClosest(self, points, k):
       
        distances = []
        for point in points:
            sqrt = math.sqrt(point[0]**2 + point[1]**2)
            distances.append((sqrt, point))  
        distances.sort(key=lambda x: x[0])
        
      
        return [distances[i][1] for i in range(k)]
