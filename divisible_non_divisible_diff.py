"""
Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
"""
def differenceOfSums(self, n, m):
        div=0
        not_div=0
        for i in range(n+1):
            if i%m==0:
                div+=i
            else:
                not_div+=i
        return not_div-div