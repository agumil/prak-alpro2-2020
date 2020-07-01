#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:51:01 2020

@author: gumil
"""

def insertionSortAsc(sort_list):
    print('================== Ascending ===================')
    print('deret : ', sort_list, '\n')
    n = 1
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = key
        print('pergeseran pada iterasi ke', n, 'dimana j =', sort_list[j+1],'ke index', j+1)
        print('iterasi ke', n, sort_list, '\n')
        n += 1

def insertionSortDesc(sort_list):
    print('================== Descending ===================')
    print('deret : ', sort_list, '\n')
    n = 1
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key > sort_list[j]:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = key
        print('pergeseran pada iterasi ke', n, 'dimana j =', sort_list[j+1],'ke index', j+1)
        print('iterasi ke', n, sort_list, '\n')
        n += 1
        
A = [4, 3, 5, 6, 2, 78, 98]
insertionSortAsc(A)

A = [4, 3, 5, 6, 2, 78, 98]
insertionSortDesc(A)
