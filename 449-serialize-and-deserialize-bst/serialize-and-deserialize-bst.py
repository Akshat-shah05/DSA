# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def postorder(node):
            if not node:
                return
            
            postorder(node.left)
            postorder(node.right)
            vals.append(str(node.val))
        
        postorder(root)
        return ",".join(vals)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []

        vals = list(map(int, data.split(",")))

        def build(low, high):
            if not vals:
                return None
            
            if not low < vals[-1] < high:
                return None
            
            v = vals.pop()
            node = TreeNode(v)
            node.right = build(v, high)
            node.left = build(low, v)
            return node
        
        return build(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans