class Solution:
    def isValid(self, s: str) -> bool:
        d={
            "(" :  ")",
            "{" :  "}",
            "[" :  "]"
        }
        st=[]
        for i in s:
            if i in d.keys():
                st.append(i)
            elif st==[]:
                return False
            elif i==d[st[-1]]:
                st.pop()
            else:
                return False
        if st==[]:
            return True
        else:
            return False
        