import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt

num_data=1000
#print("Daten einlesen")
#data = pd.read_csv("dataset/dataset_vim_clean.csv")
#df   = pd.DataFrame(data=data)#
#df   = df.drop(df.columns[0], axis=1)
#print(list(df), sep="\n")

station_array=np.array(["ds_dublin","ds_shannon","ds_casement","ds_cork","ds_knock"])
list=np.genfromtxt("dataset/"+str(station_array[0])+".csv",delimiter=",",unpack=True, max_rows=1,dtype='unicode')
#len(station_array)
def load_data_to_array(station):
    empty_array=np.array([])
    for j in range(0,
        len(list)
        ):
        empty_array=np.append(empty_array,station+list[j])
    empty_array = np.genfromtxt("dataset/"+str(station)+".csv",max_rows=num_data,delimiter=",",skip_header=1, unpack=True)
    return empty_array


ds_dublin=load_data_to_array("ds_dublin")
ds_shannon=load_data_to_array("ds_shannon")
x=np.linspace(0,num_data,num_data)

print(x.dtype, ds_dublin[5].dtype)

plt.plot(x,(ds_dublin[5]))
plt.savefig("ds_dublin.pdf")
        #station_array[i]=np.array([list[j]])

        #str(station_array[i])+str(list[j])=np.append()
        #station_array[i]=np.array(np.append(station_array[i],str(station_array[i])+str(list[j])))




#    np.getfromtxt(str(station_array[i])+".csv"
    #, unpack=True, delimiter=",",skip_header=1,max_rows=2)
#plt.figure(2)
#count_station = df["station"].value_counts()
#plt.bar(x=count_station.index, height=count_station.values)
#plt.subplots_adjust(bottom=0.25)
#plt.xticks(rotation='45')
#plt.savefig('station_hist.pdf')
#plt.figure(3)
#count_countys = df["county"].value_counts()
#plt.bar(x=count_countys.index, height=count_countys.values)
#plt.show()
