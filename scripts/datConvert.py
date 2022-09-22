import pandas as pd
import csv

def string_in_file(file,s):
    datContent = [i.strip().split('\t') for i in open(r'{file}')]
    with open(file,'r') as F:
        writer = csv.writer(F)
        writer.writerows(datContent)
        