def binarysearch(arr,key,l,h):
    mid=(l+h)//2
    while(l<=h):
        
        if key==arr[mid]:
            return mid
        elif key>arr[mid]:
            return binarysearch(arr,key,mid+1,h)
        elif key<arr[mid]:
            return binarysearch(arr,key,l,mid-1)
    

def main():
    
    print("Enter the number of elements: ")
    n=int(input())
    arr=[]
    
    for i in range(n):
        arr.append(int(input(f"Enter the element{i+1}:")))
    key=int(input("Enter the key you want to search: "))
    result=binarysearch(arr,key,0,len(arr))
    print(result)
    
if __name__=="__main__":
    main()


    
    

