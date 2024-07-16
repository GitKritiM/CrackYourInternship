class Solution:

    def findMinDiff(self, A,N,M):
       
        # code here
         A.sort()
         min_diff = A[N-1] - A[0]
         for i in range(len(A) - M + 1):
            min_diff = min(min_diff ,  A[i + M - 1] - A[i])
         return min_diff