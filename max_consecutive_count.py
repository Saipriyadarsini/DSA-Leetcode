"""
Input: arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
Output: 4
Explanation: The maximum number of consecutive 1's in the array is 4 from index 8-11.
"""
def maxConsecutiveCount(self,arr):
    maxCount, count = 0, 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 1

    return max(maxCount, count)