""""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Input: nums = [1,2,2,3]
Output: true
"""
def isMonotonic(self, nums):
       def increasing():
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]: 
                    return False
            return True
      
       def decreasing():
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
            return True

       return increasing() or decreasing()