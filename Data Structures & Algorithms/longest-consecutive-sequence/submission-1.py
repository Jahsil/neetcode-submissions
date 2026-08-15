class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 1
        arr = list(set(nums))

        arr = sorted(arr)
        maxVal = 1
        tmp = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == 1:
                tmp += 1
            else:
                tmp = 1
            maxVal = max(maxVal, tmp)
        return maxVal
