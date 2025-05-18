from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        @param: nums: An array containing n distinct numbers in the range [0, n]
        @return: The missing number in the range
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 0, 1]
    
    # Test case 2
    nums2 = [0, 1]
    
    # Test case 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    
    test_cases = [nums1, nums2, nums3]
    
    for i, nums in enumerate(test_cases, 1):
        result = solution.missingNumber(nums)
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Missing number: {result}")
        print()

if __name__ == "__main__":
    main() 