# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:23:01 2024

@author: Chi
"""

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
A = (a**(1/2) - (b**(1/2))) / ((a**(1/4) - b**(1/4))) - ((a**(1/2) + (a*b)**(1/4)) / (a**(1/4) + b**(1/4)))
print("kết quả: ", A)