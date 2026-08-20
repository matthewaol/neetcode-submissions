class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        # prepopulate the courses at its prerequisites
        for course, prereq in prerequisites:
            if course not in preMap:
                preMap[course] = []
            preMap[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited: # if we've taken this course already, cycle
                return False
            
            if preMap[course] == []: # if we've already taken all of the prereqs
                return True
            
            visited.add(course)
            
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            preMap[course] = []

            return True

        for i in range(numCourses): 
            if not dfs(i):
                return False
        
        return True