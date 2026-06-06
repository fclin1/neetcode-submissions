class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr) - 1, -1, -1):
            value = arr[i]
            arr[i] = max
            if value > max:
                max = value
        return arr
        