"""
Search in sorted array - I

Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.


Examples:
Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output: -1
Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.
"""


# ----------------------------
# Brute Force Solution
# ----------------------------
def searchBrute(nums: list[int], k: int) -> int:
    # array length
    n = len(nums)

    # array traversal to find the target element
    for i in range(n):
        if nums[i] == k:
            return i

    # if element not found, return -1
    return -1


"""
Time Complexity: O(n) due to the linear scan of the input array in the worst case.
Space Complexity: O(1) as it uses a constant amount of extra space.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def searchOptimal(nums: list[int], target: int) -> int:
    # array length
    n = len(nums)

    # initializing two pointers for array traversal
    low, high = 0, n - 1

    while low <= high:
        # find middle index
        mid = (low + high) // 2

        # if target is found directly at mid
        if nums[mid] == target:
            return mid

        # check if the left half [low...mid] is sorted
        if nums[low] <= nums[mid]:
            # if target lies within sorted left half
            if nums[low] <= target <= nums[mid]:
                # move search space to left half
                high = mid - 1
            else:
                # otherwise, target lies in right half
                low = mid + 1

        # otherwise, the right half [mid...half] is sorted
        else:
            # if target lies within this sorted right half
            if nums[mid] <= target <= nums[high]:
                # move search space to right half
                low = mid + 1
            else:
                # otherwise, target lies in left half
                high = mid - 1

    return -1


"""
Time Complexity: O(log n) due to the binary search.
Space Complexity: O(1) as it uses a constant amount of extra space.
"""
