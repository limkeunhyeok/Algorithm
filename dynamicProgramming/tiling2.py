def tiling2(n):
    dp = [1, 2]
    if n == 1: return dp[0]
    if n == 2: return dp[1]
    for i in range(n - 2):
        dp.append(dp[i] + dp[i + 1])
    return dp[-1] % 1000000007