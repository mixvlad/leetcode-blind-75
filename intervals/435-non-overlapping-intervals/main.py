from typing import List

def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[1, 2], [2, 3], [3, 4], [1, 3]],
            "expected": 1,
            "name": "Example 1"
        },
        {
            "input": [[1, 2], [1, 2], [1, 2]],
            "expected": 2,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = erase_overlap_intervals(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 