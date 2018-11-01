class Solution(object):

    def merge(self, a, b):
        # assume a and b sorted, and recursively return
        # a sorted array of all elements of a and b
        if a == []: return b
        if b == []: return a
        else:
            a_0 = a[0]
            b_0 = b[0]
            if a_0 <= b_0: return [a_0] + self.merge(a[1:],b)
            else: return [b_0] + self.merge(a, b[1:])

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combinedList = self.merge(nums1, nums2)
        mid = (len(combinedList) - 1) / 2
        if len(combinedList) % 2 == 1:
            return float(combinedList[mid])
        else:
            return (float(combinedList[mid]) + float(combinedList[mid+1])) / 2.0
