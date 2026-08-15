class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums = sorted(nums)
        ans = []

        for i in range(N):
            num = nums[i]

            left, right = i + 1, N - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right: 
                target = nums[left] + nums[right]

                if num + target == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif num + target > 0:
                    right -= 1 
                else:
                    left += 1
        return ans

                