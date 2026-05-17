class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """complexity O(1) but O(n)
        Point : This list is sorted!
        """

        left_index = 0
        right_index = len(numbers) - 1

        while left_index <= right_index:
            cal_num = numbers[left_index] + numbers[right_index]

            if cal_num == target:
                return [left_index + 1, right_index + 1]
            elif cal_num < target:
                left_index += 1
            else :
                right_index -= 1

        return None
