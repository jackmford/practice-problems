"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""

class MyHashMap:

    def __init__(self):
        self.hashmap = []
        

    def put(self, key: int, value: int) -> None:
        for kv in self.hashmap:
            if key == kv[0]:
                kv[1] = value
                return
        self.hashmap.append([key, value])
        

    def get(self, key: int) -> int:
        for k in self.hashmap:
            if k[0] == key:
                return k[1]
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
myHashMap = MyHashMap();
print(myHashMap.put(1, 1)); ## The map is now [[1,1]]
print(myHashMap.put(2, 2)); ## The map is now [[1,1], [2,2]]
print(myHashMap.get(1));    ## return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3));    ## return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(myHashMap.put(2, 1)); ## The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2));    ## return 1, The map is now [[1,1], [2,1]]
print(myHashMap.remove(2)); ## remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2));    ## return -1 (i.e., not found), The map is now [[1,1]]
