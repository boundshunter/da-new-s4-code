#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

def BinarySearch(arr,key):
    # print("222")
    min = 0
    max = len(arr) -1
    while True:
        # count += 1
        center = (max - min)/2
        if arr[center] < key:
            min = center + 1
        elif arr[center] > key:
            max = center -1
        else:
            print("get it")
            return arr[center]

if __name__ == '__main__':
    arr = [1,6,9,12,14,16,18,23,26,34,56,765]
    key = input(">>:").strip()
    if str.isdigit(key):
        BinarySearch(arr,key)
    else:
        print("Input error ,not digit.")