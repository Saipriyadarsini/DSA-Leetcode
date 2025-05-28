"""
An array is considered special if the parity of every pair of adjacent elements is different. 
In other words, one element in each pair must be even, and the other must be odd.
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
"""

def isArraySpecial(self, nums):
        def odd(num):
            return num%2==1
        if len(nums)<=1:
            return True
        else:
            for i in range(len(nums)-1):
               if odd(nums[i]) == odd(nums[i + 1]):
                 return False

        return True
        