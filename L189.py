"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
 def rotate(self, nums, k):
        length = len(nums)  #length
        result = [0] * n #creating a empty list with the same size as nums
        for i in range(n):
            result[(i + k) % n] = nums[i]  #to rotate the nums list and store in result
        nums[:] = result  # copying result to original list

        