"""
Find Square Root of a number

Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).

Examples:
Input: n = 36
Output: 6
Explanation: 6 is the square root of 36.
"""


# ----------------------------
# Brute Force Solution
# ----------------------------
def floorSqrtBrute(self, n: int) -> int:
    # If n is 0 or 1 then return n
    if n == 0 or n == 1:
        return n

    # Initialize sqrt to 0 (default for n = 0)
    sqrt = 0

    # Iterate from 1 up to n-1
    # (we stop earlier because if i^2 > n, further values will also exceed n)
    for i in range(1, n):
        val = i * i

        # If i^2 is still <= n, update sqrt
        if val <= n:
            sqrt = i
        else:
            # Stop as soon as i^2 exceeds n (no need to check further)
            break

    # Return the largest integer whose square is <= n
    return sqrt


"""
Time Complexity: O(sqrt(n)) due to the loop iterating up to the floor of the square root of n.
Space Complexity: O(1) because it uses a constant amount of extra space.
"""


# ----------------------------
# Optimal Solution
# ----------------------------
def floorSqrtOptimal(self, n: int) -> int:
    # Base cases:
    # sqrt(0) = 0 and sqrt(1) = 1
    if n == 0 or n == 1:
        return n

    # Search space for possible sqrt values:
    # The square root of n will never be more than n//2 when n > 1
    low, high = 1, n // 2

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2

        # Instead of mid * mid <= n (risk of overflow),
        # we check mid <= n // mid (equivalent but safer).
        if mid <= n // mid:
            # mid is a valid candidate, but there might be a larger one
            # so move to the right half
            low = mid + 1
        else:
            # mid*mid > n, so move to the left half
            high = mid - 1

    # At the end of the loop:
    # 'low' will have crossed the sqrt boundary,
    # so the correct floor(sqrt(n)) is stored in 'high'
    return high


"""
Time Complexity: O(log(n)) due to the binary search performed on the search space from 1 to n/2
Space Complexity:O(1) as it uses a constant amount of extra space.
"""
