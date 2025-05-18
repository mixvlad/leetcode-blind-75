def longest_palindrome(s: str) -> str:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": "babad",
            "expected": "bab",
            "name": "Example 1"
        },
        {
            "input": "cbbd",
            "expected": "bb",
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = longest_palindrome(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 