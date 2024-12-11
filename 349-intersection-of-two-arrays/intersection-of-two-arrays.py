class Solution(object):
    def intersection(self, nums1, nums2):
       result=[]
       for x in nums1:
        if x in nums2 and x not in result:
            result.append(x)
       return result
        