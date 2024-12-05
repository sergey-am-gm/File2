mod = 10
list_ = [55,'str_1']
immutable_var = 10,'string',True,mod, list_
print(immutable_var)
immutable_var[4][1] = 'str_2'
print(immutable_var)

mutable_list = [10,'string',True,mod,list_]
print(mutable_list)
mutable_list[3] = 20
mutable_list.remove(list_)
mutable_list[0] = False
print(mutable_list)