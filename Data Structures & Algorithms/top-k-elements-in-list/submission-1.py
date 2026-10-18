class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = collections.defaultdict(int)

        for num in nums:
            countMap[num] += 1

        return sorted(countMap, key=countMap.get, reverse=True)[:k]