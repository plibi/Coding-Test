def solution(x, y, n):
    if x == y:
        return 0

    dp = [1e9 for __ in range(1000001)]
    dp[x] = 0
    
    for i in range(x, y+1):
        if dp[i] == 1e9:
            continue
        if i + n <= 1000000:
            dp[i+n] = min(dp[i+n], dp[i]+1)
        if i * 2 <= 1000000:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i * 3 <= 1000000:
            dp[i*3] = min(dp[i*3], dp[i]+1)
    
    if dp[y] == 1e9:
        return -1
    else:
        return dp[y]