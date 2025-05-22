from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    max_sum = float("-inf")

    def max_gain(node):
        if not node:
            return 0

        # Max sum on the left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Current node's contribution to the max path sum
        current_gain = node.val + left_gain + right_gain

        # Update the global max sum
        nonlocal max_sum
        max_sum = max(max_sum, current_gain)

        # Return the max gain for the parent call
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum


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
    test_cases = [
        {"input": [1, 2, 3], "expected": 6, "name": "Example 1"},
        {"input": [-10, 9, 20, None, None, 15, 7], "expected": 42, "name": "Example 2"},
    ]

    for tc in test_cases:
        root = list_to_binary_tree(tc["input"])
        result = max_path_sum(root)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: root = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
