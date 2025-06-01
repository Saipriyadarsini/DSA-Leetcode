"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""
def plusOne(self,digits):
    n=len(digits)
    for i in range(n-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits