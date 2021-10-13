# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:51:53 2021

@author: Saksham
"""

l = eval(input('Length of Multi List: '))
final_list = []

for i in range(0, l):
    templist = []
    n = eval(input('Length of Nested List: '))
    for a in range(0, n):
        e = input('Element of the List: ')
        templist.append(e)
    final_list.append(templist)

# displays the list
print('\n',final_list,'\n')

# displays individual elements of the list
for i in final_list:
    print()
    for n in i:
        print(n,end= ' ')
