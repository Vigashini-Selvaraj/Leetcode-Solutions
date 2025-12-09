class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        ans="1"
        
        for n in range(n-1):
            res=[]
            i=0
            while i<len(ans):
                count=1
                while i+1<len(ans) and ans[i]==ans[i+1]:
                    i+=1
                    count+=1
                res.append(str(count)+ans[i])
                i+=1
            ans="".join(res)
        return ans


       
       


            

    
           





        