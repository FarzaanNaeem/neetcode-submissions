class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _map = Counter(nums)
        for key, val in _map.items():
            if _map[key] > 1:
                return True
        return False
        