from typing import List, Dict, Set

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Builds the lexicographical order of characters in an alien language.
        
        Args:
            words: List of words in the alien language
            
        Returns:
            str: The lexicographical order of characters, or empty string if order is invalid
        """
        # Build adjacency list and in-degree count
        graph: Dict[str, Set[str]] = {c: set() for word in words for c in word}
        in_degree: Dict[str, int] = {c: 0 for c in graph}
        
        # Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Check for invalid prefix case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
                
            # Find first different character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Topological sort using DFS
        visited = set()  # All visited nodes
        temp = set()     # Nodes in current DFS path
        result = []
        
        def dfs(node: str) -> bool:
            """
            Performs DFS to detect cycles and build topological order.
            
            Args:
                node: Current character being processed
                
            Returns:
                bool: True if cycle detected, False otherwise
            """
            if node in temp:
                return True  # Cycle detected
            if node in visited:
                return False
                
            temp.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            temp.remove(node)
            visited.add(node)
            result.append(node)
            return False
        
        # Process all nodes
        for node in graph:
            if node not in visited:
                if dfs(node):
                    return ""  # Cycle detected
        
        return "".join(reversed(result))

def main():
    solution = Solution()
    test_cases = [
        {
            "input": ["wrt", "wrf", "er", "ett", "rftt"],
            "expected": "wertf",
            "name": "Example 1"
        },
        {
            "input": ["z", "x"],
            "expected": "zx",
            "name": "Example 2"
        },
        {
            "input": ["z", "x", "z"],
            "expected": "",
            "name": "Example 3 (cycle)"
        }
    ]

    for tc in test_cases:
        result = solution.foreignDictionary(tc["input"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"{status} {tc['name']}")
        print(f"  Input: words = {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got: {result}\n")

if __name__ == "__main__":
    main() 