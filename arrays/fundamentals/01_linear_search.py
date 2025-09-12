"""
Linear Search

Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1.

Examples:
Input: nums = [2, 3, 4, 5, 3], target = 3
Output: 1
Explanation:
The first occurence of 3 in nums is at index 1

Input: nums = [2, -4, 4, 0, 10], target = 6
Output: -1
Explanation:
The value 6 does not occur in the array, hence output is -1
"""


def linearSearch(nums: list[int], target: int) -> int:
    # Special case: If the array has only one element and it's the target
    if len(nums) == 1 and nums[0] == target:
        return 0

    # Iterate through each element in the list
    for i in range(len(nums)):
        # If the current element matches the target, return its index
        if nums[i] == target:
            return i

    # If the loop ends without finding the target, return -1
    return -1


"""
Time Complexity: O(n) because, in the worst case, the algorithm iterates through the entire input array 'nums' once.
Space Complexity: O(1) because the algorithm uses a constant amount of extra space.
"""
