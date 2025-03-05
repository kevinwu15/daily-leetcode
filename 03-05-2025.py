class Solution:
    def coloredCells(self, n: int) -> int:
        # prev = 1
        # for i in range(2, n + 1):
        #     prev += 4 * (i - 1)
        # return prev

        return 2 * n * (n - 1) + 1