class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefixProduct, suffixProduct = [1] * (N + 1), [1] * (N + 1)
        output = [1] * N

        for i in range(1, N + 1):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]
        for i in range(N - 1,-1, -1):
            suffixProduct[i] = suffixProduct[i + 1] * nums[i]

        for i, num in enumerate(nums):
            output[i] = prefixProduct[i] * suffixProduct[i + 1]
        return output

        

