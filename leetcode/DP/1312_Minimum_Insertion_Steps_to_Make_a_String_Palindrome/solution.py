class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # dp[i][j] stores the minimum insertion steps to make s[i:j+1] a palindrome
        dp = [[0] * n for _ in range(n)]
            
        # Fill in the values for substrings of length 2 or greater
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                
                if s[i] == s[j]:
                    # this means character at i-th and j-th position matches, therefore we do not need to insert any character, so we can reuse what we computed earlier
                    dp[i][j] = dp[i+1][j-1]
                else:
                    # we can either insert a character at i-th position or j-th position to make the substring a palindrome; taking the min to achieve our objective
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
        
        # dp[0][n-1] stores the minimum insertion steps to make s[0:n] a palindrome by definition; s[0:n] is referring to the whole string s
        return dp[0][n-1]

