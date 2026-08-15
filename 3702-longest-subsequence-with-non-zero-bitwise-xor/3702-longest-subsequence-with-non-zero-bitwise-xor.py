class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor_sum = 0
        all_zeros = True
        
        for num in nums:
            xor_sum ^= num
            if num != 0:
                all_zeros = False
                
        # Edge Case: If all elements are 0, we can never get a non-zero XOR
        if all_zeros:
            return 0
            
        # If total XOR is non-zero, we can use the whole array
        if xor_sum != 0:
            return len(nums)
            
        # If total XOR is zero, removing any single non-zero element makes it non-zero
        return len(nums) - 1
