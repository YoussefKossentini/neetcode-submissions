class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j=0
        for i in range(j+1,len(nums)):
            if nums[j]==nums[i]:
                return True 
            else : 
                j+=1
        return False
