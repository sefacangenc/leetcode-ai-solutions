class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        s = str(root.val)
        s += "," + self.serialize(root.left)
        s += "," + self.serialize(root.right)
        return s

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        queue = data.split(",")
        return self.deserialize_helper(queue)

    def deserialize_helper(self, queue: List[str]) -> TreeNode:
        if not queue:
            return None
        val = queue.pop(0)
        if val == "":
            return None
        node = TreeNode(int(val))
        node.left = self.deserialize_helper(queue)
        node.right = self.deserialize_helper(queue)
        return node
