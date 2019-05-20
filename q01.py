##
## Imprima la suma de la segunda columna.
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)
q01 = base[1].sum()
print(q01)