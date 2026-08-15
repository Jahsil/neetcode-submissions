class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 1

        numsSet = set(nums)
        maxVal = 1

        for num in nums:
            tmp = 1
            if (num - 1 not in numsSet):
                while (num + tmp ) in numsSet:
                    tmp += 1
            maxVal = max(maxVal, tmp)

        return maxVal
