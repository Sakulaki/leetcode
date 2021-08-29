class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        dic = dict()

        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            dic[s[i]] = i
        return max_length

if __name__ == "__main__":
    s = "abcabcd"
    so = Solution()
    print(so.lengthOfLongestSubstring(s))

