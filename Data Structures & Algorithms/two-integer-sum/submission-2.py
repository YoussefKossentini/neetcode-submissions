class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()
        i = 0
        j = len(arr) - 1
        while i < j:
            current = arr[i][0] + arr[j][0]
            if current < target:
                i += 1
            elif current > target:
                j -= 1
            else:
                return sorted([arr[i][1], arr[j][1]])