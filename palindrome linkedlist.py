class node:
    def __init__(self,data):
        self.val=data
        self.next=None

class solution:

    def rev(self,head):
        prev=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    
    def palindrome(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        reversed=self.rev(slow)

        while reversed:
            if head.val!=reversed.val:
                return False
            head=head.next
            reversed=reversed.next
        return True
    
class main():
    def main():
        l1=node(1)
        l2=node(2)
        l3=node(2)
        l4=node(2)

        l1.next=l2
        l2.next=l3
        l3.next=l4

        sol=solution()

        res=sol.palindrome(l1)

        return res
        
if __name__=="__main__":
    print(main.main())