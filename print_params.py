
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(5, 15)
print_params(c=225)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = ['88', [15, 16,'ddd'], ('q','w','e','r','t','y')]
values_dict = {'a': '111', 'b': 222, 'c': False}

print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)