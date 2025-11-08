# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def postorder(node):
            if not node:
                vals.append("#") # represents a None Node 
                return 
            
            postorder(node.left)
            postorder(node.right)
            vals.append(str(node.val))
        
        postorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        def rebuild():
            if not vals:
                return None
            
            v = vals.pop()
            if v == "#":
                return None
            
            node = TreeNode(int(v))
            node.right = rebuild()
            node.left = rebuild()
            return node
        
        return rebuild()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))