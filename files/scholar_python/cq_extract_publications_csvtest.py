#!/usr/bin/env python
"""
Script pour extraire les donnees
"""
###
###
import csv

pilist=open("pi_list.csv").realines()
year="2012"

for x in range(0, 3):
  piname=pilist[1,x]
  
  %run scholar.py -c 5 -a "piname" -t --none "calcul quebec" --after 2012 --no-patents --no-citations --csv > "piname".csv


