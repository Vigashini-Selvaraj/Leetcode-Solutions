class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if len(res)==1:
            b=res[-1]
            res.append(b)
        elif len(res)>2:
            ans.append(res[0])
            ans.append(res[-1])
            return ans
        elif len(res)==0:
            res.append(-1)
            res.append(-1)
        return res
            

        