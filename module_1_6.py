my_dict = {'sergey':1966,'sveta':1965,'nadia':1972,'anna':2011}
print('my_dict:',my_dict)
print('Existing value:',my_dict['anna'])
print('Not existing value:',my_dict.get('den'))
my_dict_1 = {'max':1999,'vera':1945}
my_dict.update(my_dict_1)
print('Deleted value:',my_dict.pop('anna'))
print('Modified my_dict:',my_dict)

tuple_ = (7,8,9)
my_set = {5,5,13,'sveta',3.14,11,5,tuple_}
print('my_set:',my_set)
my_set.add('anna')
my_set.add('1234')
my_set.remove(5)
print('Modified my_set:',my_set)

#Вариант добавить два элемента объединением
#my_set = my_set.union(set(my_dict_1.keys()))
#print('Modified my_set:',my_set)
