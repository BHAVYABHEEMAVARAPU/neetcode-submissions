class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl=len(matrix)
        cl=len(matrix[0])
        for i in range(0,rl):
            for j in range(0,cl):
                if matrix[i][j]==target:
                    return True
        return False
        