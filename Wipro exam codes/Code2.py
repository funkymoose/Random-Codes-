
n = int(input())
k = int(input())
nums = list(map(int, input().split(" ")))
sum = 0
for i in nums:
    sum+=(i%k)
print(sum)
