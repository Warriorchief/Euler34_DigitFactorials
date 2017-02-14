#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:30:40 2016

@author: christophergreen
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(x):
    i=x;
    fac=1;
    while i>1:
        fac*=i
        i-=1;
    return fac;

def separate_into_chars(num):
    s=str(num);
    chars=[];
    i=0;
    while i<len(s):
        chars.append(s[i]);
        i+=1;
    #print(list(chars));
    return list(chars);
    
def is_spec_num(num):
    chars=separate_into_chars(num);
    tot=0;
    i=0;
    while i<len(chars):
        tot+=factorial(int(chars[i]));
        i+=1;
    #print("total for",num,"is",tot);
    if tot==num:
        return True;
    return False;

def find_all_spec_nums(max):
    i=3;
    spec=[];
    while i<max:
        if i%100000==0:
            print("trying i as",i,"so there's another hundred thousand tested");
        if is_spec_num(i):
            spec.append(i);
        i+=1;
    print("special numbers are",spec,"so there are",len(spec),"that are less than",max);
    return spec;

#find_all_spec_nums(150); #special numbers are [145] so there are 1 that are less than 150

#find_all_spec_nums(1000000); #special numbers are [145, 40585] so there are 2 that are 
#less than 1000000

#find_all_spec_nums(10000000); #through ten million...special numbers are [145, 40585] 
#so there are 2 that are less than 10000000

find_all_spec_nums(100000000) #through one hundred million...
#special numbers are [145, 40585] so there are 2 that are less than 100000000
#answer=145+40585= 40730 CORRECT