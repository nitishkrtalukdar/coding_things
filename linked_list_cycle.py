##detect cycles in a linkedlist
#CONCEPT: Fast and slow pointer approach

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class solution:
    def hascycle(self,head):
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False
    
class main:
    def main():
        n1=ListNode(0)
        n2=ListNode(1)
        n3=ListNode(2)
        n4=ListNode(3)

        n1.next=n2
        n2.next=n3
        n3.next=n4
        n4.next=None

        sol=solution()
        print(sol.hascycle(n1))


    if __name__=="__main__":
        main()