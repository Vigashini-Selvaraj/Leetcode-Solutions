class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res=[]
        nums.sort()
        for i in queries:
            total=0
            count=0
            for j in nums:
                if total+j<=i:
                    count+=1
                    total+=j
                else:
                    break
            res.append(count)
        return res


        

        