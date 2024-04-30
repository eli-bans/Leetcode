class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            hashmap[i] = 0 # value doesn't matter
        return False


# Time complexity: O(n), Space complexity: O(n)
'''
Brute force:
    - Compare each element with every other element in the list.
    - Time complexity: O(n^2)
    - Space complexity: O(1)
    
Sorting method:
Woud've taken O(nlogn) time complexity and O(1) space complexity.

The hash table makes the time complexity of the containsDuplicate function O(n).
Could've use a set as well. Also takes a time complexity of O(1) for searching.
'''