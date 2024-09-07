#2
immutable_var = 1, 2.0, 3, 'baby'
print(type(immutable_var))
print(immutable_var)

#3
# TypeError: 'tuple' object does not support item assignment
# Главное свойство кортежа - это невозможность изменить содержимое кортежа после его создания
# после его создания

#4
mutable_list = ['baby', [1, 2, 3]]
mutable_list [1] = 'aplle'
mutable_list [1] = 2.0
print(type(mutable_list))
print(mutable_list)
