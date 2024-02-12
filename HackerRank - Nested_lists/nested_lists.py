if __name__ == '__main__':
    
    lst = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score in lst:
            lst[score].append(name)
        else:
            lst[score] = [name]
    
    second_smallest = list(lst.keys())[1]
    smallest = list(lst.keys())[0]
    
    if second_smallest < smallest:
        second_smallest, smallest = smallest, second_smallest
     
    for key in lst.keys():
        if key > smallest and key < second_smallest:
            second_smallest = key
        elif key < smallest:
            smallest = key
            
    for nm in sorted(lst[second_smallest]):
        print(nm)
        