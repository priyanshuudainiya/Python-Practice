def binary_search(arr,key,low,high):
    while low<=high:
        mid=(low+high)//2

        if key==arr[mid]:
            return mid
        elif key>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[]
low=0
high=int(input("Enetr the no. of elements:\n"))
print("Enter the values of element:")
for i in range(low,high):
    ele=int(input())
    arr.append(ele)
arr.sort()
print("Sorted:",arr)
key=int(input("Enter the element, which you want search.\n"))
result=binary_search(arr,key,low,high)

if result==-1:
    print("Element is not found!")
else:
    print("Element found at index:",result)
