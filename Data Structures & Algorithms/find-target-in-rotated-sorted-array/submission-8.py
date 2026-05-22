class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # 真ん中を見つける
            middle_index = left + (int(right - left) // 2)
            # 真ん中がターゲットだったら終了
            if target == nums[middle_index]:
                return middle_index            

            # 左側の坂にいる
            if nums[left] <= nums[middle_index]:
                # 左側の坂はソートずみ
                if nums[left] <= target and target <= nums[middle_index]:
                    right = middle_index - 1
                else:
                    left = middle_index + 1
            # 右側の坂にいる
            else :
                # 右側はソート済み
                if nums[middle_index] <= target and target <= nums[right]:
                    left = middle_index + 1
                else:
                    right = middle_index - 1

        return -1                  
