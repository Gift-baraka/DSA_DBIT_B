def transform_list(lst, mode= 'reverse', k=1):
    if mode== 'reverse':
        return lst [::-1]
    elif mode == 'reverse':
        k = k % len(lst)
        return lst[-k: ] + lst[:-k]
    else:
        raise ValueError("mode must either be reversed or rotated.")
    print(transform_list([1, 2, 3, 4, 5,6,7,8,9], mode='reverse')) 
print(transform_list([1,2,3,4,5,6,7,8,9], mode ='rotate'))
   


