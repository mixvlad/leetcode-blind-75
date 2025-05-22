from typing import List

def max_sub_array(nums: List[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray using optimized Kadane's algorithm.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of a contiguous subarray
    """
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum

def main():
    test_cases = [
        {
            "input": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            "expected": 6,
            "name": "Example 1"
        },
        {
            "input": [1],
            "expected": 1,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = max_sub_array(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 