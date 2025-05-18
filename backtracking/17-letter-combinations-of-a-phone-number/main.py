from typing import List

def letter_combinations(digits: str) -> List[str]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "23",
            "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            "name": "Example 1"
        },
        {
            "input": "",
            "expected": [],
            "name": "Example 2"
        },
        {
            "input": "2",
            "expected": ["a", "b", "c"],
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = letter_combinations(tc["input"])
        # Sort both result and expected for comparison
        result = sorted(result)
        expected = sorted(tc["expected"])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: digits = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 