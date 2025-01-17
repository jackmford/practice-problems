"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""

class MyHashSet:

    def __init__(self):
        self.hashset = []
        

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)
        

    def remove(self, key: int) -> None:
        for i in range(len(self.hashset)):
            if self.hashset[i] == key:
                self.hashset.pop(i)
                return

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
myHashSet = MyHashSet();
myHashSet.add(1);      ## set = [1]
myHashSet.add(2);      ## set = [1, 2]
myHashSet.contains(1); ## return True
myHashSet.contains(3); ## return False, (not found)
myHashSet.add(2);      ## set = [1, 2]
myHashSet.contains(2); ## return True
myHashSet.remove(2);   ## set = [1]
myHashSet.contains(2); ## return False, (already removed)
