class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for string in strs:
            return_string += str(len(string)) + "#" + string
        return return_string

    def decode(self, s: str) -> List[str]:
        return_list, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            return_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return return_list

