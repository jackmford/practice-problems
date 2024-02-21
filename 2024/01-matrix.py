class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        q = []
        for i in range(height):
            for j in range(width):
                if mat[i][j] != 0:
                    mat[i][j] = ''
                else:
                    q.append((i, j))
        
        while q:
            i, j = q.pop(0)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= i+dx < height and 0 <= j+dy < width and (i+dx, j+dy):
                    if mat[i+dx][j+dy] == '':
                        mat[i+dx][j+dy] = mat[i][j] + 1
                        q.append((i+dx, j+dy))
                
        
        return mat