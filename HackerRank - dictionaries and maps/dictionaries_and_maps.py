n = int(input())

dic = {}
for _ in range(n):
    name, number = input().split()
    dic[name] = number

while True:
    
    try:
        nm = input()
    except EOFError:
        break
    
    if nm in dic:
        print(f'{nm}={dic[nm]}')
    else:
        print('Not found')
    