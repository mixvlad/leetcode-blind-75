from typing import Dict, List, Set, Tuple


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_word: bool = False
        self.word: str = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []

        rows, cols = len(board), len(board[0])
        result: Set[str] = set()

        # Pre-check: verify all characters exist in board
        board_chars = set()
        for row in board:
            board_chars.update(row)

        # Filter out words that can't be formed
        valid_words = [
            word for word in words if all(char in board_chars for char in word)
        ]

        # Build Trie only with valid words
        trie = Trie()
        for word in valid_words:
            trie.insert(word)

        # Cache for visited cells during DFS
        visited: Set[Tuple[int, int]] = set()

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]

            if node.is_word:
                result.add(node.word)

            # Try all four directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc, node)

            visited.remove((r, c))

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root)

        return list(result)


def main():
    solution = Solution()

    test_cases = [
        {
            "name": "Basic test case",
            "board": [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            "words": ["oath", "pea", "eat", "rain"],
            "expected": ["eat", "oath"],
        },
        {
            "name": "No words found",
            "board": [["a", "b"], ["c", "d"]],
            "words": ["abcb"],
            "expected": [],
        },
        {
            "name": "Single character board",
            "board": [["a"]],
            "words": ["a", "b"],
            "expected": ["a"],
        },
        {
            "name": "Complex case with overlapping words",
            "board": [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
            "words": ["abc", "def", "ghi", "aei", "ceg", "adg", "beh", "cfi"],
            "expected": ["abc", "def", "ghi", "aei", "ceg", "adg", "beh", "cfi"],
        },
        {"name": "Empty board", "board": [], "words": ["test"], "expected": []},
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case['name']}")
        print("-" * 50)
        print(f"Board: {test_case['board']}")
        print(f"Words to find: {test_case['words']}")

        result = solution.findWords(test_case["board"], test_case["words"])
        expected = set(test_case["expected"])
        actual = set(result)

        print(f"Expected words: {sorted(expected)}")
        print(f"Found words: {sorted(actual)}")

        if expected == actual:
            print("✅ Test PASSED")
        else:
            print("❌ Test FAILED")
            if expected - actual:
                print(f"Missing words: {sorted(expected - actual)}")
            if actual - expected:
                print(f"Extra words: {sorted(actual - expected)}")
        print("-" * 50)


if __name__ == "__main__":
    main()
