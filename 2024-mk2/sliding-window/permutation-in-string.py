
def checkDicts(s1Map, s2Map):
    for k in s1Map.keys():
        if k not in s2Map.keys() or s1Map[k] != s2Map[k]:
            return False

    return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Need count of characters in map in s1
        if len(s1) > len(s2):
            return False

        s1Map = defaultdict(int)
        for c in s1:
            s1Map[c]+=1
        print(s1Map)

        # Create initial s2Map
        s2Map = defaultdict(int)
        for i in range(len(s1)):
            s2Map[s2[i]]+=1
        print(s2Map)

        if checkDicts(s1Map, s2Map):
            return True
        # Start adjusting window
        l, r = 0, len(s1)
        while r < len(s2):
            s2Map[s2[l]]-=1
            l+=1

            s2Map[s2[r]]+=1
            r+=1

            if checkDicts(s1Map, s2Map):
                return True
        return False

        
