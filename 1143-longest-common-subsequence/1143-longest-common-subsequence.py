class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]
        
        
        
        flag1 = False
        for i in range(len(text1)):
            if text1[i] == text2[0] or flag1:
                dp[i][0] = 1
                flag1 = True
        
        flag2 = False
        for j in range(len(text2)):
            if text1[0] == text2[j] or flag2:
                dp[0][j] = 1
                flag2 = True
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[len(text1)-1][len(text2)-1]