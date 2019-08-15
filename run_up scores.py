n = int(input())
arr = list(map(int, input().split()))[:n]
ab=max(arr)
while ab == max(arr):
arr.remove(max(arr))
print(max(arr))