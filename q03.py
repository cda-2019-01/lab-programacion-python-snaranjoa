##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)
q03c = base.groupby(0).sum()[1]
q03l = list(q03c)
q02list = list(base[0])
uniqueletters = set(q02list)
ul = list(uniqueletters)
letters = sorted(uniqueletters)
for i in range(5):
    print(letters[i], q03l[i], sep=',')