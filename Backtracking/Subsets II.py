class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.generate_subsets(nums, 0, [], subsets)
        return subsets
    
    def generate_subsets(self, nums, start, subset, subsets):
        subsets.append(subset[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.generate_subsets(nums, i+1, subset, subsets)
            subset.pop()
