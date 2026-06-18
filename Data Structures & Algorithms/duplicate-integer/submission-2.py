class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # _map = Counter(nums)
        # for key, val in _map.items():
        #     if _map[key] > 1:
        #         return True
        # return False
        # nums_set = set(nums)
        # return len(nums_set) != len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        