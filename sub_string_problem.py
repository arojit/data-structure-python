def longest_common_substring(s1, s2):
    # Dynamic Programming Approach
    dp = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
    maxm = 0
    lst = []
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lst.append(s1[i - 1])
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > maxm:
                    maxm = dp[i][j]

    return maxm


def longest_unique_substring(s1):
    # Sliding Window Approach
    seen = {}
    i = 0
    maxm = 0

    for j in range(len(s1)):
        c = s1[j]

        while seen.get(c):
            del seen[s1[i]]
            i += 1
        seen[c] = True
        maxm = max(maxm, j - i + 1)
    return maxm


if __name__ == '__main__':
    s1 = "ABCDGH"
    s2 = "ACDGHR"
    res = longest_common_substring(s1, s2)
    print(res)

    s1 = "abcdebcdefg"
    res = longest_unique_substring(s1)
    print(res)

