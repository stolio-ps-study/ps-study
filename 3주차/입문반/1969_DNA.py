import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]

ans_dna = []
h_dist = 0
for i in range(m):
    cnt = [0] * 4
    for dna in s:
        cnt['ACGT'.index(dna[i])] += 1
    max_ = max(cnt)
    ans_dna.append('ACGT'[cnt.index(max_)])
    h_dist += n - max_

print(''.join(ans_dna), h_dist, sep='\n')