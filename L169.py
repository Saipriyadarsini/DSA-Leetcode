""" 
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""
def majorityElement(self, nums):
       count = Counter(nums)
       return max(count,key=count.get)

"""
2nd approach using Boyer-Moore Voting Algorithm
"""

def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate