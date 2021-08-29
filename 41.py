from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        tol = int((1+n+1)*n/2)
        for i, m in enumerate(nums):
            if 1 <= m <= n+1:
                tol -= m
            else:
                tol -= (n+1-i)
        return tol

if __name__ == "__main__":
    fun = Solution()
    nums = [3,4,-1,1]
    print(fun.firstMissingPositive(nums))