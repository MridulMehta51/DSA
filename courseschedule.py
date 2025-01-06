from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create graph with defaultdict of lists
        graph = defaultdict(list)
        
        for prereq in prerequisites:
            a, b = prereq  # `a` needs `b` as a prerequisite
            graph[a].append(b)
        
        result = []
        
        # Track the state of each course during DFS
        # 0: unvisited, 1: visiting (in recursion stack), 2: visited (safe)
        state = [0] * numCourses

        # DFS function to detect cycles
        def dfs(course):
            if state[course] == 1:  # cycle detected
                return False
            if state[course] == 2:  # already visited, no cycle from this course
                return True
            
            # Mark the course as visiting (in the current DFS stack)
            state[course] = 1
            
            # Visit all prerequisites (neighbors)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            # Mark the course as visited (all its prerequisites are processed)
            state[course] = 2
            return True
        
        # Try to visit each course
        for course in range(numCourses):
            if state[course] == 0:  # unvisited
                if not dfs(course):
                    return False
        
        return True
