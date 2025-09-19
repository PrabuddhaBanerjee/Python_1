# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        import collections
        """
        102. Binary Tree Level Order Traversal

        Given the root of a binary tree, return the level order 
        traversal of its nodes' values. (i.e., from left to right, 
        level by level).

        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]

        Example 2:
        Input: root = [1]
        Output: [[1]]

        Example 3:
        Input: root = []
        Output: []

        Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000

        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Time Complexity O(N)
        if root == None:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        return res