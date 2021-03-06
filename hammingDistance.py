class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x^y
        ans = 0
        while (z>0):
            if (z%2 == 1):
                ans = ans+1
            z = z//2
        return ans
