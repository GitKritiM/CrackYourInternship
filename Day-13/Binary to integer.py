class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
         num = 0
         current = head
    
         while current is not None:
            num = num * 2 + current.val
            current = current.next
        
         return num
        