from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return "[" + ",".join(result) + "]"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None

        values = data[1:-1].split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if index < len(values):
                if values[index] != "null":
                    node.left = TreeNode(int(values[index]))
                    queue.append(node.left)
                index += 1

                if index < len(values):
                    if values[index] != "null":
                        node.right = TreeNode(int(values[index]))
                        queue.append(node.right)
                    index += 1

        return root


def main():
    codec = Codec()

    # Test case 1: [1,2,3,null,null,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)

    # Test case 2: []
    root2 = None

    test_cases = [root1, root2]

    for i, root in enumerate(test_cases, 1):
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        print(f"Test case {i}:")
        print(f"Original tree: {root.val if root else None}")
        print(f"Serialized: {serialized}")
        print(f"Deserialized: {deserialized.val if deserialized else None}")
        print()


if __name__ == "__main__":
    main()
