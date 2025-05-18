from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # TODO: Implement your solution here
    pass

def main():
    test_cases = [
        {
            "input": [[1, 2, 5], 11],
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": [[2], 3],
            "expected": -1,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        coins = tc["input"][0]
        amount = tc["input"][1]
        result = coin_change(coins, amount)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: coins = {coins}, amount = {amount}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 