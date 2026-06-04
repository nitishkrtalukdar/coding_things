
from typing import List
class solution:
    def partitiion(self,nums:List[int],pivot:int)->List[int]:
        less=[]
        equal=[]
        more=[]

        for i in nums:
            if i<pivot:
                less.append(i)
            if i>pivot:
                more.append(i)
            if i==pivot:
                equal.append(i)
        return less+equal+more

class main:
    def main(): 
        nums=list(map(int,input("Enter space seperated numbers:").split()))
        piv=int(input("Enter the pivot number: "))
        sol=solution()
        print(sol.partitiion(nums,piv))
        return


    if __name__=="__main__":
        main()