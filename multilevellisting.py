# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:32:36 2021

@author: shash
"""

#Python program to input multilevel list
multi_level_list = list()
number_of_lists = 0
while number_of_lists == 0:
    number_of_lists = input("Please provide Number of lists :")
for index in range(number_of_lists):
    multi_level_list.append(list())
    list_length = input("Please length of list [%s] :" %index)
    while list_length > 0:
        multi_level_list[index].append(input("please provide the value for list [%s][%s] :" %(index, len(multi_level_list[index]))))
        list_length -= 1

print (multi_level_list)

     