H = int(input())
T = []
for i in range(H):
    input_ = input()
    line = list(map(int, input_.split(' ')))
    assert len(line) == i + 1
    T.append(line)

k = 2
for i in range(1, H):
    for j in range(k):
        if j == 0:
            T[i][j] = T[i][j] + T[i - 1][j]
        elif i == j:
            T[i][j] = T[i][j] + T[i - 1][j - 1]
        else:
            T[i][j] = max(T[i - 1][j - 1], T[i - 1][j]) + T[i][j]
    k += 1
print(max(T[H - 1]))