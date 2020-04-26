#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in range(0, len(s)):
            if (s[x] == '(') or (s[x] == '{') or (s[x] == '['):
                stack.append(s[x])
            elif (len(stack) == 0):
                return False
            elif (s[x] == ')') and (stack.pop() != '('):
                return False
            elif (s[x] == '}') and (stack.pop() != '{'):
                return False
            elif (s[x] == ']') and (stack.pop() != '['):
                return False
        if (len(stack) == 0):
            return True
        else:
            return False
            
# @lc code=end

