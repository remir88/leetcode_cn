#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        p = 0
        q = len(s)-1
        deleted = False
        while True:
            if p >= q:
                return True
            if s[p]!=s[q]:
                if not deleted:
                    deleted = True
                    if s[p+1] == s[q]:
                        p += 1
                    else:
                        break
                else:
                    break
            p += 1
            q -= 1

        p = 0
        q = len(s)-1
        deleted = False        
        while True:
            if p >= q:
                return True
            if s[p]!=s[q]:
                if not deleted:
                    deleted = True
                    if s[p] == s[q-1]:
                        q -= 1
                    else:
                        break
                else:
                    break
            p += 1
            q -= 1

        return False
            
# @lc code=end

