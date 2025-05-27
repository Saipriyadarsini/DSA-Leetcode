"""
Input: chalk = [5,1,5], k = 22
Output: 0
Explanation: The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.
Student number 0 does not have enough chalk, so they will have to replace it.
"""

def chalkReplacer(self, chalk, k):
     sum=0
     p=0
     i=0
     for i in range(len(chalk)):
        sum+=chalk[i]
     rem=k%sum
     for i in range(len(chalk)):
            if rem < chalk[i]:
                return i
            rem -= chalk[i]