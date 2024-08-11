class HashMap:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size
        
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k,v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    break
                else:
                    self.table[index].append((key, value))
            
    
    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k,v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    break


# Create a HashMap with a size of 10
hash_map = HashMap(10)

# Put some key-value pairs into the HashMap
hash_map.put("apple", 5)
hash_map.put("banana", 7)
hash_map.put("orange", 3)
hash_map.put("apple", 10)  # Update the value for the key "apple"

# Get values from the HashMap
print(hash_map.get("apple"))  # Output: 10
print(hash_map.get("banana"))  # Output: 7
print(hash_map.get("grape"))  # Output: None (key not found)

# Remove a key-value pair from the HashMap
hash_map.remove("banana")

# Try to get the removed key
print(hash_map.get("banana"))  # Output: None (key not found)

# Try to get the updated key
print(hash_map.get("apple"))  # Output: 10