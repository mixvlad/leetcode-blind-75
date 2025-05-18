from typing import List

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[[1, 3], [6, 9]], [2, 5]],
            "expected": [[1, 5], [6, 9]],
            "name": "Example 1"
        },
        {
            "input": [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]],
            "expected": [[1, 2], [3, 10], [12, 16]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        intervals = tc["input"][0]
        new_interval = tc["input"][1]
        result = insert(intervals, new_interval)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: intervals = {intervals}, newInterval = {new_interval}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 