class Solution:
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack, swap back

        result = []
        backtrack(0)
        return result