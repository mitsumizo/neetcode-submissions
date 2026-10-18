class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_list = []
        check_map = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            check_map[sorted_word].append(word)

        for value in check_map.values():
            return_list.append(value)

        return return_list 