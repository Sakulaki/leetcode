class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        length = 1
        for i in range(len(s)-1):
            j = 1
            len1 = 1
            while i-j >= 0 and i+j <= len(s)-1 and s[i-j]==s[i+j]:
                len1 += 2
                j += 1
            if len1 > length:
                res = s[i-j+1:i+j]
                length = len1

            j = 0
            len2 = 0
            while i-j >= 0 and i+1+j <= len(s)-1 and s[i-j]==s[i+1+j]:
                len2 += 2
                j += 1
            if len2 > length:
                res = s[i-j+1:i+j+1]
                length = len2
        print(length)
        return res


if __name__ == "__main__":
    s = Solution()
    t = "abcc"
    print(s.longestPalindrome(t))
