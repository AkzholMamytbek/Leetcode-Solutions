class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        characters= set()
        left=0
        longest=0
        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left+=1
            characters.add(s[right])
            longest=max(longest,right-left+1)

        return longest