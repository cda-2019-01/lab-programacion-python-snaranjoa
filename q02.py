##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)
q02list = list(base[0])
uniqueletters = set(q02list)
q02c = [(l, q02list.count(l)) for l in sorted(uniqueletters)]
for i in range(5):
    print(q02c[i][0],q02c[i][1], sep=',')