def binarysearch(a,l,r,x):
        mid=(l+r)//2
        if r>=l:        
                if a[mid]==x:
                        return 1
                elif a[mid]>x:
                        return binarysearch(a,l,a[mid],x)
                elif a[mid]<x:
                        return binarysearch(a,a[mid],r,x)
a=list(map(int,input().split()))
x=int(input())
t=binarysearch(a,0,len(a)-1,x)
if t==1:
        print("Found")
else:
        print("Not Found")
