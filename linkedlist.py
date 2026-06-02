class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=self.tail=None
        

    def add(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def pop(self):
        self.prev
        self.temp
        prev=temp=self.head
        if self.head is None:
            print("Empty List")
        else:
            while temp.next!=None:
                prev=temp
                temp=temp.next
            self.tail=prev
            self.tail.next=None
    def display(self):
        temp=self.head
        if self.head is None:
            print("List is Empty")
        else:
            while(temp.next!=None):
                print(temp.data)
                temp=temp.next
def main():
    choice=0
    linked_list=singlylinkedlist()
    while(choice!=4):
        choice=int(input("Enter Choice\n1.Add\n2.Delete\n3.Display\n4.Exit\n"))
        switch={
            1: lambda:linked_list.add(input("Enter the element")),
            2: lambda:linked_list.pop(),
            3: lambda:linked_list.display(),
            4: lambda:exit()
        }
        action=switch.get(choice,lambda:print("Invalid Choice"))
        action()
        
if __name__=="__main__":
    main()
                


    