class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs)<=1 or len(strs[0])==0):
            return ""
        j = 0
        flag = True
        while flag:
            for i in range(1,len(strs)):
                if (j>=len(strs[i]) or strs[0][j] != strs[i][j]):
                    flag = False
                    break
            j = j+1
        if (j==0):
            return ""
        else:
            return strs[0][0:j-1]
