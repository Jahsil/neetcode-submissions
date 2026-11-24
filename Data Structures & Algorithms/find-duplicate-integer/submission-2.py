class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        secondSlow = 0 
        ans = 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: 
                break

        while True: 
            secondSlow = nums[secondSlow]
            slow = nums[slow]
            if secondSlow == slow: 
                return secondSlow
        return ans
        


