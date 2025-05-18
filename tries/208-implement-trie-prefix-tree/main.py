class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # TODO: Implement your solution here
        pass

    def search(self, word: str) -> bool:
        # TODO: Implement your solution here
        pass

    def starts_with(self, prefix: str) -> bool:
        # TODO: Implement your solution here
        pass

def main():
    test_cases = [
        {
            "operations": [
                ("insert", "apple"),
                ("search", "apple", True),
                ("search", "app", False),
                ("starts_with", "app", True),
                ("insert", "app"),
                ("search", "app", True)
            ],
            "name": "Example 1"
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
                result = trie.starts_with(op[1])
                expected = op[2]
                status = "✓" if result == expected else "✗"
                print(f"{status} Starts With: {op[1]}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        print()

if __name__ == "__main__":
    main() 