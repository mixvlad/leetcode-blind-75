from typing import List

def rob(nums: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [2, 3, 2],
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": [1, 2, 3, 1],
            "expected": 4,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = rob(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 