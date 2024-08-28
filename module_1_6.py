my_dict={'Marydit' : 1985, 'Kristina' : 1986, 'Georg' : 1983}
print(my_dict)
print(my_dict['Marydit'])
my_dict['Elis'] = 1968
print(my_dict)
my_dict.update({'Elizabet' : 1984, 'Alex' : 1987})
del my_dict['Georg']
print(my_dict.get('Georg'))
my_set={1,2,'apple',2,8,'orange', 'apple'}
print(my_set)
my_set.add('banana')
my_set.add(4)
my_set.discard(8)
print(my_set)