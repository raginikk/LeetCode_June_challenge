class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if nums[i]>nums[j]:
                    temp = nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                j+=1
        return nums 
