"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0
≤ x < 10n.

Example:
    Given n = 2, return 91. (The answer should be the total numbers in the range
    of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

Hint:
    A direct way is to use the backtracking approach.

    Backtracking should contains three states which are (the current number,
    number of steps to get that number and a bitmask which represent which
    number is marked as visited so far in the current number). Start with
    state (0,0,0) and count all valid number till we reach number of steps
    equals to 10n.
    
    This problem can also be solved using a dynamic programming approach and
    some knowledge of combinatorics.

    Let f(k) = count of numbers with unique digits with length equals k.

    f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is
    9 because a number cannot start with 0].

Credits:
    Special thanks to @memoryless for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        if n > 10:
            n = 10
        counter = [0 for i in range(10)]
        for i in range(n):
            if i == 0:
                counter[i] = 10
            else:
                counter[i] = 9
                for j in range(1,i + 1):
                    counter[i] *= (10 - j)
        return sum(counter)
        
a = Solution()
for i in range(12):
    print(a.countNumbersWithUniqueDigits(i))
