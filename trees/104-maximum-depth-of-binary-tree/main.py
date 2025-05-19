from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def main():
    solution = Solution()

    # Test cases with expected results
    test_cases = [
        {
            "name": "Balanced tree [3,9,20,null,null,15,7]",
            "tree": TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            "expected": 3,
        },
        {
            "name": "Unbalanced tree [1,null,2]",
            "tree": TreeNode(1, None, TreeNode(2)),
            "expected": 2,
        },
        {"name": "Empty tree", "tree": None, "expected": 0},
        {"name": "Single node tree", "tree": TreeNode(1), "expected": 1},
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test['name']}")
        result = solution.maxDepth(test["tree"])
        print(f"Expected depth: {test['expected']}")
        print(f"Actual depth: {result}")
        print(f"Result: {'✓' if result == test['expected'] else '✗'}")


if __name__ == "__main__":
    main()
