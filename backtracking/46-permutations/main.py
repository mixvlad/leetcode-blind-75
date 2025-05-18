from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [1, 2, 3],
            "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            "name": "Example 1"
        },
        {
            "input": [0, 1],
            "expected": [[0, 1], [1, 0]],
            "name": "Example 2"
        },
        {
            "input": [1],
            "expected": [[1]],
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = permute(tc["input"])
        # Sort both result and expected for comparison
        result = sorted([tuple(perm) for perm in result])
        expected = sorted([tuple(perm) for perm in tc["expected"]])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 