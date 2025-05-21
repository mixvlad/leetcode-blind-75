from typing import List

def rob(nums: List[int]) -> int:
    """
    Find the maximum amount of money that can be robbed from houses.
    
    Args:
        nums: List of integers representing money in each house
        
    Returns:
        Maximum amount that can be robbed
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # dp[i] represents the maximum amount that can be robbed up to house i
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # For each house, we can either:
    # 1. Rob current house + max amount from 2 houses back
    # 2. Skip current house and take max amount from previous house
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

def main():
    test_cases = [
        {
            "input": [1, 2, 3, 1],
            "expected": 4,
            "name": "Example 1"
        },
        {
            "input": [2, 7, 9, 3, 1],
            "expected": 12,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = rob(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 