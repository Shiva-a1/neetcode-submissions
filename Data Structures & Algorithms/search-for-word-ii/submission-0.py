class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()

        def add(word):
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word
        for word in words:
            add(word)
        
        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node):
            if (r<0 or c<0 or r>=rows or c>=cols) or (r, c) in visit or board[r][c] not in node.children:
                return
            node = node.children[board[r][c]]
            if node.word:
                res.add(node.word)
            visit.add((r, c))
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root)
        return list(res)