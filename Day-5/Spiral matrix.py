from typing import List

class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        ans = []
        n = len(mat)  # no. of rows
        m = len(mat[0])  # no. of columns
        top, left = 0, 0
        bottom, right = n - 1, m - 1

       
        while top <= bottom and left <= right:
            # For moving left to right
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

            # For moving top to bottom.
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            # For moving right to left.
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            # For moving bottom to top.
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
