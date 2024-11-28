class Solution(object):
    def maxWidthOfVerticalArea(self, points):
       self.points=points
       points.sort(key=lambda x:x[0])
       maxx=0
       for x in range(len(points)-1):
           difference=points[x+1][0]-points[x][0]
       
           maxx=max(maxx,difference)
       return maxx
