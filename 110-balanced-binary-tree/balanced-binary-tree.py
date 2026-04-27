# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balance(root):
            if not root:
                return (True, 0)

            leftBalanced, leftMax = balance(root.left)
            rightBalanced, rightMax = balance(root.right)

            return (leftBalanced and rightBalanced and abs(leftMax - rightMax) <= 1, 1 + max(leftMax, rightMax))
        
        ans, _ = balance(root)
        return ans



        