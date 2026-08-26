class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        list1 = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            list1[freq].append(num)
        result = []
        for freq in range(len(list1) - 1, 0, -1): #reverse the for loop : step=-1
            for num in list1[freq]:
                result.append(num)
                if len(result) == k:
                    return result