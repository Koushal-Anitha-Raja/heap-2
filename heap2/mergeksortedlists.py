#Time_Complexity: O(nlogk)
#Space_Complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         # creating the custom comparator by overrding the default lessthan operator 
        ListNode.__lt__ = lambda a,b : a.val<b.val
        #define the __lt__ function with lambda function
        minheap=[] # creating the minheap
         #dummy node   
        result = ListNode(-1)
        #current to the result
        curr = result 

        #iterate through f head in lists
        for lhead in lists:
            #if head is present
            if lhead:
                #pushing it to the minhead 
                heappush(minheap,lhead)

        # until minheap is empty
        while minheap: 
            # pop the heap value and store in top
            top = heappop(minheap)
            # top to curr.next
            curr.next = top 
            #curr to curr.next
            curr = curr.next
            #until top.next is there
            if top.next:
                # push the top.next value in the heap array
                heappush(minheap,top.next) 


        return result.next
        
