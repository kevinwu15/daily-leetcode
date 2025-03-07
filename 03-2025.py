# Mar 5
def coloredCells(self, n: int) -> int:
    # prev = 1
    # for i in range(2, n + 1):
    #     prev += 4 * (i - 1)
    # return prev

    return 2 * n * (n - 1) + 1

# Mar 6
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

# Mar 7
def closestPrimes(self, left: int, right: int) -> List[int]:
    nums = [0 for _ in range(right + 1)]
    nums[0] = 1
    nums[1] = 1

    for i in range(2, right):
        if nums[i] == 0:
            multiple = i * 2
            while multiple <= right:
                nums[multiple] = 1
                multiple += i
    
    prev = None
    minn = float('inf')
    start = None
    for i in range(left, right + 1):
        if nums[i] == 0:
            if not prev:
                prev = i
            else:
                if i - prev < minn:
                    start = prev
                    minn = i - prev
                prev = i
        
        if minn == 2:
            return [start, start + 2]
    
    if not start:
        return [-1, -1]
    
    return [start, start + minn]