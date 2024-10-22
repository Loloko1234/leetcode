from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

# Explanation:
# This solution efficiently groups anagrams using a hash map approach.
# We iterate through each word in the input list:
# 1. Sort the characters of the word to create a 'signature'.
# 2. Use this sorted word as a key in our hash map (defaultdict).
# 3. Append the original word to the list associated with this key.