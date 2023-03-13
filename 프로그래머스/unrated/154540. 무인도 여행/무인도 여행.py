import sys
sys.setrecursionlimit(10**5)
def solution(maps):
    answer = []
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0 for __ in range(len(maps[0]))] for __ in range(len(maps))]
    
    def dfs(x, y):
        food = int(maps[x][y])
        visited[x][y] = 1
        
        for m in move:
            dx = x + m[0]
            dy = y + m[1]
            if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]) and not visited[dx][dy]:
                if maps[dx][dy] == 'X':
                    continue
                food += dfs(dx, dy)
                
        return food
    
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(dfs(i, j))


    if answer:
        answer.sort()
        return answer
    else:
        return [-1]