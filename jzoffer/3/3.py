class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        for idx in range(1, len(nums)):
            if pre == nums[idx]:
                return pre
            pre = nums[idx]