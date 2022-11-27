data_list = [1,2, 3]
ones_list = [1,1, 1]
print(data_list)
print(ones_list)
def sum_list(arr1, arr2):
    emp_list= []
    zip_list_new = list(zip(arr1, arr2))
    print(zip_list_new) #list of tuples
    for i in zip_list_new:
        sum_ = i[0] +i[1]
        emp_list.append(sum_)
    return emp_list

sum_l = sum_list(data_list,ones_list)
print(sum_l)