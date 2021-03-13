import collections
n, m = map(int, input().split())

sadari, bam = collections.defaultdict(int), collections.defaultdict(int)
for _ in range(n):
    tmp = list(map(int, input().split()))
    sadari[tmp[0]] = tmp[1]

for _ in range(m):
    tmp = list(map(int, input().split()))
    bam[tmp[0]] = tmp[1]


visited = [1e9] * 101

q = collections.deque()

visited[1] = True
q.append((1, 0))
mn = 1e9
while q:
    pos, count = q.popleft()
    if pos == 100:
        mn = min(count, mn)
        continue
    if sadari[pos] > 0:
        q.append((sadari[pos], count))
        continue
    if bam[pos] > 0:
        q.append((bam[pos], count))
        continue
    for i in range(1, 7):
        n_pos = pos + i
        if n_pos > 100:
            continue
        if visited[n_pos] > count + 1:
            visited[n_pos] = count + 1
            q.append((n_pos, count + 1))
print(mn)