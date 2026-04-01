# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check if they have the same depth
        depth_p = self.find_depth(root, p.val, depth=0)
        depth_q = self.find_depth(root, q.val, depth=0)

        while depth_p > depth_q:
            p = self.find_parent(root, p.val)
            depth_p -= 1

        while depth_q > depth_p:
            q = self.find_parent(root, q.val)
            depth_q -= 1

        # now move both up until they meet
        while p.val != q.val:
            p = self.find_parent(root, p.val)
            q = self.find_parent(root, q.val)

        return p

        
        
    def find_depth(self ,root, val, depth=0):
        if root is None:
            return -1
        if root.val == val:
            return depth
        if val < root.val:
            return self.find_depth(root.left, val, depth+1)
        else: 
            return self.find_depth(root.right, val, depth+1)

    def find_parent(self, root,val, parent=None):
        if root is None:
            return None
        if root.val == val:
            return parent
        if val < root.val: 
            return self.find_parent(root.left, val, root)
        else: 
            return self.find_parent(root.right, val, root)
        