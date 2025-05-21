from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Find the minimum number of coins needed to make up the given amount using dynamic programming.
        
        Args:
            coins: List of available coin denominations
            amount: Target amount to make up
            
        Returns:
            Minimum number of coins needed, or -1 if impossible
        """
        # Initialize dp array with amount + 1 (which is greater than any possible answer)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):
            # Try each coin denomination
            for coin in coins:
                if coin <= i:  # Only consider coins that are not larger than current amount
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return -1 if amount cannot be made up, otherwise return the minimum number of coins
        return dp[amount] if dp[amount] <= amount else -1

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
            "name": "Example 2 - Impossible amount"
        },
        {
            "input": [[1, 2, 5], 28],
            "expected": 7,
            "name": "Example 3 - Large amount"
        },
        {
            "input": [[1, 3, 4], 6],
            "expected": 2,
            "name": "Example 4"
        },
        {
            "input": [[1, 4, 5], 8],
            "expected": 2,
            "name": "Example 5"
        },
        {
            "input": [[1, 2147483647], 2],
            "expected": 2,
            "name": "Example 6 - Large coin value"
        }
    ]

    solution = Solution()
    for tc in test_cases:
        coins = tc["input"][0]
        amount = tc["input"][1]
        result = solution.coinChange(coins, amount)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: coins = {coins}, amount = {amount}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 