# LINKEDLIST
Given a reference to the head of a doubly-linked list and an integer,  
create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.
Example
 head refers to the list 1<->2<->4->null
 data = 3
Return a reference to the new list: 1<->2<->3<->4->null

Function Description
Complete the sortedInsert function in the editor below.

sortedInsert has two parameters:
DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list
int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

Returns
DoublyLinkedListNode pointer: a reference to the head of the list

# if head is None, add int in the front
# if int < head, add int in the front
# if int > nodes in dll, add it in the end
# traverse thru the length of the dll
# add int to dll by checking and iterating if int is > prev node & < next node.
           
class Solution:
    def sortedInsert(head, data):
        dataNode = DoublyLinkedListNode(data)
        if head is None:
            head = dataNode
            dataNode.next = None
            return head
        current = head
        while current:
            if dataNode.data < current.data:
                current = dataNode
                dataNode.next = head
                return dataNode
            if dataNode.data > current.data & dataNode.data < current.next.data:
                current.data = dataNode
                dataNode.prev = current
                dataNode.next = current.next
                current.prev.next = dataNode
        return head
