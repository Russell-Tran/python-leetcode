class Node:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {} # 'c' -> c's node

class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.is_end = True

    def _search_helper(self, word, curr_node):
        if not word:
            return curr_node.is_end

        char = word[0]
        
        if char == '.':
            return any(self._search_helper(word[1:], child_node) for child_node in curr_node.children.values())

        if char not in curr_node.children:
            return False

        return self._search_helper(word[1:], curr_node.children[char])

    def search(self, word: str) -> bool:
        return self._search_helper(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)