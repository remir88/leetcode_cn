class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (t1==None and t2==None):
            return(None)
        t = TreeNode((t1.val if (t1!=None) else 0)+(t2.val if (t2!=None) else 0))
        t.left = self.mergeTrees(t1.left if (t1!=None) else None, t2.left if (t2!=None) else None)
        t.right = self.mergeTrees(t1.right if (t1!=None) else None, t2.right if (t2!=None) else None)
        return(t)
