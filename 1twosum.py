class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create an empty dictionary
        # It will store: number -> index
        mp = {}

        # Go through the array
        # i = index
        # num = value at that index
        #
        # Example:
        # nums = [2, 7, 11, 15]
        #
        # First loop:  i = 0, num = 2
        # Second loop: i = 1, num = 7
        for i, num in enumerate(nums):

            # Find the number we need to add with 'num'
            # to get the target
            #
            # Example:
            # target = 9
            # num = 2
            #
            # complement = 9 - 2 = 7
            #
            # So, we need 7 to make 9
            complement = target - num

            # Check whether the complement was already
            # seen earlier in the array
            #
            # Example:
            # complement = 2
            # mp = {2: 0}
            #
            # 2 is present in mp -> True
            if complement in mp:

                # mp[complement] gives the index
                # where the complement was found
                #
                # i gives the current number's index
                #
                # Example:
                # mp[2] = 0
                # i = 1
                #
                # Therefore return [0, 1]
                return [mp[complement], i]

            # If complement was not found,
            # store the current number and its index
            #
            # Example:
            # num = 2
            # i = 0
            #
            # mp becomes {2: 0}
            mp[num] = i