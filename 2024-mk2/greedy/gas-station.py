# brute force O(n^2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def find(start):
            save = start
            visited =0
            curGas = 0
    
            while visited != len(gas):
                # Fill up where we are
                curGas += gas[start]
    
                # Travel if we can
                if curGas >= cost[start]:
                    curGas -= cost[start]
                else:
                    return False, 0
    
                if start+1 < len(cost):
                    start = start+1
                else:
                    start = 0
    
                visited += 1
            return True, save

        for i in range(len(cost)):
            tf, r = find(i)
            if tf != False:
                return r
            
        return -1
