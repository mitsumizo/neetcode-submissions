class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def search(path, start_index, remaining):
            if remaining == 0:
                result.append(path)
                return
            if remaining < 0:
                return
            for i in range(start_index, len(nums)):
                search(path + [nums[i]], i, remaining - nums[i])



        search([], 0, target)
        return result

