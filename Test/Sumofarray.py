def largest(arr,num):
    max=arr[0]
    for i in range(0,num):
        if(arr[i]>max):
            max=arr[i]
    return max
arr=[]
num=int(input("Enter the Array Size"))
print("Enter the Array")
for i in range(0,num):    
    item=int(input())
    arr.append(item)

ans = largest(arr,num)
print(arr)
print("Largest num is ",ans)
    