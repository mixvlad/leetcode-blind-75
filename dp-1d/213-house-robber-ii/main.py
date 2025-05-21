from typing import List

class Solution:
    def _rob_linear(self, nums: List[int], start: int, end: int) -> int:
        """
        Helper function to rob houses in a linear arrangement
        Uses O(1) space instead of O(n)
        """
        if start >= end:
            return 0
        
        prev2 = 0  # max amount from 2 houses back
        prev1 = nums[start]  # max amount from previous house
        
        for i in range(start + 1, end):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1

    def rob(self, nums: List[int]) -> int:
        """
        Main function to rob houses arranged in a circle
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Case 1: Rob all houses except the first one
        case1 = self._rob_linear(nums, 1, len(nums))
        
        # Case 2: Rob all houses except the last one
        case2 = self._rob_linear(nums, 0, len(nums) - 1)
        
        return max(case1, case2)

def main():
    solution = Solution()
    test_cases = [
        {
            "input": [2, 3, 2],
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": [1, 2, 3, 1],
            "expected": 4,
            "name": "Example 2"
        },
        {
            "input": [1, 2, 3],
            "expected": 3,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        result = solution.rob(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 