from typing import List

def search(nums: List[int], target: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[4, 5, 6, 7, 0, 1, 2], 0],
            "expected": 4,
            "name": "Example 1"
        },
        {
            "input": [[4, 5, 6, 7, 0, 1, 2], 3],
            "expected": -1,
            "name": "Example 2"
        },
        {
            "input": [[1], 0],
            "expected": -1,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = search(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input'][0]}, target = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 