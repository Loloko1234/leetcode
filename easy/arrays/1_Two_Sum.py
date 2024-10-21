class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for a, b in enumerate(nums):
            diff = target - b
            if diff in hash:
                return [hash[diff], a]
            hash[b] = a
        return False

# Explanation:
# This solution uses a hash map to solve the Two Sum problem efficiently.
# We iterate through the list once, doing the following for each element:
# 1. Calculate the difference between the target and the current element.
# 2. If this difference is already in our hash map, we've found our pair.
# 3. If not, we add the current element and its index to the hash map.
# This approach has a time complexity of O(n) as we only traverse the list once.
# The space complexity is also O(n) in the worst case, where we might need to store all elements in the hash map.
# This method is more efficient than the brute force approach of checking every pair of numbers.
