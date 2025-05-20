from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


def create_test_tree():
    """Создает тестовое дерево для всех тестовых случаев."""
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    return root


def main():
    solution = Solution()
    root = create_test_tree()

    test_cases = [
        {
            "name": "Тест 1: LCA для узлов в разных поддеревьях",
            "p": root.left,  # 2
            "q": root.right,  # 8
            "expected": 6,
        },
        {
            "name": "Тест 2: LCA для узлов в одном поддереве",
            "p": root.left,  # 2
            "q": root.left.right,  # 4
            "expected": 2,
        },
        {
            "name": "Тест 3: LCA для узлов на разных уровнях",
            "p": root.left.right.left,  # 3
            "q": root.left.right.right,  # 5
            "expected": 4,
        },
    ]

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"Узлы: {test['p'].val} и {test['q'].val}")
        result = solution.lowestCommonAncestor(root, test["p"], test["q"])
        print(f"Ожидаемый LCA: {test['expected']}")
        print(f"Полученный LCA: {result.val}")
        print(f"Тест {'пройден' if result.val == test['expected'] else 'не пройден'}")


if __name__ == "__main__":
    main()
