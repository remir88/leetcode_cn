#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for x in range(0, len(s)//2):
            if s[x]!=s[len(s)-(x+1)]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), 0, -1):
            for i in range(0, len(s)-length+1):
                if self.isPalindrome(s[i:length+i]):
                    return(s[i:length+i])
        return(s)

# @lc code=end

