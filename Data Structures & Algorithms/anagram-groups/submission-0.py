from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for _str in strs:
            count = [0] * 26 # represents 26 letters in the alphabet
            for char in _str:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(_str)
        return list(result.values())