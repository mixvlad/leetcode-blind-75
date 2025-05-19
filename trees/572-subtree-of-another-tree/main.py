from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        if (
            (p is None or q is None)
            or p.val != q.val
            or not self.isSameTree(p.left, q.left)
            or not self.isSameTree(p.right, q.right)
        ):
            return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        @param: root: The root of the main tree
        @param: subRoot: The root of the subtree to check
        @return: True if subRoot is a subtree of root, False otherwise
        """
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


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

    test_cases = [
        {
            "name": "Test 1: Simple subtree",
            "root": root1,
            "subRoot": subRoot1,
            "expected": True,
        },
        {
            "name": "Test 2: Subtree with additional node",
            "root": root2,
            "subRoot": subRoot2,
            "expected": False,
        },
    ]

    print("Running subtree tests:")
    print("-" * 50)

    for test in test_cases:
        result = solution.isSubtree(test["root"], test["subRoot"])
        print(f"\n{test['name']}")
        print(f"Expected result: {test['expected']}")
        print(f"Actual result: {result}")
        print(f"Test {'PASSED' if result == test['expected'] else 'FAILED'}")
        print("-" * 50)


if __name__ == "__main__":
    main()
