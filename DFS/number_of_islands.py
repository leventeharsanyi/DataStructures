grid = [
    [1,1,0,0,0],
    [1,1,1,0,0],
    [0,0,1,1,0],
    [0,0,0,1,1],
    [0,0,0,0,1]
]

max_col = len(grid[0])
max_row = len(grid)

def get_neighbors(coordinate:tuple[int,int]) -> list[tuple[int,int]]:
    x,y = coordinate
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    neighbors = []
    for dx, dy in directions:
        x += dx
        y += dy
        if 0 <= x < max_col and 0 <= y < max_row:
            if grid[x][y] == 1:
                neighbors.append((x,y))
    return neighbors

def dfs(coordinate: tuple[int,int]) -> None:
    x,y = coordinate
    grid[x][y] = 0
    for neighbor in get_neighbors((x,y)):
        dfs(neighbor)

if __name__ == "__main__":
    count = 0
    for i in range(max_row):
        for j in range(max_col):
            if grid[i][j] == 1:
                dfs((i,j))
                count += 1
    print(f"The number of islands is: {count}")