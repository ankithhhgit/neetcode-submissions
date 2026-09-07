class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        interval = len(nums)

        s = set(nums)

        for i in range(interval+1):
            if i not in s :
                return i



        