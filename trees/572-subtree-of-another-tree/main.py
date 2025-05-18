from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        @param: root: The root of the main tree
        @param: subRoot: The root of the subtree to check
        @return: True if subRoot is a subtree of root, False otherwise
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1: root = [3,4,5,1,2], subRoot = [4,1,2]
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    
    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)
    
    # Test case 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)
    
    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(2)
    
    test_cases = [(root1, subRoot1), (root2, subRoot2)]
    
    for i, (root, subRoot) in enumerate(test_cases, 1):
        result = solution.isSubtree(root, subRoot)
        print(f"Test case {i}:")
        print(f"Result: {result}")
        print()

if __name__ == "__main__":
    main() 