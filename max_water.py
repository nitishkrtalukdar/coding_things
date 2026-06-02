def maxwater(height,heightsize):
    left=0
    right=heightsize-1
    max_water=0

    while(left<right):
        width=right-left
        if(height[left]<height[right]):
            h=height[left]
        else:
            h=height[right]
        water=width*h
        if(water>=max_water):
            max_water=water
        if(height[left]<height[right]):
            left+=1
        else:
            right-=1
    return(max_water)

def main():
    height=list(map(int,input("Enter the heights of the sticks: ").split()))
    heightsize=len(height)
    result=maxwater(height,heightsize)
    print(f"The max water that the sticks can hold: {result}")

if (__name__=="__main__"):
    main()




