class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []

        for index in range(len(temperatures)):
            target = temperatures[index]

            count = 0
            for sub_index in range(index+1, len(temperatures)):
                count += 1
                if target >= temperatures[sub_index]:
                    continue
                res.append(count)
                break
            if index + 1 != len(res):
                res.append(0)
        return res 
