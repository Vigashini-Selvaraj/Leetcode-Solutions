class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        a=0
        for i in strs:
            if i.isdigit():
                a=max(a,int(i))
            else:
                a=max(a,len(i))
        return a
        