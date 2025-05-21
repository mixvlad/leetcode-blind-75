from typing import List
import bisect

def length_of_lis(nums: List[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence using binary search.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    # sub[i] represents the smallest possible tail value for all increasing subsequences
    # of length i + 1
    sub = []
    
    for num in nums:
        # Find the first element in sub that is greater than or equal to num
        i = bisect.bisect_left(sub, num)
        
        # If num is greater than all elements in sub, append it
        if i == len(sub):
            sub.append(num)
        # Otherwise, replace the first element that is greater than or equal to num
        else:
            sub[i] = num
    
    return len(sub)

def main():
    test_cases = [
        {
            "input": [10, 9, 2, 5, 3, 7, 101, 18],
            "expected": 4,
            "name": "Example 1"
        },
        {
            "input": [0, 1, 0, 3, 2, 3],
            "expected": 4,
            "name": "Example 2"
        },
        {
            "input": [10, 9, 2, 5, 3, 7, 101, 4, 6],
            "expected": 4,
            "name": "Example 3"
        },
        {
            "input": [10, 9, 2, 5, 3, 7, 101, 4, 6, 9],
            "expected": 5,
            "name": "Example 4"
        },
        {
            "input": [10, 9, 2, 5, 3, 7, 101, 4],
            "expected": 4,
            "name": "Example 5"
        }
    ]

    for tc in test_cases:
        result = length_of_lis(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: nums = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 