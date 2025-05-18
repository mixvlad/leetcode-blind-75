from typing import List

def length_of_lis(nums: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [10, 9, 2, 5, 3, 7, 101, 18],
            "expected": 4,
            "name": "Example 1"
        },
        {
            "input": [0, 1, 0, 3, 2, 3],
            "expected": 4,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = length_of_lis(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 