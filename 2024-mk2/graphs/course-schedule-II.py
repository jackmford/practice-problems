
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        coursesToReqs = defaultdict(list)
        for course in prerequisites:
            coursesToReqs[course[0]].append(course[1])
        print(coursesToReqs)
        path = []

        def dfs(course):
            if course in visited:
                return False
            # Already have this course as a prereq
            if course in path:
                return True

            visited.add(course)

            for prereq in coursesToReqs[course]:
                if dfs(prereq) == False:
                    return False
            
            visited.remove(course)
            coursesToReqs.pop(course)
            path.append(course)
            return True


        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return path
