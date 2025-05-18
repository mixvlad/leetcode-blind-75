from typing import List

def max_sub_array(nums: List[int]) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            "expected": 6,
            "name": "Example 1"
        },
        {
            "input": [1],
            "expected": 1,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = max_sub_array(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 