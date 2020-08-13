arr = []
n = int(input())
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

for i in arr:
    if(i==max(arr)):
        arr.remove(i)
arr.remove(max(arr))
print(max(arr))
