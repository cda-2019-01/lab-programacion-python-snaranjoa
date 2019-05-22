##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)

#Contar los registros de los campos 3 y 4 separados por ,
base['count3'] = base[3].str.split(",").str.len()
base['count4'] = base[4].str.split(",").str.len()

basefinal = base[[0,'count3','count4']]
print(basefinal)