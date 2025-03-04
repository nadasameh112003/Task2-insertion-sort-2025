def insertionSort(arr):
  m=len(arr)
  for i in range(1,m):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
grades = [77,44,88,98,65,50]
insertionSort(grades)
print(grades)      