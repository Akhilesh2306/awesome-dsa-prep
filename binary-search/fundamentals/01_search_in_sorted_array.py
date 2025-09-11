"""
Search X in sorted array

Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. If the target is found in the array, return its index. If the target is not found, return -1.

Examples:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: The target integer 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: The target integer 2 does not exist in nums so return -1
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def search(self, nums, target):
    # length of array
    n = len(nums)

    # initializing boundaries
    low, high = 0, n - 1

    # traversing array to search target element
    while low <= high:
        # finding mid index
        mid = (low + high) // 2

        # check if element at mid index is lesser than target
        if nums[mid] < target:
            # increment low
            low = mid + 1

        elif nums[mid] > target:
            # decrement high
            high = mid - 1

        else:
            # target element found at mid index
            return mid

    # if element not found in the array
    return -1


"""
Time Complexity: O(log n) - Binary search reduces the search space by half in each iteration.
Space Complexity: O(1) - Constant extra space is used for variables, regardless of the input size.
"""
