class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Find the length of the longest common subsequence between two strings.
        
        Args:
            text1 (str): First input string
            text2 (str): Second input string
            
        Returns:
            int: Length of the longest common subsequence
        """
        # Create a 2D DP table with dimensions (len(text1) + 1) x (len(text2) + 1)
        # dp[i][j] represents the length of LCS of text1[0:i] and text2[0:j]
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Fill the DP table
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    # If characters match, add 1 to the previous diagonal value
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # If characters don't match, take maximum of left or top value
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # The bottom-right cell contains the length of LCS
        return dp[len(text1)][len(text2)]

def main():
    solution = Solution()
    test_cases = [
        {
            "input": ["abcde", "ace"],
            "expected": 3,
            "name": "Example 1"
        },
        {
            "input": ["abc", "abc"],
            "expected": 3,
            "name": "Example 2"
        }
    ]

    for tc in test_cases:
        text1 = tc["input"][0]
        text2 = tc["input"][1]
        result = solution.longestCommonSubsequence(text1, text2)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: text1 = {text1}, text2 = {text2}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 