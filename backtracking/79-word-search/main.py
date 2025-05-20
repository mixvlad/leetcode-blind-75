from typing import List, Set, Tuple


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    # Quick check: if word is longer than total cells
    if len(word) > rows * cols:
        return False

    # Pre-check: verify all characters exist in board
    board_chars = set()
    for row in board:
        board_chars.update(row)
    if not all(char in board_chars for char in word):
        return False

    def dfs(r: int, c: int, word_idx: int, visited: Set[Tuple[int, int]]) -> bool:
        # Base case: found the word
        if word_idx == len(word):
            return True

        # Check boundaries and if current cell matches
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or (r, c) in visited
            or board[r][c] != word[word_idx]
        ):
            return False

        visited.add((r, c))

        # Try directions in order: right, down, left, up
        # This order often finds solutions faster for left-to-right languages
        result = (
            dfs(r, c + 1, word_idx + 1, visited)
            or dfs(r + 1, c, word_idx + 1, visited)
            or dfs(r, c - 1, word_idx + 1, visited)
            or dfs(r - 1, c, word_idx + 1, visited)
        )

        visited.remove((r, c))
        return result

    # Start from cells that match first letter
    first_char = word[0]
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == first_char and dfs(r, c, 0, set()):
                return True
    return False


def main():
    test_cases = [
        {
            "input": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
            ],
            "expected": True,
            "name": "Example 1",
        },
        {
            "input": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "SEE",
            ],
            "expected": True,
            "name": "Example 2",
        },
        {
            "input": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
            ],
            "expected": False,
            "name": "Example 3",
        },
    ]

    for tc in test_cases:
        board = tc["input"][0]
        word = tc["input"][1]
        result = exist(board, word)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: board = {board}, word = {word}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main()
