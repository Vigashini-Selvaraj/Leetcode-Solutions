class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ab={}
        for i ,num in enumerate(nums):
            diff=target-nums[i]
            if diff in ab:
                return [ab[diff],i]
            ab[num]=i

     

        