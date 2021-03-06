"""
The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called the "root." Besides the root, each house has
one and only one parent house. After a tour, the smart thief realized that "all
houses in this place forms a binary tree". It will automatically contact the
police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting
the police.

Example 1:
    
         3
        / \
       2   3
        \   \ 
         3   1
    
    Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
        
         3
        / \
       4   5
      / \   \ 
     1   3   1

    Maximum amount of money the thief can rob = 4 + 5 = 9.

Credits:
    Special thanks to @dietpepsi for adding this problem and creating all test
    cases.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        soln = self.robDP(root)
        return max(soln)

    def robDP(self, root):
        soln = [0, 0]
        if root is None:
            return soln
        left = self.robDP(root.left)
        right = self.robDP(root.right)
        soln[0] = max(left) + max(right)
        soln[1] = root.val + left[0] + right[0]
        return soln
        
"""
Note:
    step by step tutorial
    https://discuss.leetcode.com/topic/39834/step-by-step-tackling-of-the-problem

    Approach III
    for each root, return soln = [int, int], where soln[0] is the max robbed
    value when root is not robbed, soln[1] is the max robbed value when root is
    robbed
"""
