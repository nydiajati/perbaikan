# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:04:49 2024

@author: ACER
"""
n = int(input("Masukkan nilai n: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1


print("Jumlah bilangan dari 1 hingga", n, "adalah:", total)
