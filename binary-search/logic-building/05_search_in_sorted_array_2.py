"""
Search in sorted array - II

Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.


Examples:
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Output: True
Explanation: The element 3 is present in the array. So, the answer is True.

Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Output: False
Explanation:The element 10 is not present in the array. So, the answer is False.
"""


# ----------------------------
# Brute Force Solution
# ----------------------------
def searchInARotatedSortedArrayIIBrute(self, nums: list[int], target: int) -> bool:
    # array length
    n = len(nums)

    # traversing array to find target element
    for i in range(n):
        # check if the current element equals to target
        if nums[i] == target:
            return True

    # if target not found, return False
    return False


"""
Time Complexity: O(n) due to iterating through the array once.
Space Complexity: O(1) because it uses constant extra space.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def searchInARotatedSortedArrayIIOptimal(self, nums: list[int], target: int) -> bool:
    # length of the array
    n = len(nums)

    # intialize two pointers
    low, high = 0, n - 1

    # traverse the array to find out the target element
    while low <= high:
        # find the mid index
        mid = (low + high) // 2

        # if target found, return it
        if nums[mid] == target:
            return True

        # handle duplicates: shrink search space
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            # restart loop after shrinking
            continue

        # left half [low...mid] is sorted
        if nums[low] <= nums[mid]:
            # target lies in left half
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            # otherwise, search in right half
            else:
                low = mid + 1

        # right half [mid...high] is sorted
        else:
            # target lies in right half
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            # otherwise, search in left half
            else:
                high = mid - 1

    # target not found
    return False


"""
Time Complexity: O(log n) in the average case, O(n) in the worst case due to duplicates.
Space Complexity: O(1) as it uses constant extra space.
"""
