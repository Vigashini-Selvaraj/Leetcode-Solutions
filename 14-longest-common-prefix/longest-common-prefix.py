class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        result=""
        s1=strs[0]
        s2=strs[-1]
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                result+=s1[i]
            else:
                break
        return result
      



    
        