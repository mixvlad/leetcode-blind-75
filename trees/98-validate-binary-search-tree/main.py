from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        @param: root: The root of the binary tree
        @return: True if the tree is a valid BST, False otherwise
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1: [2,1,3]
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    
    # Test case 2: [5,1,4,null,null,3,6]
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    
    # Test case 3: [1,1]
    root3 = TreeNode(1)
    root3.left = TreeNode(1)
    
    test_cases = [root1, root2, root3]
    
    for i, root in enumerate(test_cases, 1):
        result = solution.isValidBST(root)
        print(f"Test case {i}:")
        print(f"Is valid BST: {result}")
        print()

if __name__ == "__main__":
    main() 