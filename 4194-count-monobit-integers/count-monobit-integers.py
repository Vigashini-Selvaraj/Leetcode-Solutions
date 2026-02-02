class Solution:
    def countMonobit(self, n: int) -> int:
        res=[]
        count=0
        for i in range(n+1):
            a=bin(i)[2:]
            print(a)
            res.append(a)
        for i in res:
            if len(set(i))==1:
                count+=1
        return count
        