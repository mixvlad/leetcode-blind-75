class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Calculate the number of ways to decode a string of digits.
        
        Args:
            s (str): Input string containing only digits
            
        Returns:
            int: Number of ways to decode the string
        """
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            # Check if current digit is valid
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
            # Check if two digits form a valid number
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]

def main():
    solution = Solution()
    test_cases = [
        {
            "input": "12",
            "expected": 2,
            "name": "Example 1"
        },
        {
            "input": "226",
            "expected": 3,
            "name": "Example 2"
        },
        {
            "input": "0",
            "expected": 0,
            "name": "Invalid: Single zero"
        },
        {
            "input": "06",
            "expected": 0,
            "name": "Invalid: Leading zero"
        },
        {
            "input": "27",
            "expected": 1,
            "name": "Valid: Two digits > 26"
        },
        {
            "input": "100",
            "expected": 0,
            "name": "Invalid: Contains zero"
        },
        {
            "input": "63000456",
            "expected": 0,
            "name": "Complex invalid case"
        }
    ]

    for tc in test_cases:
        result = solution.numDecodings(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 