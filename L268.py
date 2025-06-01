"""
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""

#1st approach
def missingNumber(self, nums):
      nums.sort()
      k=len(nums)
      for i in range(k+1):
        if i not in nums:
            return i
        
#2nd approach
def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum
        