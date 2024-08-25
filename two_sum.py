class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store number and its index
        num_to_index = {}
        
        # Iterate over the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # Return the indices of the complement and the current number
                return [num_to_index[complement], i]
            
            # Store the number and its index in the dictionary
            num_to_index[num] = i
        
        # In case no solution is found (though the problem guarantees exactly one solution)
        return []

# Create an instance of the Solution class
solution = Solution()

# Define the input
nums = [2, 4, 1, 15]
target = 3

# Call the twoSum method and get the result
result = solution.twoSum(nums, target)

# Print the result
print(result)  # Output: [0, 1]
