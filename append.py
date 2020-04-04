list= ['a','b', 'c', 'd']
list.append(('e', 'F'))
print(list)

list1=['apple','peach', 'pineappe', "grape orange"]
list1.clear()
print(list1)

list1= ['people', 'sex', 'age', 'healthy']
list2=['1','2', '3', '4']
mylist= list1+list2
print(mylist)

list1.extend(list2)
print(list1)
print(list1.count('1'))

list.insert(0, 'Z')
print(list)
list.reverse()
print(list)
list.remove('a')
print(list)
print(len(list))
