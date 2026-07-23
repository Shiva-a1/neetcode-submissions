class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        new_node = Node(homepage)
        self.curr = new_node

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        self.curr.next.prev = self.curr
        self.curr = new_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.prev: 
                return self.curr.data
            else:
                self.curr = self.curr.prev
        return self.curr.data

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.next:
                return self.curr.data
            else:
                self.curr = self.curr.next
        return self.curr.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)