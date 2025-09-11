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


### Using Recursion
def targetSearch(nums: list[int], low: int, high: int, target: int) -> int:
    # base case
    if low > high:
        return -1

    # to store index of target
    mid = (low + high) // 2

    # if element at mid < target, searching in right space
    if nums[mid] < target:
        target_index = targetSearch(nums, mid + 1, high, target)
    # if element at mid > target, searching in left space
    elif nums[mid] > target:
        target_index = targetSearch(nums, low, mid - 1, target)
    # target found, return the index
    else:
        target_index = mid

    return target_index


def search(nums, target):
    # length of array
    n = len(nums)

    # recursive call to the targetSearch function
    return targetSearch(nums, 0, n - 1, target)


"""
Time Complexity: O(log n) due to the binary search halving the search space in each recursive call.
Space Complexity: O(log n) due to the recursive call stack in the worst-case scenario.
"""
