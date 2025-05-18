def climb_stairs(n: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": 2,
            "expected": 2,
            "name": "Example 1"
        },
        {
            "input": 3,
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = climb_stairs(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: n = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 