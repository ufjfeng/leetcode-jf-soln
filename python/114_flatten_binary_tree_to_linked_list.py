"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

Hints:
If you notice carefully in the flattened tree, each node's right child points
to the next node of a pre-order traversal.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        leftLeaf = self.findLeaf(root.left)
        rightRoot = root.right
        if leftLeaf:
            root.right = root.left
            root.left = None
            leftLeaf.right = rightRoot

    def findLeaf(self, root):
        if root is None:
            return None
        p = root
        while p.right:
            p = p.right
        return p


