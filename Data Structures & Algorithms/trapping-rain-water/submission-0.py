class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left_index = 0
        right_index = len(height) - 1

        left_max = height[left_index]
        right_max = height[right_index]

        while left_index < right_index:
            if height[left_index] <= height[right_index]:
                left_index += 1
                if left_max > height[left_index]:
                    res += left_max - height[left_index]
                else:
                    left_max = height[left_index]

            else:
                right_index -= 1
                if right_max > height[right_index]:
                    res += right_max - height[right_index]
                else:
                    right_max = height[right_index]
        return res
