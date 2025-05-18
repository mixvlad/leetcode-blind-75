from typing import List

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [1, 2, 2],
            "expected": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
            "name": "Example 1"
        },
        {
            "input": [0],
            "expected": [[], [0]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = subsets_with_dup(tc["input"])
        # Sort both result and expected for comparison
        result = sorted([sorted(subset) for subset in result])
        expected = sorted([sorted(subset) for subset in tc["expected"]])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 