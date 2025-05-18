from typing import List

def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[10, 1, 2, 7, 6, 1, 5], 8],
            "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            "name": "Example 1"
        },
        {
            "input": [[2, 5, 2, 1, 2], 5],
            "expected": [[1, 2, 2], [5]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        candidates = tc["input"][0]
        target = tc["input"][1]
        result = combination_sum2(candidates, target)
        # Sort both result and expected for comparison
        result = sorted([sorted(combination) for combination in result])
        expected = sorted([sorted(combination) for combination in tc["expected"]])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: candidates = {candidates}, target = {target}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 