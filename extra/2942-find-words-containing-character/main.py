from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        You are given a 0-indexed array of strings words and a character x.
        Return an array of indices representing the words that contain the character x.
        Note that the returned array may be in any order.

        Time Complexity: O(n * m), where n is the number of words and m is the average length of words
        Space Complexity: O(k), where k is the number of words containing character x

        Args:
            words: List of strings to search through
            x: Character to find in words

        Returns:
            List of indices where the character x appears in the corresponding word
        """
        return [i for i, word in enumerate(words) if x in word]


def main():
    test_cases = [
        {
            "input": [["leet", "code"], "e"],
            "expected": [0, 1],
            "name": "Example 1 - Character appears in both words"
        },
        {
            "input": [["abc", "bcd", "aaaa", "cbc"], "a"],
            "expected": [0, 2],
            "name": "Example 2 - Character appears in first and third words"
        },
        {
            "input": [["abc", "bcd", "aaaa", "cbc"], "z"],
            "expected": [],
            "name": "Example 3 - Character not found in any word"
        },
        {
            "input": [["a", "b", "c"], "a"],
            "expected": [0],
            "name": "Single character words"
        },
        {
            "input": [["aaa", "aaa", "aaa"], "a"],
            "expected": [0, 1, 2],
            "name": "All words contain the character"
        },
        {
            "input": [[], "a"],
            "expected": [],
            "name": "Empty input list"
        },
        {
            "input": [["hello", "world"], "l"],
            "expected": [0, 1],
            "name": "Character appears multiple times in words"
        }
    ]

    solution = Solution()
    for tc in test_cases:
        result = solution.findWordsContaining(tc["input"][0], tc["input"][1])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: words = {tc['input'][0]}, x = {tc['input'][1]}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")


if __name__ == "__main__":
    main() 