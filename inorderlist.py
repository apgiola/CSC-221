def in_order(input_list):
    # a is is a list of true or false if i-1 index <= current index iterated 
    # through list starting from 2nd index to last index
    list_val = [input_list[i-1] <= input_list[i] for i in range(1, len(input_list))]
    # return true only if ALL values are boolean True. Otherwise return False
    return all(a == list_val[0] for a in list_val)
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')