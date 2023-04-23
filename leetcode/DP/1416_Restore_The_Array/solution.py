class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        mod = 10**9 + 7
        n = len(s)

        # create the dp array: dp[i] refers to "number of arrays for s[0:i]"
        dp = [0] * (n+1)
        # base case: there is only one array (the empty array) for an empty string
        dp[0] = 1

        for start in range(n):
            # not allowed to have leading zeros
            if s[start] == '0':
                continue

            for end in range(start, n):
                num = s[start:end+1]
                if int(num) > k:
                    break

                # if num (= s[start:end+1]) is a valid integer
                dp[end + 1] += dp[start]
                dp[end + 1] %= mod

        # return dp[-1] equiv to dp[n], meaning "number of possible arrays for s[0:n] (wholse string s)"
        return dp[-1]
    