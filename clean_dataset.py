import numpy as np
import pandas as pd

from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt



# funktionen definieren
# erhalte nummer des tags im jahr
def num_of_day(date):
    st_dayofyear = pd.Timestamp(year=date.year, month=1, day=1)
    day          = pd.Timestamp(year=date.year, month=date.month, day=date.day) 
    return((day - st_dayofyear).days + 1)


# entferne NaN eintraege aus spalte in dataframe
def rnan_lines(dframe, col_name):
    return( dframe[pd.notnull(dframe[col_name])])



# test
print("test1")
data = pd.read_csv("dataset/dataset_hard_clean.csv")
df = pd.DataFrame(data=data)
print(list(df))

# plt.figure(1)
# plt.plot(df["longitude"], df["latitude"], "x")
# plt.show()
# plt.close() 

print("test2")




# count how often which station occurs
plt.figure(2)
count_station = df["station"].value_counts()
plt.bar(x=count_station.index, height=count_station.values)
plt.show()
plt.close()


# Zerlege Datum in Jahr, Tag im Jahr, Stunde
# dtimes = np.datetime64(np.array(df["date"]))
dtimes = pd.Series([pd.to_datetime(dt) for dt in df["date"]]) 
years  = pd.Series([dts.year for dts in dtimes])
days   = pd.Series([num_of_day(dts) for dts in dtimes])  
hours  = pd.Series([dts.hour for dts in dtimes])

print(years[100:110], "\n", days[100:110], "\n", hours[100:110], "\n")


# erstelle DateFrames fuer jede der Stationen
df_dublin   = df[df["station"] == "Dublin_Airport"]
df_shannon  = df[df["station"] == "Shannon_Airport"]
df_casement = df[df["station"] == "Casement"]
df_cork     = df[df["station"] == "Cork_Airport"]
df_knock    = df[df["station"] == "Knock_Airport"]

plt.hist(df_dublin["temp"])
plt.show()
