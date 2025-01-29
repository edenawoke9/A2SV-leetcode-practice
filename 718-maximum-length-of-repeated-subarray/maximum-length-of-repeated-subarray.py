class Solution(object):
    def findLength(self, nums1, nums2):
        matrix = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        
        for i in range(1, len(nums1) + 1):  
            for j in range(1, len(nums2) + 1): 
                if nums1[i-1] == nums2[j-1]:  
                    matrix[i][j] = matrix[i-1][j-1] + 1
        
       
        maxv = max(max(row) for row in matrix)
        return maxv
