def linear_search(arr,key,n):
    for i in range(0,n):
        if arr[i]==key:
            return i
    return -1

arr=[]
n=int(input("Enter the no. of elements:\n"))
print("Enter the values of element:")
for i in range(0,n):
    ele=int(input())
    arr.append(ele)

key=int(input("Enter the element, which you want to search.\n"))
result=linear_search(arr,key,n)

if result==-1:
    print("Element not found!")
else:
    print("Element found at index: ",result)
