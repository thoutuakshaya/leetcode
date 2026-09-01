class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word):
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()

            node = node.children[ch]

        node.isEnd = True

    def search(self, word):
        node = self

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.isEnd

    def startsWith(self, prefix):
        node = self

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True