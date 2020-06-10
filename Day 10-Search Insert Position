def getIndex(value,arr):
    for num in range(len(arr)):
        if value<=arr[num]:
            return num
    return len(arr)    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            
        return getIndex(target,nums)
        
