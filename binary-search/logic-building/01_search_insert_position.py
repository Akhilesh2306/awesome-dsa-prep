"""
Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


Examples:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2.

Input: nums = [1, 3, 5, 6], target = 2
Output: 1
Explanation: The target value 2 is not found in the array. However, it should be inserted at index 1 to maintain the sorted order of the array.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def searchInsert(nums, target):
    # length of array
    n = len(nums)

    # initializing two pointers for array traversal
    low, high = 0, n - 1

    while low <= high:
        # calculate mid index
        mid = (low + high) // 2

        # if target found at mid index, then return the index
        if nums[mid] == target:
            return mid

        # find the target in the right space
        elif nums[mid] < target:
            low = mid + 1

        # find the target in the left space
        else:
            high = mid - 1

    # if the element is not found, the low pointer has the position where the element should be inserted.
    return low


"""
Time Complexity: O(log n) due to the binary search algorithm.
Space Complexity: O(1) because it uses a constant amount of extra space.
"""
