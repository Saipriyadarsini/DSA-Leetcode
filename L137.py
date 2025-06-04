"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
def singleNumber(self, nums):
       
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
              return nums[i]
            i+=3
        return nums[-1]
        """
        count=Counter(nums)
        for num in count:
            if count[num] == 1:
                return num
        """
