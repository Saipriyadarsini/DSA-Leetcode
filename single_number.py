"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
"""


def singleNumber(nums):
       nums.sort()
       count=0
       while count<len(nums)-1:
        if nums[count]==nums[count+1]:
            count+=2
        else:
            return nums[count]
       return nums[count]

nums=singleNumber([4,1,2,1,2])
print(nums)