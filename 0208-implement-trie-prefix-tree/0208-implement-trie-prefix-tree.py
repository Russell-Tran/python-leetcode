class Node:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {} # "c" -> c's node

class Trie:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)