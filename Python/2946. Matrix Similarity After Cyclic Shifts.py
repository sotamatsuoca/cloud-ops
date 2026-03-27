class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        num_cols = len(mat[0])
        for row_idx, row in enumerate(mat):
            for col_idx in range(num_cols):
                if row[col_idx] != row[(col_idx + k) % num_cols]:
                    return False
        return True