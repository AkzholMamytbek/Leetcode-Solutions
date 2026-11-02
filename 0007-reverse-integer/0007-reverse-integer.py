class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x, rev = abs(x), 0
        while x:
            x, digit = divmod(x, 10)
            if rev > (INT_MAX - digit) // 10:   # rev * 10 + digit would overflow
                return 0
            rev = rev * 10 + digit
        return sign * rev