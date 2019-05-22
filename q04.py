##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
import pandas
base = pandas.read_csv("data.csv", sep="\t", header=None)
base.head(1)
import datetime
base[2] = pandas.to_datetime(base[2], errors='ignore')
base[2].dt
base['mes'] = base[2].dt.month
base1 = base.groupby('mes')[1].count()
print(base1)