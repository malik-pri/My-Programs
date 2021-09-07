#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:13:23 2021
find the word used the mlst in the text

@author: Preeti
"""

name=input('Enter the file name: ')
handle=open(name)


counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[words]=counts.get(words,0)+1
        
    
bigword= None
bigcount=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
        
        
        
print('bigword:', word)    
print('bigcount',count)
