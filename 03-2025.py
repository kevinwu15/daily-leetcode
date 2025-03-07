# Mar 4
def coloredCells(self, n: int) -> int:
    # prev = 1
    # for i in range(2, n + 1):
    #     prev += 4 * (i - 1)
    # return prev

    return 2 * n * (n - 1) + 1

# Mar 5
def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    n = len(grid)
    s = set()
    duplicate = None
    summ = 0
    for y in range(n):
        for x in range(n):
            if grid[y][x] not in s:
                s.add(grid[y][x])
            else:
                duplicate = grid[y][x]
            summ += grid[y][x]
    
    missing = (n*n * (n*n + 1) // 2) - summ + duplicate
    return [duplicate, missing]