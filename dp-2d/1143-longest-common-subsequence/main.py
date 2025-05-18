def longest_common_subsequence(text1: str, text2: str) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": ["abcde", "ace"],
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": ["abc", "abc"],
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        text1 = tc["input"][0]
        text2 = tc["input"][1]
        result = longest_common_subsequence(text1, text2)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: text1 = {text1}, text2 = {text2}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 