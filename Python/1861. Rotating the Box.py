class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROW, COL = len(boxGrid), len(boxGrid[0])
        
        for i in range(ROW):
            emptyPos = COL - 1
            for j in range(COL - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    emptyPos = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j], boxGrid[i][emptyPos] = ".", "#"
                    emptyPos -= 1
                    
        res = [["" for _ in range(ROW)] for _ in range(COL)]
        for r in range(ROW):
            for c in range(COL):
                res[c][ROW - 1 - r] = boxGrid[r][c]
        return res