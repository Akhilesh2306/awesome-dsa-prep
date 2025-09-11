"""
Lower Bound

Given a sorted array of nums and an integer x, write a program to find the lower bound of x.

The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

If no such index is found, return the size of the array.


Examples:
Input : nums= [1,2,2,3], x = 2
Output:1
Explanation:
Index 1 is the smallest index such that arr[1] >= x.

Input : nums= [3,5,8,15,19], x = 9
Output: 3
Explanation:
Index 3 is the smallest index such that arr[3] >= x.
"""


# ----------------------------
# Brute Force Solution
# ----------------------------
def lower_bound_brute(nums, x):
    # length of array
    n = len(nums)

    for i in range(n):
        # check condition for current element
        if nums[i] >= x:
            return i

    # if lower bound not found, return length of array
    return n


""" 
Time Complexity: O(n) because in the worst case, the loop iterates through all elements of the input array nums.
Space Complexity: O(1) because the algorithm uses a constant amount of extra space, regardless of the input size.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def lower_bound_optimal(nums, x):
    # length of array
    n = len(nums)

    # to store the index
    ans = n

    # initializing the pointers
    low, high = 0, n - 1

    while low <= high:
        # calculate mid pointer
        mid = (low + high) // 2

        # if current element at mid is greater than equal to x, then store in ans and decrement high (left search space)
        if nums[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            # else, look into right search space
            low = mid + 1

    return ans


"""
Time Complexity: O(log n) due to the binary search algorithm.
Space Complexity: O(1) as it uses a constant amount of extra space.
"""
