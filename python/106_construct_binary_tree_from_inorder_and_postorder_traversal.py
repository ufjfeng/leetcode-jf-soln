"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or inorder == []:
            return None
        rVal = postorder.pop()
        rIdx = inorder.index(rVal)
        root = TreeNode(rVal)
        root.right = self.buildTree(inorder[rIdx + 1:], postorder)
        root.left = self.buildTree(inorder[:rIdx], postorder)
        return root
