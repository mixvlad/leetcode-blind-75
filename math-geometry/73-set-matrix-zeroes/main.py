from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            "name": "Example 1"
        },
        {
            "input": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        matrix = [row[:] for row in tc["input"]]  # Create a deep copy
        set_zeroes(matrix)
        status = "✓" if matrix == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: matrix = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {matrix}\n")

if __name__ == "__main__":
    main() 