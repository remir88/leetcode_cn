#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    __li = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__li = []
        

    def push(self, x: int) -> None:
        self.__li.append(x)

    def pop(self) -> None:
        return self.__li.pop()

    def top(self) -> int:
        return self.__li[len(self.__li)-1]

    def getMin(self) -> int:
        return min(self.__li)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

