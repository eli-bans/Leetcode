class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #let's create an array of prefixes
        res = [1] * len(nums)  #initialize the array with 1s
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #store the prefix
            prefix *= nums[i] #update the prefix


        #let's get the post fixes
        postfix = 1
        for i in range(len(nums)-1,-1, -1):
            res[i] *= postfix  #multiply the prefix with the postfix
            postfix *= nums[i]

        return res

    '''
    Time complexity: O(n)
    Space complexity: O(1)
    
    The trick is to store the prefix and postfix in the same array.
    
    This one really took me a while to get. 
    '''

