class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxSum = float('-inf')
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                if maxSum < ones:
                    maxSum = ones
                ones = 0

        if maxSum < ones:
            maxSum = ones

        return maxSum