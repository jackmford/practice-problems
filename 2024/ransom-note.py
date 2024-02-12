class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m1, m2 = {}, {}
        for char in ransomNote:
            if char in m1:
                m1[char] += 1
            else:
                m1[char] = 1
        
        for char in magazine:
            if char in m2:
                m2[char] += 1
            else:
                m2[char] = 1
        
        for char in ransomNote:
            if char not in magazine:
                return False
            if m2[char] < m1[char]:
                return False
        
        return True