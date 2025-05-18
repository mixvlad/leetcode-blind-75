from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED"
            ],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "SEE"
            ],
            "expected": True,
            "name": "Example 2"
        },
        {
            "input": [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB"
            ],
            "expected": False,
            "name": "Example 3"
        }
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