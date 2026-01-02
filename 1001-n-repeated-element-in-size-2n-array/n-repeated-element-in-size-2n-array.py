class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a=len(nums)//2
        b=list(set(nums))
        for i in b:
            if nums.count(i)==a:
                return i
        
       
        