def solution(A):
    n = len(A)
    if n < 2:
        return 0

    # Preprocess array for circular reference
    A.extend(A)

    # Initialize dynamic programming table
    dp = [0] * (2 * n)

    # Dynamic programming for finding maximum pairs
    for i in range(1, 2 * n - 1):
        if (A[i - 1] + A[i]) % 2 == 0:
            dp[i] = dp[i - 2] + 1
        else:
            dp[i] = max(dp[i - 1], dp[i - 2])

    max_pairs = 0
    for i in range(n, 2 * n - 1):
        max_pairs = max(max_pairs, dp[i] - dp[i - n])
        print(max_pairs)
    print(dp)
    return max_pairs


A = [4, 2, 5, 8, 7, 3, 7]
print(solution(A))  # Output: 2



"""A = [14, 21, 16, 35, 22]
print(solution(A))  # Output: 1"""
