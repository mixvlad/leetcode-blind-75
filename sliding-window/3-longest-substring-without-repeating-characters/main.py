from typing import List

def length_of_longest_substring(s: str) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "abcabcbb",
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": "bbbbb",
            "expected": 1,
            "name": "Example 2"
        },
        {
            "input": "pwwkew",
            "expected": 3,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = length_of_longest_substring(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 