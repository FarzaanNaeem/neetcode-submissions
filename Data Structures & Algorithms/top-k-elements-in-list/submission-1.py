from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)
        res = []
        heap = []

        for key, val in freq.items():
            heappush(heap, (-val, key))
            
        while heap and len(res) < k:
            _, key = heappop(heap)
            res.append(key)
        
        return res