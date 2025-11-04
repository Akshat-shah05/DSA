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
                vals.append("#")
                return None
            
            postorder(node.left)
            postorder(node.right)
            vals.append(str(node.val))
        
        postorder(root)
        return ",".join(vals)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = data.split(",")
        def build():
            if not vals:
                return None
            
            v = vals.pop()
            if v == "#":
                return None
            
            node = TreeNode(int(v))
            node.right = build()
            node.left = build()
            return node
        
        return build()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans