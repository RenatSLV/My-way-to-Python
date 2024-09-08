def add_num_sum(lst):
    Sum_pos = sum(x for x in lst if x > 0)
    Sum_neg = abs(sum(x for x in lst if x < 0))

    X = Sum_neg - Sum_pos
    lst.append(X)
    return lst

lst = [-3 ,-1 ,-4 ,-6 ,-8 ,5 ,2 ,7 ,9 ,3 ,2]
print(f"Старый список {lst}")
New_lst = add_num_sum(lst)
print(f"Новый список {New_lst}")