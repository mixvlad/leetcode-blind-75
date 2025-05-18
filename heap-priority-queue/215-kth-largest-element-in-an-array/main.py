from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[3,2,1,5,6,4], 2],
            "expected": 5,
            "name": "Example 1"
        },
        {
            "input": [[3,2,3,1,2,4,5,5,6], 4],
            "expected": 4,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        nums = tc["input"][0]
        k = tc["input"][1]
        result = find_kth_largest(nums, k)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {nums}, k = {k}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 