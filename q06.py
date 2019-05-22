##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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

#Resultado
basefinalmax = basedataframe1.groupby(0)[1].max()
basefinalmin = basedataframe1.groupby(0)[1].min()

#Resultado en listas
triolist = list(basedataframe1[0])
triounique = set(triolist)
trio = sorted(triounique)
basefinalmaxl = list(basefinalmax)
basefinalminl = list(basefinalmin)

for i in range(len(trio)):
    print(trio[i], basefinalminl[i], basefinalmaxl[i], sep=',')