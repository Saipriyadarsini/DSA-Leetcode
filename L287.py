"""
Input: nums = [1,3,4,2,2]
Output: 2
"""
class Solution(object):
    def findDuplicate(self, nums):
        # Phase 1: Find the intersection point of the two runners
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
