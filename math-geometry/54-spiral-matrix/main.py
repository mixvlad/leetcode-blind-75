from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
            "name": "Example 1"
        },
        {
            "input": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = spiral_order(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: matrix = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 