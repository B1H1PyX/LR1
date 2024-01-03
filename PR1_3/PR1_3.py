n = 5
for i in range(n, 0, -1):
    print('  ' * n, end='')
    print(*range(i, n + 1))
for i in range(n + 1):
    print('  ' * (n - i + 1), end='')
    print(*range(i, 0, -1))