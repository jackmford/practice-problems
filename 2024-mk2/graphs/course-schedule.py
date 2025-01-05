class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS cycle detection
        classes = defaultdict(list)
        for pre in prerequisites:
            classes[pre[0]].append(pre[1])

        print(classes)

        visited = set()
        def dfs(class_):
            # Cycle - class that requires this class but also has this class as a requirement
            if class_ in visited:
                return False
            # No requirements, return True
            if class_ not in classes:
                return True
            
            
            visited.add(class_)
            # Checking requirements recursively 
            for req in classes[class_]:
                if dfs(req) == False:
                    return False

            # We have checked all requirements and found we *can* take this class
            # No need to check it anymore if it is a req for others
            visited.remove(class_)
            classes.pop(class_)

            return True

        
        # For every class, check if there is a cyclical req
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True

