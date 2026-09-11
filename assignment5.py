def lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    # Reconstruct the LCS
    i = m
    j = n
    answer = []

    while i > 0 and j > 0:

        if seq1[i - 1] == seq2[j - 1]:
            answer.append(seq1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse because we built the answer backwards
    answer.reverse()

    return dp[m][n], ''.join(answer)


# Main program
seq1 = "ABCBDAB"
seq2 = "BDCABA"

length, subsequence = lcs(seq1, seq2)

print("Sequence 1:", seq1)
print("Sequence 2:", seq2)
print("Longest Common Subsequence:", subsequence)
print("Length of LCS:", length)