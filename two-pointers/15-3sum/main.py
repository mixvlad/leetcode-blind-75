from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]],
            "name": "Example 1"
        },
        {
            "input": [],
            "expected": [],
            "name": "Example 2"
        },
        {
            "input": [0],
            "expected": [],
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = three_sum(tc["input"])
        # Sort both result and expected for comparison
        result = sorted([sorted(x) for x in result])
        expected = sorted([sorted(x) for x in tc["expected"]])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 