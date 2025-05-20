class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
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
        # Start from the root node
        current = self.root

        # Traverse through each character in the word
        for char in word:
            # If character not found, word doesn't exist
            if char not in current.children:
                return False
            # Move to the next node
            current = current.children[char]

        # Check if we've reached the end of a word
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        current = self.root

        # Traverse through each character in the prefix
        for char in prefix:
            # If character not found, prefix doesn't exist
            if char not in current.children:
                return False
            # Move to the next node
            current = current.children[char]

        # If we've reached here, prefix exists
        return True


def main():
    test_cases = [
        {
            "operations": [
                ("insert", "apple"),
                ("search", "apple", True),
                ("search", "app", False),
                ("startsWith", "app", True),
                ("insert", "app"),
                ("search", "app", True),
            ],
            "name": "Example 1",
        }
    ]

    for tc in test_cases:
        trie = Trie()
        print(f"Test Case: {tc['name']}")
        for op in tc["operations"]:
            if op[0] == "insert":
                trie.insert(op[1])
                print(f"  Inserted: {op[1]}")
            elif op[0] == "search":
                result = trie.search(op[1])
                expected = op[2]
                status = "✓" if result == expected else "✗"
                print(f"{status} Search: {op[1]}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
            elif op[0] == "starts_with":
                result = trie.startsWith(op[1])
                expected = op[2]
                status = "✓" if result == expected else "✗"
                print(f"{status} Starts With: {op[1]}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        print()


if __name__ == "__main__":
    main()
