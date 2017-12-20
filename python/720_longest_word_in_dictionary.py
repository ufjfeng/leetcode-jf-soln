"""
Given a list of strings words representing an English Dictionary, find the
longest word in words that can be built one character at a time by other words
in words. If there is more than one possible answer, return the longest word
with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]

Output: "world"

Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and
"worl".

Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

Output: "apple"

Explanation: 

Both "apply" and "apple" can be built from other words in the dictionary.
However, "apple" is lexicographically smaller than "apply".

Note:

    All the strings in the input will only contain lowercase letters.

    The length of words will be in the range [1, 1000].

    The length of words[i] will be in the range [1, 30].
"""
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        words_set = set(words)
        max_len = 0
        soln = []
        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in words_set:
                    valid = False
                    break
            if valid:
                if len(word) == max_len:
                    soln.append(word)
                elif len(word) > max_len:
                    soln = [word]
                    max_len = len(word)
        if soln:
            return sorted(soln)[0]
        else:
            return ""

a = Solution()
assert a.longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]) == 'eyj'
