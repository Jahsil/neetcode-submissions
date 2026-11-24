class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Algorithm:
        # use floyds algorithm to detect a cycle: 
        # first increment slow pointer and fast pointer until both are equal 
        # then start a new slow pointer and move until the values of the
        # new slow and old slow are equal 
        # at that instant you have found the cycle starting point 

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
        


