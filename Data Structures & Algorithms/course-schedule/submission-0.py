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
            if course in visited:
                return False

            if not preMap[course]: # if no pre-requisites, return
                return True

            visited.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            preMap[course] = [] # set it to empty, since we know that we've already taken the course
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
            
        
        



