"""
We are gonna use has map

gonna look something like this

(0,0,1,1,0........0):[matching strings ]
(0,0,1,1,0........0):[matching strings ]
(0,0,1,1,0........0):[matching strings ]
(0,0,1,1,0........0):[matching strings ]

"""
from collections import defaultdict
from typing import List



class solution:
    def group_anagram(self,strs:List[str])->List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())
class main:
    def main():
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        sol=solution()
        res=sol.group_anagram(strs)

        print(res)

    
    if __name__=="__main__":
        main()