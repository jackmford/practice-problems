class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Dictionary of 
        # {classes: prereqs}
        # If any class has a prereq that itself is a prereq for, false

        classes = {}
        for courses in prerequisites:
            p = classes.get(courses[0], [])
            p.append(courses[1])
            classes[courses[0]] = p

        visited = set()
        
        # This is cycle detection
        # Check if there is a cycle for every class
        def dfs(course):
            # Already saw this class, cycle
            if course in visited:
                return False
            # No prerequisite, it is good
            if course not in classes.keys():
                return True

            visited.add(course)
            # For every prereq on the course,
            # check validity
            for pre in classes[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)
            # This course is good, don't need to check it anymore
            classes.pop(course)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True
        
