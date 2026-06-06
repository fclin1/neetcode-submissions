class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = []
        for num in nums:
            if num != val:
                output.append(num)
        k = len(output)
        nums[:] = output
        return k
        