class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(combination, curr_sum, start_idx):
            if curr_sum == target:
                res.append(combination)
                return
            if curr_sum > target:
                return
            for i in range(start_idx, len(candidates)):
                curr_num = candidates[i]
                dfs(combination + [curr_num], curr_sum + curr_num, i)
                
        dfs([], 0, 0)
        return res
