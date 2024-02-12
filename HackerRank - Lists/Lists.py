if __name__ == '__main__':
    N = int(input())
    
    lst = []
    
    for j in range(N):
        line = input().split()
        cmd = line[0]
        
        if cmd == 'insert':
            pos = int(line[1])
            element = int(line[2])
            lst.insert(pos, element)
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            ele = int(line[1])
            lst.remove(ele)
        elif cmd == 'append':
            ele = int(line[1])
            lst.append(ele)
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
        else:
            print(f'command {cmd} not found')