class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start from the root node
        current = self.root

        # Traverse through each character in the word
        for char in word:
            # If the character is not in children, create a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the next node
            current = current.children[char]

        # Mark the end of the word
        current.is_end = True

    def search(self, word: str) -> bool:
        return self._search_helper(self.root, word, 0)

    def _search_helper(self, node: TrieNode, word: str, index: int) -> bool:
        # If we've reached the end of the word, check if it's a valid word
        if index == len(word):
            return node.is_end

        char = word[index]

        # If the current character is a wildcard
        if char == ".":
            # Try all possible children
            for child in node.children.values():
                if self._search_helper(child, word, index + 1):
                    return True
            return False

        # If the character exists in children, continue searching
        if char in node.children:
            return self._search_helper(node.children[char], word, index + 1)

        return False


def main():
    test_cases = [
        {
            "operations": [
                ("add_word", "bad"),
                ("add_word", "dad"),
                ("add_word", "mad"),
                ("search", "pad", False),
                ("search", "bad", True),
                ("search", ".ad", True),
                ("search", "b..", True),
            ],
            "name": "Example 1",
        }
    ]

    for tc in test_cases:
        wd = WordDictionary()
        print(f"Test Case: {tc['name']}")
        for op in tc["operations"]:
            if op[0] == "add_word":
                wd.addWord(op[1])
                print(f"  Added: {op[1]}")
            elif op[0] == "search":
                result = wd.search(op[1])
                expected = op[2]
                status = "✓" if result == expected else "✗"
                print(f"{status} Search: {op[1]}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        print()


if __name__ == "__main__":
    main()
