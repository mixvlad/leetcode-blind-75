from typing import List

def partition(s: str) -> List[List[str]]:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "aab",
            "expected": [["a", "a", "b"], ["aa", "b"]],
            "name": "Example 1"
        },
        {
            "input": "a",
            "expected": [["a"]],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = partition(tc["input"])
        # Sort both result and expected for comparison
        result = sorted([tuple(part) for part in result])
        expected = sorted([tuple(part) for part in tc["expected"]])
        status = "✓" if result == expected else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 