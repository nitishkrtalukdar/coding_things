"""
1. we gonna have a hash map of matching ones
2. we iterate through s
3. if we find a closing paren )}] then we check if the stack has its matching open paren ([{
    3.1 if the stack top aint equal we can directly print false
4. else we append to the stack
"""


class solution:
    def isvalid(self,s):
        closetoopen={')':'(',
                     ']':'[',
                     '}':'{'}
        stack=[]
        for c in s:                                         #iterate
            if c in closetoopen:                            #check if its a closing bracket (the keys are closing brackets so if we check if c is a key it means we are currently at a closing bracket)
                if stack and stack[-1]==closetoopen[c]:     #since c is a closing, we check if the stack top is its corresponding opening or not, if yes we pop stack 
                    stack.pop()                             
                else:
                    return False                            #stack top doesnt have the matching opening hence we return false
            else:
                stack.append(c)                             # this executes when c is not a key, it means its not closing, hence it is opening, so we append
        return True
    
class main:
    def main():
        s=str(input("Enter your string [.....BRACKETS ONLY......]:"))
        sol=solution()
        print(sol.isvalid(s))
        return

    if __name__=="__main__":
        main()
