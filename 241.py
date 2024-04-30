# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
# # Time complexity: O(nlogn), Space complexity: O(n).
'''
More efficient way:
    - Create a hashmap for each string.
    - Compare the hashmaps.
    - Time complexity: O(n), Space complexity: O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap of both strings and the counts of each's character
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i],0)
            tMap[t[i]] = 1 + tMap.get(t[i],0)
        for c in sMap:
            if sMap[c] != tMap.get(c,0):
                return False
        return True