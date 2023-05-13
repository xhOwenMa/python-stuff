class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [0] * (high + 1) # dp[i] means the number of good strings of length i
        dp[0] = 1 # length 0 is empty string

        mod = 10**9 + 7

        # iteratively find the amount of good strings by incrementing the string length
        for end in range(1, high + 1):
            if end >= zero:
                # this means we can append `zero` amount of 0s
                dp[end] += dp[end - zero]
            if end >= one:
                # this means we can append `one` amount of 1s
                dp[end] += dp[end - one]
            dp[end] %= mod

        return sum(dp[low : (high + 1)]) % mod