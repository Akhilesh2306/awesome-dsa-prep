"""
First and Last Occurrence

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].


Examples:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation:The target is 8, and it appears in the array at indices 3 and 4, so the output is [3,4]

Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Expalantion: The target is 6, which is not present in the array. Therefore, the output is [-1, -1].
"""


# ----------------------------
# Brute Force Solution
# ----------------------------
def searchRangeBrute(self, nums, target):

    # length of array
    n = len(nums)

    # initializing two pointers for first and last occurrence
    first, last = -1, -1

    # traversing the array for finding first occurrence of target
    for i in range(n):
        # finding the first occurrence of the element
        if nums[i] == target:
            first = i
            break

    # traversing the array for finding last occurrence of target
    for i in range(n - 1, first - 1, -1):
        # finding the first occurrence of the element
        if first >= 0 and nums[i] == target:
            last = i
            break

    # returning first and last occurrence of target
    return [first, last]


"""
Time Complexity: O(n) in the worst case, due to two loops that iterate through the array, and O(1) in the best case, when the target is not found
Space Complexity: O(1), because it uses a constant amount of extra space for variables regardless of the input size
"""


# ----------------------------
# Optimal Solution I
# ----------------------------
# Using lower and upper bound


def lowerBound(nums, target):
    """
    Returns the first index where nums[index] >= target.
    If all elements are smaller than target, returns len(nums).
    """
    n = len(nums)
    low, high = 0, n - 1
    ans = n  # default answer if target is greater than all elements

    while low <= high:
        mid = (low + high) // 2  # middle index

        if nums[mid] >= target:
            # mid is a potential answer, but there might be an even smaller index
            ans = mid
            high = mid - 1  # shrink search space to the left half
        else:
            # nums[mid] < target, so ignore left half
            low = mid + 1

    return ans


def upperBound(self, nums, target):
    """
    Returns the first index where nums[index] > target.
    If all elements are <= target, returns len(nums).
    """
    n = len(nums)
    low, high = 0, n - 1
    ans = n  # default answer if target is greater or equal to all elements

    while low <= high:
        mid = (low + high) // 2  # middle index

        if nums[mid] > target:
            # mid is a potential answer, but there might be an even smaller index
            ans = mid
            high = mid - 1  # shrink search space to the left half
        else:
            # nums[mid] <= target, so ignore left half
            low = mid + 1

    return ans


def searchRangeOptimalI(self, nums, target):
    """
    Returns the first and last index of target in sorted array nums.
    If target is not found, returns [-1, -1].
    Uses lowerBound and upperBound.
    """

    n = len(nums)

    # Find first index where nums[i] >= target
    first_occurrence = self.lowerBound(nums, target)

    # Find first index where nums[i] > target
    last_occurrence = self.upperBound(nums, target) - 1

    # If lower_bound is out of range OR target is not actually present
    if first_occurrence == n or nums[first_occurrence] != target:
        return [-1, -1]

    # upper_bound points to first index greater than target,
    # so last occurrence of target is upper_bound - 1
    return [first_occurrence, last_occurrence]


""" 
Time Complexity: O(log n) because the lowerBound and upperBound functions, which are called within searchRange, use binary search.
Space Complexity: O(1) as it uses a constant amount of extra space.
"""


# ----------------------------
# Optimal Solution II
# ----------------------------
def first_occurrence(self, nums: list[int], target: int) -> int:
    """
    Find the first (leftmost) occurrence of target in a sorted array.
    Returns index if found, otherwise -1.
    """
    n = len(nums)
    ans = -1
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            # Potential answer found, but keep searching left side
            ans = mid
            high = mid - 1

        elif nums[mid] < target:
            # Target is in right half
            low = mid + 1

        else:
            # Target is in left half
            high = mid - 1

    return ans


def last_occurrence(self, nums: list[int], target: int) -> int:
    """
    Find the last (rightmost) occurrence of target in a sorted array.
    Returns index if found, otherwise -1.
    """
    n = len(nums)
    ans = -1
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            # Potential answer found, but keep searching right side
            ans = mid
            low = mid + 1

        elif nums[mid] < target:
            # Target is in right half
            low = mid + 1

        else:
            # Target is in left half
            high = mid - 1

    return ans


def searchRangeOptimalII(self, nums, target):
    """
    Return both the first and last occurrence of target in sorted array.
    If target not found, returns [-1, -1].
    """
    first_index = self.first_occurrence(nums, target)
    last_index = self.last_occurrence(nums, target)

    return [first_index, last_index]


"""
Time Complexity: O(log n) due to binary search in first_occurrence and last_occurrence functions.
Space Complexity: O(1) because it uses a constant amount of extra space.
"""
