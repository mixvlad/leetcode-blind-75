from typing import List

def max_product(nums: List[int]) -> int:
    """
    Find the maximum product of a contiguous subarray.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum product of a contiguous subarray
    """
    if not nums:
        return 0
        
    # Initialize variables to track max and min products
    max_so_far = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]
    
    # Iterate through array starting from second element
    for num in nums[1:]:
        # Store current max before updating
        temp_max = curr_max
        
        # Update current max and min
        curr_max = max(num, num * curr_max, num * curr_min)
        curr_min = min(num, num * temp_max, num * curr_min)
        
        # Update global maximum
        max_so_far = max(max_so_far, curr_max)
    
    return max_so_far

def main():
    test_cases = [
        {
            "input": [2, 3, -2, 4],
            "expected": 6,
            "name": "Example 1"
        },
        {
            "input": [-2, 0, -1],
            "expected": 0,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = max_product(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 