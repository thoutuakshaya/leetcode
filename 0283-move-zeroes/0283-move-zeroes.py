class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        arr = []

        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(nums[i])

        n = len(nums) - len(arr)
        arr.extend([0] * n)

        for i in range(len(nums)):
            nums[i] = arr[i]