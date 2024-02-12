if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(arr, reverse=True)
    
    second_large = arr[0]
    
    j = 1
    while j < len(arr):
        if arr[j] != second_large:
            second_large = arr[j]
            break
        j += 1
    print(second_large)
            
    
        
        