class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()
        j = 1

        for i in range(len(nums)):
            if nums[i]!=nums[j]:
                j+=1
            else:
                return nums[j]
        
        return nums[j]



        

        