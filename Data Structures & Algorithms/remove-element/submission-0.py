class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newArr = []
        for i in range(len(nums)):
            if nums[i] != val:
                print(nums[i])
                newArr.append(nums[i])
                    
        for i in range(len(nums)):
            if i >= len(newArr):
                nums[i] = None
            else:
                nums[i] = newArr[i]

        return len(newArr)