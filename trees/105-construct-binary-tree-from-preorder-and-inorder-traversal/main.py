from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hash map to store value -> index mapping
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build_tree_helper(
            pre_start: int, in_start: int, in_end: int
        ) -> Optional[TreeNode]:
            if pre_start >= len(preorder) or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Get the index from hash map instead of searching in list
            root_index = inorder_map[root_val]

            # Calculate the number of nodes in left subtree
            left_subtree_size = root_index - in_start

            # Recursively build left and right subtrees
            root.left = build_tree_helper(pre_start + 1, in_start, root_index - 1)
            root.right = build_tree_helper(
                pre_start + left_subtree_size + 1, root_index + 1, in_end
            )

            return root

        return build_tree_helper(0, 0, len(inorder) - 1)


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def main():
    test_cases = [
        {
            "input": [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
            "expected": [3, 9, 20, None, None, 15, 7],
            "name": "Example 1",
        },
        {"input": [[-1], [-1]], "expected": [-1], "name": "Example 2"},
    ]

    for tc in test_cases:
        preorder = tc["input"][0]
        inorder = tc["input"][1]
        result = Solution().buildTree(preorder, inorder)
        result_list = tree_to_list(result)
        status = "✓" if result_list == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: preorder = {preorder}, inorder = {inorder}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result_list}\n")


if __name__ == "__main__":
    main()
