##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)

#Separo los elementos de la columna
base1 = base[4].apply(lambda x: pandas.Series(x.split(','))) 

#Sacar cada columna por separado eliminando los NaN
base10 = base1[0].dropna()
base11 = base1[1].dropna()
base12 = base1[2].dropna()
base13 = base1[3].dropna()
base14 = base1[4].dropna()
base15 = base1[5].dropna()

base100 = list(base10)
base111 = list(base11)
base122 = list(base12)
base133 = list(base13)
base144 = list(base14)
base155 = list(base15)

#Concatenar las lista
baselistas = base100+base111+base122+base133+base144+base155

#Convertir lista completa a dataframe
basedataframe = pandas.DataFrame({'col':baselistas})

#Separar trio de letras y numero
basedataframe1 = basedataframe['col'].apply(lambda x: pandas.Series(x.split(':')))

#Contador
basedataframe2 = basedataframe1.groupby(0)[1].count()

#Resultado en listas
triolist = list(basedataframe1[0])
triounique = set(triolist)
trio = sorted(triounique)
basedataframe2l = list(basedataframe2)

for i in range(len(trio)):
    print(trio[i], basedataframe2l[i], sep=',')