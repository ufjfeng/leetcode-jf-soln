"""
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: in
        """
        if A is None:
            return 0
        if len(A) < 2:
            return 0
        n = len(A)
        sumA = sum(A)
        sumR = sum([i * A[i] for i in range(len(A))])
        soln = sumR
        for i in range(1, len(A) + 1):
            sumR = sumR + sumA - n * A[n - i]
            soln = max(soln, sumR)
        return soln

a = Solution()
print(a.maxRotateFunction([1, 3, 5, 7]) == 34)
print(a.maxRotateFunction([4, 3, 2, 6]) == 26)
