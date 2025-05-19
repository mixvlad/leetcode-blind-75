from typing import List

def is_palindrome(s: str) -> bool:
    if not s:
        return True
    lens = len(s)
    j = lens - 1
    for i in range(lens):
        while not s[j].isalnum() and j >= 0:
            j -= 1
        if not s[i].isalnum():
            continue
        if j < 0 or s[i].lower() != s[j].lower():
            return False
        j -= 1
    while not s[j].isalnum() and j >= 0:
        j -= 1
    return (True if j == -1 else False)

def main():
    test_cases = [
        {
            "input": "A man, a plan, a canal: Panama",
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": "race a car",
            "expected": False,
            "name": "Example 2"
        },
        {
            "input": " ",
            "expected": True,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = is_palindrome(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 