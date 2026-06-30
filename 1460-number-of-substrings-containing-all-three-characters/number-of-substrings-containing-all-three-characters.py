class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        count={}
        ans=0
        n=len(s)
        for r in range(n):
            count[s[r]]=count.get(s[r],0)+1
            while len(count)==3:
                ans+=n-r
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
        return ans
        