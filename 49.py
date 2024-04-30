class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for w in strs:
            # create count
            count = [0] * 26

            for c in w:
                count[ord(c) - ord("a")] += 1

            hashMap[tuple(count)].append(w)

        return hashMap.values()

