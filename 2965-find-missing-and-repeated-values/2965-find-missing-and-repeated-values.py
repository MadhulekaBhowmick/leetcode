class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        
        repeated = 0
        actual_sum = 0

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                actual_sum += num

                if num in seen:
                    repeated = num
                else:
                    seen.add(num)
        expected_sum = (n*n) * (n*n+1) // 2
        missing = expected_sum + repeated - actual_sum

        return[repeated, missing]