class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in prevMap:
                prevMap[sorted_string].append(string)
                continue
            prevMap[sorted_string] = [string]
        
        return list(prevMap.values())