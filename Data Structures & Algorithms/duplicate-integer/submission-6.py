class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        ###### Brute Force #############
        ###### Time complexity: O(n^2)#############
        ###### Space complexity: O(1) #############
        ###### Brute Force #############
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
###-------------------------------------------###
        ###### Sorting #############
        ###### Time complexity: O(n log n)#############
        ###### Space complexity: O(1) or O(n) #############
        ###### Sorting #############

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
            
        return False

###-------------------------------------------###
        ###### Hash Set #############
        ###### Time complexity: O(n)#############
        ###### Space complexity: O(n) #############
        ###### Sorting #############

        seen = set()

        for num in nums:
            if num in seen:
                return True
        return False
        # return n != len(set(nums))

        # return False
