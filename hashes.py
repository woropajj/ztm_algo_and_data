

class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if self.data[address] is None:
            return "Y'all crazy!"
        else:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]

    def keys(self):
        keys = []
        for bucket in self.data:
            if bucket is not None:
                for key in bucket:
                    keys.append(key[0])
        return keys


myHashTable = HashTable(200)
myHashTable.set("grapes", 10000)
myHashTable.set("apples", 42)
print(myHashTable.get("grapess"))
print(myHashTable.keys())
