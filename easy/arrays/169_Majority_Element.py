class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

# Explanation:
# This solution uses Boyer-Moore Voting Algorithm to find the majority element.
# We iterate through the list once, doing the following for each element:
# 1. If count is 0, we set the current number as our candidate (res).
# 2. If we see the same number as res, we increment count.
# 3. If we see a different number, we decrement count.
# 
# This approach has a time complexity of O(n) as we only traverse the list once.
# The space complexity is O(1) as we only use two variables regardless of input size.
# This method is more efficient than using a hash map or sorting approach.
# 
# The algorithm works because the majority element appears more than n/2 times,
# so it will always have a positive count at the end, while other elements
# will cancel each other out.