import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap

shortnum = 2000 


data_dublin   = pd.read_csv("dataset/ds_dublin.csv")
data_casement = pd.read_csv("dataset/ds_casement.csv") 
data_cork     = pd.read_csv("dataset/ds_cork.csv") 
data_knock    = pd.read_csv("dataset/ds_knock.csv") 
data_shannon  = pd.read_csv("dataset/ds_shannon.csv") 



df_dublin   = pd.DataFrame(data=data_dublin)
df_casement = pd.DataFrame(data=data_casement)
df_cork     = pd.DataFrame(data=data_cork)
df_knock    = pd.DataFrame(data=data_knock)
df_shannon  = pd.DataFrame(data=data_shannon)


print(list(df_dublin), sep="\n")
print(list(df_casement), sep="\n")

dublin_short   = df_dublin.head(shortnum)
casement_short = df_casement.head(shortnum) 
shannon_short  = df_shannon.head(shortnum) 
cork_short     = df_cork.head(shortnum) 



# plot locations
plt.figure(1)
m = Basemap(projection='lcc',
            llcrnrlon=-10,
            urcrnrlon=5,
            urcrnrlat=60,
            llcrnrlat=50,
            resolution="c", 
            lat_0=52.5, lon_0=-5, k_0=3)

# m.drawcoastlines()
# m.drawmapboundary(fill_color='aqua')
# m.fillcontinents(color='coral',lake_color='aqua')

coord = ["latitude", "longitude"]
lon_dublin, lat_dublin     = m(df_dublin[coord[1]][0], df_dublin[coord[0]][0])
lon_cork, lat_cork         = m(df_cork[coord[1]][0], df_cork[coord[0]][0])
lon_casement, lat_casement = m(df_casement[coord[1]][0], df_casement[coord[0]][0])
lon_knock, lat_knock       = m(df_knock[coord[1]][0], df_knock[coord[0]][0])
lon_shannon, lat_shannon   = m(df_shannon[coord[1]][0], df_shannon[coord[0]][0])

m.plot(lon_dublin, lat_dublin,     "o" , label="dublin")
m.plot(lon_cork, lat_cork,         "o" , label="cork")
m.plot(lon_casement, lat_casement, "o" , label="casement")
m.plot(lon_knock, lat_knock,       "o" , label="knock")
m.plot(lon_shannon, lat_shannon,   "o" , label="shannon")
plt.legend(loc='upper left')

m.shadedrelief(scale=1)

plt.savefig("build/map.png")



# ---functions---
def add_attr_hist(dframe, target, attribute, l, dftarget=None):
    if dftarget is None: 
        dftarget = dframe

    if set([target]) & set(attribute) == set():
        dframe[target] = dftarget[target]
        dframe_ret     = dframe.filter([target] + attribute, axis=1)
        dframe_attr    = dframe_ret.filter(attribute, axis=1)
    else:
        dframe_ret     = dframe.filter(attribute, axis=1)
        dframe_attr    = dframe_ret.filter(attribute, axis=1)
        dframe_ret["target-" + target] = dftarget[target]
    
    for j in range(0, len(attribute)):
        value = dframe_attr[attribute[j]].values.tolist()
        for i in range(1, l + 1):
            print("index : ", i)
            dframe_ret[str(attribute[j]) + "-" + str(i)] = pd.Series([np.nan] * i + value[0:(len(dframe_ret) - (i + 1))])

    return(dframe_ret[l:len(dframe)])


# eig nicht benötigt! function that creates dataframe, that contains attribute and attribute of the last l hours and next n
def attr_hist(dframe, attribute, l, n):
    dframe      = dframe.filter([str(attribute)], axis=1)
    dframe_attr = dframe[str(attribute)]

    for i in range(1, l + 1):
        dframe[str(attribute) + "-" + str(i)] = pd.Series([np.nan] * i + dframe_attr[0:(len(dframe) - (i + 1))].tolist())
        
    for i in range(1, n + 1):
        dframe[str(attribute) + "+" + str(i)] = pd.Series(dframe_attr[i:len(dframe)].tolist() + [np.nan] * i)
    
    return(dframe[l:(len(dframe) - n)])
# ---functions---



df_test_casement = add_attr_hist(casement_short, 'temp', ['temp', 'vappr', 'dewpt', 'rhum', 'msl'], 5, dftarget=dublin_short)
df_test_cork     = add_attr_hist(cork_short, 'temp', ['rain', 'vappr'], 5, dftarget=dublin_short)
df_test_shannon  = add_attr_hist(shannon_short, 'temp', ['temp'], 5, dftarget=dublin_short)

 
scatter_matrix(df_test_casement, figsize=(25, 25))
plt.savefig('build/scatter_matrix_casement.png')

scatter_matrix(df_test_cork, figsize=(25, 25))
plt.savefig('build/scatter_matrix_cork.png')

scatter_matrix(df_test_shannon, figsize=(25, 25))
plt.savefig('build/scatter_matrix_shannon.png')



# spalten exportieren

df_test_casement.to_csv('df_test_casement.csv', encoding="utf-8") 
