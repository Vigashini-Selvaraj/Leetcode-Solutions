class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        L = 0
        R = len(height) - 1
        while L < R:
            curr_area = ((R - L) * min(height[L], height[R]))
            if (res < curr_area):
                res = curr_area
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return res

    
            
        

     
    