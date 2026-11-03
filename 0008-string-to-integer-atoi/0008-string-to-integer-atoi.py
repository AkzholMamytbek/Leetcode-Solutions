class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Optional sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3 + 4. Read digits manually, clamping before overflow
        limit = INT_MAX if sign == 1 else -INT_MIN   # 2147483647 or 2147483648
        result = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            if result > (limit - digit) // 10:
                return sign * limit
            result = result * 10 + digit
            i += 1

        return sign * result