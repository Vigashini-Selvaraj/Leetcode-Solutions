class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=sorted(nums)
        res=[]
        for i in nums:
            res.append(ans.index(i))
        return res
        