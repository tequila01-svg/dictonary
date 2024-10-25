#empty
my_dict={}
#with integer
my_dict={1:'apple', 2:'mango'}
#mixed
my_dict={'name':'ayobami', 'age':'19', 'grade':'12'}
#output
print(my_dict)
print(my_dict['name'])
print(my_dict.get('age'))
#add item
my_dict['country']='nigeria'
print(my_dict)
#remove
my_dict.pop('age')
print(my_dict)
#remove
my_dict.clear()
print(my_dict)