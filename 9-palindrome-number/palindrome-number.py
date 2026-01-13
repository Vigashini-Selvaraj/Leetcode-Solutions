class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        re=0
        if x<0:
            return False
        while num>0:
            r=num%10
            re=re*10+r
            num//=10
        return x==re
    
       
        
        