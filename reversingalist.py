def method1(lst):
    # start at index 0, go to index 0, incrementing backwards by 1. Append each element to new list, and print new list.
    rev_list = []
    for i in range(len(lst)-1, -1, -1):
        rev_list.append(lst[i])
    print(f'Method 1: {rev_list}')

def method2(lst):
    #list slicing
    print('Method 2:', lst[::-1])

def method3(lst):
    #reverse() function
    lst.reverse()
    print('Method 3:', lst)
    
def method4(lst):
    #reversed() function
    print('Method 4:', list(reversed(lst)))
     
ch = [1, 2, 3, 4]          
method1(ch)
method2(ch)
method3(ch)
method4(ch)
