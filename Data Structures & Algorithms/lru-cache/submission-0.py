class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.c = capacity
        self.use = []

    def get(self, key: int) -> int:
        if key in self.dic:
            self.use.remove(key)
            self.use.append(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.use.remove(key)
            self.use.append(key)
        else:
            self.use.append(key)
        self.dic[key] = value
        if len(self.dic) > self.c:
            del self.dic[self.use[0]]
            del self.use[0]

