from typing import List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    visited = {}

    def dfs(node):
        if not node:
            return None
        if node.val in visited:
            return visited[node.val]

        clone = Node(node.val)
        visited[node.val] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


def create_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None

    # Create all nodes first
    nodes = {}
    for i in range(1, len(adj_list) + 1):
        nodes[i] = Node(i)

    # Connect nodes
    for i, neighbors in enumerate(adj_list, 1):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor])

    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []

    # Find all nodes using BFS
    nodes = {}
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current.val not in nodes:
            nodes[current.val] = current
            for neighbor in current.neighbors:
                if neighbor.val not in nodes:
                    queue.append(neighbor)

    # Create adjacency list
    adj_list = []
    for i in range(1, len(nodes) + 1):
        adj_list.append([n.val for n in nodes[i].neighbors])

    return adj_list


def main():
    test_cases = [
        {
            "input": [[2, 4], [1, 3], [2, 4], [1, 3]],
            "expected": [[2, 4], [1, 3], [2, 4], [1, 3]],
            "name": "Example 1",
        },
        {"input": [[]], "expected": [[]], "name": "Example 2"},
        {"input": [], "expected": [], "name": "Example 3"},
    ]

    for tc in test_cases:
        input_graph = create_graph(tc["input"])
        result = clone_graph(input_graph)
        result_adj_list = graph_to_adj_list(result)
        status = "✓" if result_adj_list == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: adjList = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result_adj_list}\n")


if __name__ == "__main__":
    main()
