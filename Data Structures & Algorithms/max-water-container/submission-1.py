class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left_index = 0
        right_index = len(height) - 1

        max_area = 0

        while left_index < right_index:
            tmp_area = min(height[left_index],height[right_index]) * (right_index - left_index)
            if tmp_area > max_area:
                max_area = tmp_area            
            if height[left_index] < height[right_index]:
                left_index += 1
            else :
                right_index -= 1
        return max_area            

