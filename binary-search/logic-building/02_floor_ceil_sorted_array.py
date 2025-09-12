"""
Floor and Ceil in Sorted Array

Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.

Examples:
Input : nums =[3, 4, 4, 7, 8, 10], x= 5
Output: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

Input : nums =[3, 4, 4, 7, 8, 10], x= 8
Output: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""


# ----------------------------
# Brute Force Solution
# ----------------------------
def getFloorAndCeilBrute(nums, x):
    # length of array
    n = len(nums)

    # initializing the values for floor and ceil
    floor, ceil = 0, 0

    # traversing the array to get floor value
    for i in range(n):
        if nums[i] <= x:
            floor = nums[i]
        else:
            # breaking the loop when nums[i] > x
            break

    # traversing the array in reverse order to get ceil value
    for i in range(n - 1, -1, -1):
        if nums[i] >= x:
            ceil = nums[i]
        else:
            # breaking the loop when nums[i] < x
            break

    # if floor or ceil not found, then return -1
    if floor == 0:
        floor = -1
    if ceil == 0:
        ceil = -1

    return floor, ceil


"""
Time Complexity: O(n) because in the worst-case scenario, both loops iterate through the entire array of size n.
Space Complexity: O(1) because the algorithm uses a constant amount of extra space.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def getFloorAndCeilOptimal(nums, x):
    # length of array
    n = len(nums)

    # initializing the values for floor and ceil
    floor, ceil = 0, 0

    # initializing two pointers for binary search
    low, high = 0, n - 1

    while low <= high:
        # calculating mid pointer
        mid = (low + high) // 2

        # if current element at mid equals x, then return the element
        if nums[mid] == x:
            return nums[mid], nums[mid]

        # if current element at mid is <= x, assign the element to floor and low to mid+1
        elif nums[mid] <= x:
            floor = nums[mid]
            low = mid + 1

        # if current element at mid is >= x, assign the element to ceil and high to mid-1
        else:
            ceil = nums[mid]
            high = mid - 1

    # if floor or ceil not found, then return -1
    if floor == 0:
        floor = -1

    if ceil == 0:
        ceil = -1

    return floor, ceil


"""
Time Complexity: O(log n) due to binary search.
Space Complexity: O(1) as it uses constant extra space.
"""
