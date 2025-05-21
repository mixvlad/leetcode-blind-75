from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determine if the string can be segmented into a space-separated sequence of dictionary words.
        
        Args:
            s: Input string to check
            wordDict: List of valid words
            
        Returns:
            bool: True if the string can be segmented, False otherwise
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always valid
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]

def main():
    solution = Solution()
    test_cases = [
        {
            "input": ["leetcode", ["leet", "code"]],
            "expected": True,
            "name": "Example 1"
        },
        {
            "input": ["applepenapple", ["apple", "pen"]],
            "expected": True,
            "name": "Example 2"
        },
        {
            "input": ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
            "expected": False,
            "name": "Example 3"
        }
    ]

    for tc in test_cases:
        s = tc["input"][0]
        word_dict = tc["input"][1]
        result = solution.wordBreak(s, word_dict)
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: s = {s}, wordDict = {word_dict}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 