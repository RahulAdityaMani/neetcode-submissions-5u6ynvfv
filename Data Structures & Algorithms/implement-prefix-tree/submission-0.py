class PrefixTree:

    def __init__(self):
        self.root = {}, False

    def insert(self, word: str) -> None:
        curr = self.root
        children, isEnd = curr
        for i, c in enumerate(word):
            if c not in children:
                children[c] = {}, False
            if len(word) - i <= 1:
                children_dict, _ = children[c]
                children[c] = children_dict, True
            children, isEnd = children[c]

    def search(self, word: str) -> bool:
        curr = self.root
        children, isEnd = curr
        for c in word:
            if c not in children:
                return False
            children, isEnd = children[c]
        return isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        children, isEnd = curr
        for c in prefix:
            if c not in children:
                return False
            children, isEnd = children[c]
        return True
        