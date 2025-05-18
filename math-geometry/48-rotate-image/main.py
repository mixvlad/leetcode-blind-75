from typing import List

def rotate(matrix: List[List[int]]) -> None:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
            "name": "Example 1"
        },
        {
            "input": [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            "expected": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        matrix = [row[:] for row in tc["input"]]  # Create a deep copy
        rotate(matrix)
        status = "✓" if matrix == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: matrix = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {matrix}\n")

if __name__ == "__main__":
    main() 