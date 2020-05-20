#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = 0
        dic = {}
        dic.clear()
        longest = 0
        length = 0

        for q in range(0, len(s)):
            if s[q] in dic:
                while s[p]!=s[q]:
                    del dic[s[p]]
                    p += 1
                    length -= 1
                p += 1
            else:
                length += 1
                dic[s[q]] = True
            if longest<length:
                longest = length

        return longest

# @lc code=end

