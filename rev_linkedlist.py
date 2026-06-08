class node:
    def __init__(self,data):
        self.val=data
        self.next=None

#                     c 
#        1<-2<-3<-4
#                 p
class solution:
    def reverse_ll(self,head):
        prev=None
        cur=head

        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    
class main():
    def main():
        linkedL=solution()
        l1=node(1)
        l2=node(2)
        l3=node(3)
        l4=node(4)

        l1.next=l2
        l2.next=l3
        l3.next=l4

        linkedL.reverse_ll(l1)
        head=l4
        while head:
            print(head.val)
            head=head.next
        return
    if __name__=="__main__":
        main()