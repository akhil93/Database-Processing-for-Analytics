# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 15:45:53 2014

@author: Akhilkumar
"""
with open('City.csv', mode='r') as infile1:
    reader1 = csv.reader(infile1)
    with open('City1.csv', mode='w') as outfile1:
        writer1 = csv.writer(outfile1)
        mydict1 = {(rows[0],rows[1]) for rows in reader1}