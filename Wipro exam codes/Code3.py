num = int(input())
arr = list(map(int, input().split(",")))
swap = int(input())
print(arr[swap:]+arr[:swap])
