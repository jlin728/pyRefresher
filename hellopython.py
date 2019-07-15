import random
import sys
import os

print ("Hello World")

'''
multiline
'''

name = "My Name Is"
print(name)

pythonDataTypes = ['Numbers', 'Strings', 'Lists', 'Tuples','Dictionaries']
print('Data Types:', pythonDataTypes[1])
'''to retrieve specific items from nested lists use
print(list[0][1])
where the first [] is the outer list, the second [] is for the inner list, etc.
'''
pythonDataTypes.append('No other types')
''' like push'''
pythonDataTypes.insert(2, 'Insert')

pythonDataTypes.remove('Insert')


pythonDataTypes.sort()
'''ascending'''

pythonDataTypes.reverse()
'''descending'''

del pythonDataTypes[4]
'''delete specific'''

len(pythonDataTypes)
'''length of list'''

max(pythonDataTypes)
'''length of list'''

min(pythonDataTypes)
'''length of list'''

py_tuple = (1, 2, 3, 4)
''' cannot be converted - immuatable'''

pyOperators = {
    'add': '+',
    'sub': '-',
    'mult': '*',
    'div': '/',
    'mod': '%, which returns the remainder when divided',
    'exponent': '**',
    'floorDiv': '//, divide and discard remainder and round down'
}
print(5//2)
print(5**2)


'''retrieve from a dictionary (aka map)'''
print (pyOperators['add'])
print(len(pyOperators))
'''pyOperators.get('key') - to get value of key
pyOperators.keys() - for list of keys
pyOperators.values() - for list of values
'''

'''conditionals
if 
elif
else  
== != > >= < <= 

logical operators
and &&
or ||
not 
'''

#for loops
num_list = [[1,2,3],[10,12,13],['A', 'B', 'C']]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

#while loops
random_num = random.randrange(0, 10)
while (random_num != 2):
    print(random_num)
    random_num = random.randrange(0, 10)

#end loop -> break
#continue



quote = "\"Always use back slash"

''' end parameter in print()
By default python’s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without newline.

Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line character. You can end a print statement with any character/string using this parameter.
'''

#Functions
def funcName()

#return vs 