from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            count[char] += 1 

        for char in t:
            count[char] -= 1 

        for val in count.values():
            if val != 0:
                return False

        return True

# Explanation:
# This solution checks if two strings are anagrams using a hash map approach.
# We first check if the lengths of the strings are equal. If not, they can't be anagrams.
# We use a defaultdict to count the occurrences of each character in the first string.
# Then we decrement the count for each character in the second string.
# If the strings are anagrams, all counts should be zero at the end.
# This method has a time complexity of O(n) and space complexity of O(1) since
# there is a fixed number of possible characters.
