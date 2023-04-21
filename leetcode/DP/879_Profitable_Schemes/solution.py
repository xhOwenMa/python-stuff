class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        N = len(group) # to make later codes cleaner

        # create dp of size (n+1) * (minProfit+1)
        # dp[i][j] means number of schemes with at most i members and at least j profits
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1 # there is only one way to have 0 member and generate 0 profit

        for k in range(N):
            g, p = group[k], profit[k]

            for i in range(n - g, -1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i+g][min(j + p, minProfit)] += dp[i][j]
                    dp[i+g][min(j + p, minProfit)] %= 10**9 + 7
                    
        return sum(dp[i][minProfit] for i in range(n+1)) % (10**9 + 7)
    