N, K = map(int, input().strip().split())

arrayList = [i for i in range(1, N+1)]
answer = []
count = 0

for i in range(N):
    count += (K-1)
    if count >= len(arrayList):
        count %= len(arrayList)
    answer.append(str(arrayList[count]))
    arrayList.pop(count)

print("<", ", ".join(answer), ">", sep = '')