#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przedmiot: Informatyka
# Kierunek studiów: Mechanika i Budowa Maszyn
# Semestr: zimowy
# Rok akademicki: 2020/2021
# Data (dzień.miesiąc.rok): 20.11.2020
# Imię: Jakub
# Nazwisko: Charkowski
# Numer albumu ZUT: 49940

import math

Vmin = 100**3

r_best = 1000,0
 
for a in range(1,1001,1):
    
     for b in range(1,1001,1):
         
         c = Vmin / a / b
         
         if a * b * math.floor(c) >= Vmin:
             
             c = math.floor(c)
         else:
            
             c = math.ceil(c)
            
         d = math.sqrt(a**2 + b**2 + c**2)
        
         r = d - math.floor(d)
        
         if r == r_best: r_best = r
a_best = a
b_best = b
c_best = c
            
print ( a_best, b_best, c_best, math.sqrt(a_best**2 + b_best**2 + c_best**2))            