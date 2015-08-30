__author__ = 'ay27'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        pat = ''
        for i in range(len(s)):
            if s[i] in pat:
                pat = pat[pat.index(s[i])+1:]
            pat += s[i]
            result = max(result, len(pat))
        return result


print(Solution().lengthOfLongestSubstring('bbbbbb'))
print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('abcdefg'))
print(Solution().lengthOfLongestSubstring(''))
