class PrefixTree:

    class PrefixTreeNode:
        
        def __init__(self):
            self.children = [0] * 26
            self.is_end = False

    def __init__(self):
       self.root = self.PrefixTreeNode() 

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            key = ord(c) - ord('a')
            if curr.children[key] == 0:
                curr.children[key] = self.PrefixTreeNode()
            curr = curr.children[key]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            key = ord(c) - ord('a')
            if curr.children[key] == 0:
                return False
            curr = curr.children[key]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            key = ord(c) - ord('a')
            if curr.children[key] == 0:
                return False
            curr = curr.children[key]
        return True
        