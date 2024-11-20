class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

# Explanation:
# This solution uses the "two pointers" approach to find the intersection of two linked lists.
# We iterate through both lists simultaneously, doing the following:
# 1. When pointer l1 reaches the end of list A, redirect it to head of list B
# 2. When pointer l2 reaches the end of list B, redirect it to head of list A
# 3. If there's an intersection, both pointers will meet at the intersection node
# 4. If there's no intersection, both pointers will become null
#
# This approach has a time complexity of O(n + m) where n and m are lengths of the lists.
# The space complexity is O(1) as we only use two pointers regardless of input size.
# 
# The algorithm works because:
# - If lists intersect, both pointers will travel the same total distance
# - After switching lists, they will meet at intersection point
# - If no intersection exists, both pointers will become null simultaneously