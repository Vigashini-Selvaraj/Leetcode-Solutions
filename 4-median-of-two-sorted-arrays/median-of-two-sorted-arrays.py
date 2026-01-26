class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        a=len(arr)
        if a%2==0:
            mid=a//2
            return (arr[mid-1]+arr[mid])/2
        else:
             mid=a//2
             return arr[mid]


        