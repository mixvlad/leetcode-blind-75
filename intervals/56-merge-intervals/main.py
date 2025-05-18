from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[1, 3], [2, 6], [8, 10], [15, 18]],
            "expected": [[1, 6], [8, 10], [15, 18]],
            "name": "Example 1"
        },
        {
            "input": [[1, 4], [4, 5]],
            "expected": [[1, 5]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = merge(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 