"""
Upper Bound

Given a sorted array of nums and an integer x, write a program to find the upper bound of x.

The upper bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than a given key i.e. x.

If no such index is found, return the size of the array.


Examples:
Input : n= 4, nums = [1,2,2,3], x = 2
Output: 3
Explanation:
Index 3 is the smallest index such that arr[3] > x.

Input : n = 5, nums = [3,5,8,15,19], x = 9
Output: 3
Explanation:
Index 3 is the smallest index such that arr[3] > x.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def upperBound(self, nums, x):
    # length of array
    n = len(nums)

    # store the upper bound of x, initializing with length array
    ans = n

    # initializing two pointers for traversing array
    low, high = 0, n - 1

    while low <= high:
        # compute mid index
        mid = (low + high) // 2

        # check if current element at mid pointer is greater than target, If it is then store the index and decrement high pointer
        if nums[mid] > x:
            ans = mid
            high = mid - 1
        else:
            # check if current element at mid pointer is lesser than equal to target, increment low pointer
            low = mid + 1

    return ans


""" 
Time Complexity: O(log n) due to the binary search algorithm.
Space Complexity: O(1) as it uses a constant amount of extra space.
"""
