na, nb = map(int, input().split())
k, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print('YES' if a[k - 1] < b[nb - m] else 'NO')
