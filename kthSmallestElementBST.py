# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        230. Kth Smallest Element in a BST

        Given the root of a binary search tree, and an integer k, 
        return the kth smallest value (1-indexed) of all the values 
        of the nodes in the tree.

        Input: root = [3,1,4,null,2], k = 1
        Output: 1

        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3
        
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        n = 0 #Number of nodes visited
        cur = root
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
            
