from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        @param: root: The root of the binary tree
        @return: A string representation of the tree
        """
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        @param: data: A string representation of the tree
        @return: The root of the reconstructed binary tree
        """
        pass

def main():
    codec = Codec()
    
    # Test case 1: [1,2,3,null,null,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    
    # Test case 2: []
    root2 = None
    
    test_cases = [root1, root2]
    
    for i, root in enumerate(test_cases, 1):
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        print(f"Test case {i}:")
        print(f"Original tree: {root.val if root else None}")
        print(f"Serialized: {serialized}")
        print(f"Deserialized: {deserialized.val if deserialized else None}")
        print()

if __name__ == "__main__":
    main() 