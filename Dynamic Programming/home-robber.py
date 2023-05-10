
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]


"""class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        prev_max, curr_max = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp

        return curr_max

"""
