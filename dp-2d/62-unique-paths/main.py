def unique_paths(m: int, n: int) -> int:
    """
    Calculate the number of unique paths from top-left to bottom-right in a m x n grid.
    Optimized version using a single array.
    
    Args:
        m (int): Number of rows
        n (int): Number of columns
        
    Returns:
        int: Number of unique paths
    """
    # Initialize array with 1s
    dp = [1] * n
    
    # Update array for each row
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[-1]

def main():
    test_cases = [
        {
            "input": [3, 7],
            "expected": 28,
            "name": "Example 1"
        },
        {
            "input": [3, 2],
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        m = tc["input"][0]
        n = tc["input"][1]
        result = unique_paths(m, n)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: m = {m}, n = {n}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 