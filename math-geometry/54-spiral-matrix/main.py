from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Traverse the matrix in spiral order starting from top-left corner.
    
    Args:
        matrix: 2D list of integers
        
    Returns:
        List of integers in spiral order
    """
    if not matrix or not matrix[0]:
        return []
        
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

def main():
    test_cases = [
        {
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
            "name": "Example 1"
        },
        {
            "input": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        result = spiral_order(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: matrix = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 