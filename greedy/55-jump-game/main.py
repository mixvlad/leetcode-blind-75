from typing import List

class Solution:
    """
    Solution for the Jump Game problem.
    Given an array of non-negative integers nums, you are initially positioned at the first index.
    Each element in the array represents your maximum jump length at that position.
    Determine if you can reach the last index.
    """
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        jump_size = 0
        while i < len(nums) - 1:
            if nums[i] > jump_size:
                jump_size = nums[i]
            i += 1
            jump_size -= 1
            if jump_size < 0:
                return False
        return True

def test_solution():
    """
    Test cases for the Jump Game solution
    """
    solution = Solution()
    
    # Basic cases
    assert solution.canJump([2, 3, 1, 1, 4]) == True, "Test case 1 failed"
    assert solution.canJump([0]) == True, "Test case 2 failed"
    assert solution.canJump([1, 2, 3]) == True, "Test case 3 failed"
    
    # Impossible cases
    assert solution.canJump([3, 2, 1, 0, 4]) == False, "Test case 4 failed"
    assert solution.canJump([0, 1]) == False, "Test case 5 failed"
    
    # Edge cases
    assert solution.canJump([1]) == True, "Test case 6 failed"
    assert solution.canJump([1, 0, 1, 0]) == False, "Test case 7 failed"
    assert solution.canJump([2, 0, 0]) == True, "Test case 8 failed"
    
    # Large numbers
    assert solution.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) == True, "Test case 9 failed"
    assert solution.canJump([1, 1, 1, 1, 1]) == True, "Test case 10 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution() 