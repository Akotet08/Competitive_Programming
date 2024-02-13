n  = int(input())

mx = 0
cap = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    cap -= a
    cap += b

    if cap > mx:
        mx = cap

print(mx)
