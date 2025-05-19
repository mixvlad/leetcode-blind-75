from typing import List, Optional


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


def list_to_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def main():
    solution = Solution()
    test_cases = [
        {"input": [[1, 2, 3], [1, 2, 3]], "expected": True, "name": "Example 1"},
        {"input": [[1, 2], [1, None, 2]], "expected": False, "name": "Example 2"},
        {"input": [[1, 2, 1], [1, 1, 2]], "expected": False, "name": "Example 3"},
    ]

    for tc in test_cases:
        p = list_to_binary_tree(tc["input"][0])
        q = list_to_binary_tree(tc["input"][1])
        result = solution.isSameTree(p, q)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: p = {tc['input'][0]}, q = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
