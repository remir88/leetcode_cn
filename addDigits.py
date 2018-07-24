class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = num
        while (ans > 9):
            add = 0
            tmp = ans
            while (tmp > 0):
                add = add + tmp%10
                tmp = tmp // 10
            ans = add
        return ans
    
            
