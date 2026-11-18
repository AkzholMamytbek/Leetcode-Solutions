class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]

        for i in range(len(first)):
            ch = first[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return first[:i]

        return first 