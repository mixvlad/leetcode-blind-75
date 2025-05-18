from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        @param: board: A 2D board of characters
        @param: words: A list of words to search for
        @return: A list of all words that can be found in the board
        """
        pass

def main():
    solution = Solution()
    
    # Test case 1
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    
    # Test case 2
    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    
    test_cases = [(board1, words1), (board2, words2)]
    
    for i, (board, words) in enumerate(test_cases, 1):
        result = solution.findWords(board, words)
        print(f"Test case {i}:")
        print(f"Board: {board}")
        print(f"Words to find: {words}")
        print(f"Found words: {result}")
        print()

if __name__ == "__main__":
    main() 