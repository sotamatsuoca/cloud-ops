class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowMap = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rowMap[row] = rowMap.get(row, 0) | (1 << (seat - 2))

        result = (n - len(rowMap)) * 2

        left = 0b00001111
        middle = 0b00111100
        right = 0b11110000

        for mask in rowMap.values():
            if (mask & left) == 0 or (mask & right) == 0:
                result += 1
            elif (mask & middle) == 0:
                result += 1

        return result