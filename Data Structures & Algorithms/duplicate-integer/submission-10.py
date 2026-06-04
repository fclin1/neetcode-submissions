class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        dupe = False
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                dupe = True
        return dupe
         