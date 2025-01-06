from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        # Step 2: Perform DFS to evaluate queries
        def dfs(start, end, visited):
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1:
                        return val * res
            return -1.0
        
        # Step 3: Evaluate each query
        result = []
        for query in queries:
            a, b = query
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(a, b, set()))
        
        return result
