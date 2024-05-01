class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # change the list to a set
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:  # check if it's a start
                count = 0
                while (n + count) in numSet:
                    count += 1

                # compare the count with the longest
                longest = max(longest, count)

        return longest

#Time complexity: O(n) because we're iterating through the list
#Space complexity: O(n) because we're storing the list in a set
'''
Trick is to figure out the start of the sequence.
And use a set for searching in constant time.
'''