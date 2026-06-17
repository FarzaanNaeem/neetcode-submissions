class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Approach
        prod_arr = []
        for i in range(len(nums)):
            curr_prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                curr_prod *= nums[j]
            prod_arr.append(curr_prod)
        return prod_arr