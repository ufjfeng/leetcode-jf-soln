"""
Given an input string, reverse the string word by word.

For example,
    Given s = "the sky is blue",
    return "blue is sky the".

Update (2015-02-12):
    For C programmers: Try to solve it in-place in O(1) space.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.strip().split()[::-1])

a = Solution()
print(a.reverseWords('a fast brown fox jumped over the lazy dog') == 
      'dog lazy the over jumped fox brown fast a')
