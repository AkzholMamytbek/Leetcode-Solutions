class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                b = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge2(lists[i], b))
            lists = merged
        return lists[0]

    def merge2(self, a, b):
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next