from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        @param: matrix: A 2D matrix of integers
        @return: None, modifies the matrix in-place
        """
        if not matrix or not matrix[0]:
            return
            
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check if first row has any zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
                
        # Check if first column has any zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
                
        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Set zeros based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Handle first row
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
                
        # Handle first column
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

def main():
    solution = Solution()
    
    # Test case 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    # Test case 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    
    test_cases = [matrix1, matrix2]
    
    for i, matrix in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        print("Original matrix:")
        for row in matrix:
            print(row)
        
        solution.setZeroes(matrix)
        
        print("\nModified matrix:")
        for row in matrix:
            print(row)
        print()

if __name__ == "__main__":
    main() 