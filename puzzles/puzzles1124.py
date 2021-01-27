
def int_sum(lst, k):
    new_lst = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == k:
                new_lst.append([lst[i], lst[j]])
                return True
            else:
                return False

    return new_lst

    
            

