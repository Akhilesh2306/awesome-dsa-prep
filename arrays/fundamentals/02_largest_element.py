"""
Largest Element

Given an array of integers nums, return the value of the largest element in the array

Examples:
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6

Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99
"""


def largestElement(nums: list[int]) -> int:
    # Special case: If the array has only one element, return it directly
    if len(nums) == 1:
        return nums[0]

    # Assume the first element is the largest initially
    largest_element = nums[0]

    # Traverse the rest of the array to find the maximum
    for i in range(1, len(nums)):
        # If a larger element is found, update largest_element
        if nums[i] > largest_element:
            largest_element = nums[i]

    # Return the largest element found
    return largest_element


"""
Time Complexity: O(n) because the code iterates through the input array once.
Space Complexity: O(1) as it uses a constant amount of extra space.
"""
