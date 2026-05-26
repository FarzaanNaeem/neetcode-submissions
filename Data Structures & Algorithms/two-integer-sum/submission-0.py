class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in _map:
                return [_map[remaining], i]
            _map[nums[i]] = i


