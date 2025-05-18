from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        @param: root: The root of the binary tree
        @return: The maximum depth of the tree
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Test case 2: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    
    test_cases = [root1, root2]
    
    for i, root in enumerate(test_cases, 1):
        depth = solution.maxDepth(root)
        print(f"Test case {i}:")
        print(f"Maximum depth: {depth}")
        print()

if __name__ == "__main__":
    main() 