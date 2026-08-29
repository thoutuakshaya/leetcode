class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:


        n = len(nums)

        # value + original index
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]

        i = 0

        while i < n:

            j = i

            # Find one connected group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Values in this group
            values = [arr[x][0] for x in range(i, j + 1)]

            # Original positions of this group
            indices = sorted(arr[x][1] for x in range(i, j + 1))

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                ans[idx] = value

            i = j + 1

        return ans