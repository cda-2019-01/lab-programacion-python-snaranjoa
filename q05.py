##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)
q051 = base.groupby(0).max()[1]
q052 = base.groupby(0).min()[1]
q051l = list(q051)
q052l = list(q052)
q02list = list(base[0])
uniqueletters = set(q02list)
ul = list(uniqueletters)
letters = sorted(uniqueletters)
for i in range(5):
    print(letters[i], q051l[i], q052l[i], sep=',')