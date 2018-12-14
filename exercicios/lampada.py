N = int(input())
status = input().split()

A = 0
B = 0

for i in range(N):
    if status[i] == '1':
        A = 1 if A == 0 else 0
    elif status[i] == '2':
        A = 1 if A == 0 else 0
        B = 1 if B == 0 else 0
print(A)
print(B)
