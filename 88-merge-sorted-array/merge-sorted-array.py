class Solution(object):
    def merge(self,nums1, m,nums2,n):
     i=m-1
     j=n-1
     totali=m+n-1
     while j>=0:
        if i>=0 and nums1[i]>=nums2[j]:
            nums1[totali]=nums1[i]
            i-=1
        else:
            nums1[totali]=nums2[j]
            j-=1
        totali-=1
        