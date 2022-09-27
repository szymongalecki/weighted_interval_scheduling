from bisect import bisect_right

"""
Weighted Interval Scheduling :
calculate maximum total weigth of a subset of of the non-overlapping intervals

n - number of intervals
S - start times
F - finish times
W - weights
"""

n = int(input())
S, F, W = [], [], []

# read input
for _ in range(n):
    s, f, w = [int(_) for _ in input().split()]
    S += [s]
    F += [f]
    W += [w]

# sort all intervals by finish time in ascending order
F, S, W = (list(_) for _ in zip(*sorted(zip(F, S, W))))
M = [W[0]] + [None] * (n - 1)


# calculate optimal solution for each interval
for i in range(1, n):
    j = bisect_right(F, S[i])
    j = j - 1 if j > 0 else -1
    w = W[i] + M[j] if j != -1 else W[i]
    M[i] = max(w, M[i - 1])

# print optimal solution for provided set of intervals
print(M[-1])
