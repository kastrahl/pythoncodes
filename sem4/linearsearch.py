list = []
num = int(input("no of elements in array: "))
for i in range(1, num + 1):
    element = int(input("Enter element: "))
    list.append(element)
print("Array is :", list)
searchkey = int(input("Enter element to search"))

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
searchresult = search(list,searchkey)
if searchresult == -1 :
     print("not found")
else :
     print("element found at index ", searchresult)

