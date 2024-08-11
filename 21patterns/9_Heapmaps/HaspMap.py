

def calculate_hash(key):
    key_base = 2069
    return key % key_base

def main():
    keys = [1, 2068, 2070]
    i = 0
    for key in keys:
        i+= 1
        hashed_value = calculate_hash(key)
        print(i, ".\tkey:", key)
        print("\tHashed value:", hashed_value)
        
        
class Bucket:
    def __init__(self) -> None:
        self.bucket = []
    
    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] == (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
                break
            

class DesignHashMap():
    def __init__(self):
        self.key_space = 2069
        self.bucket = [Bucket()] * self.key_space
    
    def put(self, key, value):
        hash_key = key % self.key_space
        return self.bucket[hash_key].update(key, value)
    
    def get(self, key):
        hash_key = key % self.key_space
        return self.bucket[hash_key].get(key)
    
    def remove(self, key):
        hash_key = key % self.key_space
        self.bucket[hash_key].remove(key)
        
def main():
    input_hash_map = DesignHashMap()
    keys = [5, 2069, 2070, 2073, 4138, 2068]
    keys_list = [5, 2069, 2070, 2073, 4138, 2068]
    values = [100, 200, 400, 500, 1000, 5000]
    funcs = ["Get", "Get", "Put", "Get",
             "Put", "Get", "Get", "Remove",
             "Get", "Get", "Remove", "Get"]
    func_keys = [[5], [2073], [2073, 250], [2073], 
                 [121, 110], [121], [2068], [2069], [2069],
                 [2071], [2071], [2071]]

    for i in range(len(keys)):
        input_hash_map.put(keys[i], values[i])

    for i in range(len(funcs)):
        if funcs[i] == "Put":
            print(
                i + 1,  ".\t put(", func_keys[i][0],  ", ", func_keys[i][1],  ")", sep="")
            if not func_keys[i][0] in keys_list:
                keys_list.append(func_keys[i][0])
            input_hash_map.put(func_keys[i][0], func_keys[i][1])
        elif funcs[i] == "Get":
            print(i + 1, ".\t get(", func_keys[i][0], ")", sep="")
            print("\t Value returned: ", input_hash_map.get(
                func_keys[i][0]), sep="")
        elif funcs[i] == "Remove":
            print(i + 1,  ". \t remove(", func_keys[i][0], ")", sep="")
            input_hash_map.remove(func_keys[i][0])

        print("-"*100)

if __name__ == '__main__':
    main()
    
        
        
main()