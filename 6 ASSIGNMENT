# 0/1 Knapsack using Top-Down and Bottom-Up approaches

# ---------- Top-Down Approach ----------
def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, capacity):
        if i == n or capacity == 0:
            return 0

        if (i, capacity) in memo:
            return memo[(i, capacity)]

        # Do not select the item
        not_take = solve(i + 1, capacity)

        # Select the item
        take = 0
        if weights[i] <= capacity:
            take = values[i] + solve(i + 1, capacity - weights[i])

        memo[(i, capacity)] = max(take, not_take)
        return memo[(i, capacity)]

    return solve(0, capacity)


# ---------- Bottom-Up Approach ----------
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ---------- Main Program ----------
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

top_down_result = knapsack_top_down(weights, values, capacity)
bottom_up_result = knapsack_bottom_up(weights, values, capacity)

print("Weights:", weights)
print("Values :", values)
print("Capacity:", capacity)

print("\nMaximum Value using Top-Down:", top_down_result)
print("Maximum Value using Bottom-Up:", bottom_up_result)
