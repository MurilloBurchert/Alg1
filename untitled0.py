# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:11:00 2022

@author: muril
"""

# -*- coding: utf-8 -*-

#1
    
def check_divide_tres(n):
        
    if n%3 == 0:
        return True
    else:
        return False
    
def fatorial(n):
        
    y = 1
    while n > 0:
        y = y * n
        n -=1
    return y
    
def serie(n):
        
    x = 0
    s = 0
    while x<=n:
        s = s + n/fatorial(x)
        x+=1
    return s

def main():
        ###A leitura dos números vem aqui. Como não tenho certeza de como é feita,
        #é só adaptar de algum outro código que já tenha feito.
    num_list = []
    count = 0
    while True:
        n = input('Entrada: ')
        n = int(n)
        count+=1
        if check_divide_tres(n):
            n = fatorial(n)
        else:
            n = serie(n)
        num_list.append(n)
        if count>4:
            break
        
    return sum(num_list)

num = main()
print(round(num, 2))