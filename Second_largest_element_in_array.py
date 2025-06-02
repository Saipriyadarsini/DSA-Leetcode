"""
Find the second largest element in an array
else retrun -1
"""
def getSecondLargest(self, arr):
        k=sorted(set(arr))
        if len(k) < 2:
         return -1
        return k[-2]