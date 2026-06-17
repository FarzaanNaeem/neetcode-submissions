class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Approach
        # prod_arr = []
        # for i in range(len(nums)):
        #     curr_prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         curr_prod *= nums[j]
        #     prod_arr.append(curr_prod)
        # return prod_arr

        # Prefix sum Approach
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1

        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]

        for j in range(n-2, -1, -1):
            suff[j] = nums[j+1] * suff[j+1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
