#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="":
            return ""
        ls = len(s)
        longest = s[0]
        for i in range(0, ls):
            if len(longest)>min(ls-i, i)*2+1:
                continue
            
            # case 1: aba
            j = 0
            while (i-j-1>=0)and(i+j+1<ls):
                if (s[i-j-1]==s[i+j+1]):
                    j += 1
                else:
                    break
            if (2*j+1)>len(longest):
                longest = s[i-j:i+j+1]

            # case 2: abba
            j = 0
            while (i-j>=0)and(i+j+1<ls):
                if (s[i-j]==s[i+j+1]):
                    j += 1
                else:
                    break
            if (2*j>len(longest)):
                longest = s[i-j+1:i+j+1]
        return longest
# @lc code=end

