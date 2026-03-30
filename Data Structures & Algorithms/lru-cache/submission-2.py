class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        

    def get(self, key: int) -> int:
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        
        if len(self.cache)== self.cap:
            first_key = list(self.cache.keys())[0]
            del self.cache[first_key]
        self.cache[key] = value
