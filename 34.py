from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def searchLeft(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return left

        def searchRight(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] <= target:
                    left = mid + 1
            return right
        length = len(nums)
        left = searchLeft(0, length-1, target)
        right = searchLeft(0, length-1, target+1)
        if left == length or nums[left] != target:
            return [-1, -1]
        return [left, right-1]

if __name__ == "__main__":
    fun = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(fun.searchRange(nums,target))