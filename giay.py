# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:26:56 2024

@author: Chi
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
gi = int(input("Nhập giây: "))
tong_giay = gio * 3600 + phut * 60 + gi
print("Tổng số giây là: ",tong_giay)