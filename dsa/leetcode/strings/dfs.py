class Search:
    
    def __init__(self, s) -> None:
        self.s = s
        
    def dfs(self): 
        visited = [False] * len(self.s)
        path = "" 
        paths = []
        def _dfs(s, path, visited):
            if len(s) == len(path):
                paths.append(path)
        
            for i, char in enumerate(s):
                if not visited[i]:
                    visited[i] = True
                    _dfs(s, path + char, visited)
                    visited[i] = False
        
        _dfs(self.s, path, visited)
        return paths
    
s = Search("sea")
print(s.dfs())