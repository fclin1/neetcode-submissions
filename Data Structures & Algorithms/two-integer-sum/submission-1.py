class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in prev:
                return [prev.get(diff), i]
            prev[num] = i