class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch=set()
        left=0
        maxi=0
        for right in range(len(s)):
            while s[right] in ch:
                ch.remove(s[left])
                left+=1


            else:
                ch.add(s[right])
                maxi=max(maxi,right-left+1)
        return maxi
        

       
        