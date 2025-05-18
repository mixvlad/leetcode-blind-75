from typing import List

def missing_number(nums: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [3, 0, 1],
            "expected": 2,
            "name": "Example 1"
        },
        {
            "input": [0, 1],
            "expected": 2,
            "name": "Example 2"
        },
        {
            "input": [9, 6, 4, 2, 3, 5, 7, 0, 1],
            "expected": 8,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = missing_number(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 