class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def helper(i, node):
            curr = node
            for j in range(i, len(word)):
                c = word[j]
                if c=='.':
                    for child in curr.children.values():
                        if helper(j+1, child):
                            return True
                    return False
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.word
        return helper(0, self.root)
