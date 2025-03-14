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

# Mar 12
def maximumCount(self, nums: List[int]) -> int:
    negative = 0
    positive = 0
    # find last negative occurence
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if middle == 0:
            if nums[0] < 0:
                negative = 1
            else:
                negative = 0
            break

        if middle == len(nums) - 1:
            if nums[-1] < 0:
                negative = len(nums)
            else:
                negative = len(nums) - 1
            break

        if nums[middle - 1] < 0 and nums[middle] < 0 and nums[middle + 1] >= 0:
            negative = middle + 1
            break
        
        if nums[middle] >= 0:
            right = middle - 1
        else:
            left = middle + 1
        
    # find first positive occurence
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if middle == 0:
            if nums[0] > 0:
                positive = len(nums)
            else:
                positive = len(nums) - 1
            break

        if middle == len(nums) - 1:
            if nums[-1] > 0:
                positive = 1
            else:
                positive = 0
            break

        if nums[middle - 1] <= 0 and nums[middle] > 0 and nums[middle + 1] > 0:
            positive = len(nums) - middle
            break
        
        if nums[middle] <= 0:
            left = middle + 1
        else:
            right = middle - 1
    
    return max(positive, negative)

# Mar 14
def maximumCandies(self, candies: List[int], k: int) -> int:
    left = 1
    right = max(candies)
    maxx = 0

    while left <= right:
        curr = 0
        middle = (left + right) // 2
        for candy in candies:
            curr += (candy // middle)
        if curr >= k:
            maxx = max(middle, maxx)
            left = middle + 1
        else:
            right = middle - 1
    
    return maxx