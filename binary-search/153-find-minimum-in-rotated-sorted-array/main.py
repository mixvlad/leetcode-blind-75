from typing import List

def find_min(nums: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [3, 4, 5, 1, 2],
            "expected": 1,
            "name": "Example 1"
        },
        {
            "input": [4, 5, 6, 7, 0, 1, 2],
            "expected": 0,
            "name": "Example 2"
        },
        {
            "input": [11, 13, 15, 17],
            "expected": 11,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = find_min(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 