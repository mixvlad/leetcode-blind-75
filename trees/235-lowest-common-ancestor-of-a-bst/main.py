from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        @param: root: The root of the BST
        @param: p: First node
        @param: q: Second node
        @return: The lowest common ancestor of p and q
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    
    p1 = root1.left  # 2
    q1 = root1.right  # 8
    
    # Test case 2: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    root2 = root1
    p2 = root2.left  # 2
    q2 = root2.left.right  # 4
    
    test_cases = [(root1, p1, q1), (root2, p2, q2)]
    
    for i, (root, p, q) in enumerate(test_cases, 1):
        result = solution.lowestCommonAncestor(root, p, q)
        print(f"Test case {i}:")
        print(f"LCA of {p.val} and {q.val}: {result.val}")
        print()

if __name__ == "__main__":
    main() 