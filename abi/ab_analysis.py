

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import  matplotlib
import matplotlib.cbook as cbook


class ABB(object):

    def read_data1(self, path):
        """
        Read data from CSV file
        :param path: string
        :return: pandas dataframe
        """
        try:
            dataset = pd.read_excel("/home/kuliza227/github/Codeathons/abi/Dataset 2.xlsx",index_col=None)
            print(dataset)
            return dataset
        except Exception as e:
            print(e)

    def read_data2(self, path):
        """
        Read data from CSV file
        :param path: string
        :return: pandas dataframe
        """
        try:
            dataset = pd.read_excel("/home/kuliza227/github/Codeathons/abi/Datase 1.xlsx", index_col=None)
            print(dataset)
            return dataset
        except Exception as e:
            print(e)

    def plot_time_data(self,dataset):
        years = mdates.YearLocator()   # every year
        months = mdates.MonthLocator()  # every month
        yearsFmt = mdates.DateFormatter('%Y')

        fig, ax = plt.subplots()
        #ax.plot(dataset["Month"], r.adj_close)

        dataset["price"]= dataset.iloc[:,1]+dataset.iloc[:,2]+dataset.iloc[:,3]+dataset.iloc[:,4]+dataset.iloc[:,5]+dataset.iloc[:,6]
        dates = matplotlib.dates.date2num(dataset.iloc[:,0])

        plt.plot_date(dates, dataset["price"],color="red")
        plt.scatter(dates, dataset["price"])
        ax.set_xlabel("YEARS")
        ax.set_ylabel("PRICE ")
        ax.set_title("Price of PET vs Time")
        plt.savefig("/home/kuliza227/github/Codeathons/abi/price.png")
        plt.show()
        #print(dataset["price"])


if __name__=="__main__":
    obj = ABB()
    dataset1 = obj.read_data1("")
    obj.plot_time_data(dataset)