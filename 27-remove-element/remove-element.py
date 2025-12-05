class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_pointer=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[current_pointer]=nums[i]
                current_pointer+=1
        return(current_pointer)
      
            



        