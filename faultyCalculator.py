#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 04:38:55 2021

@author: Preeti


"""

#DESIGN A CALCULATOR WHICH WILL CORRECTLY SOLVE ALL THE PROBLEMS EXCEPT THE FOLLOWING ONE:
#45*3=555, 56+9=77,  56/6=4



def sum(a,b=0):
    if (a==56 and b==9):
        return 77
    else: return a+b
    

def multiply(a,b=1):
    if (a==45 and b==3):
        return 555
    else: return a*b
    
def divide(a,b=1):
    if (a==56 and b==6):
        return 4
    else: return a/b
    
def difference(a,b=0):
    return  a-b


a,b=input('enter two number: ' ).split()
#fn= input('enter the function you want to perform: ') 
print(multiply(float(a),float(b)))

        

    
    
          
   