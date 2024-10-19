class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        return -1
# Explanation:
# This solution implements the binary search algorithm on a sorted array.
# We use two pointers, left and right, to define the search range.
# In each iteration, we compare the middle element with the target.
# If it matches, we return the index. If not, we adjust the search range.
# This process continues until the target is found or the range is empty.