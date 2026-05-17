class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for target_num in nums_set:
            # 先頭の値じゃなければ無視
            if (target_num - 1) in nums_set:
                    continue

            # 見つかるまでカウント
            count = 1
            while (target_num + count) in nums_set:
                count += 1
            
            # 大きい方を取得
            max_length = max(count, max_length)

        return max_length
