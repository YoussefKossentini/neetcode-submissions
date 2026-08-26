class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        l1 = sorted(dict1.items())
        l2 = sorted(dict2.items())
        return l1 == l2