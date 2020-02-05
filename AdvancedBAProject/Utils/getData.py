import os
import pathlib
import pandas as pd
import datetime
from plotnine import *


def getPath():
    try:
        __file__
        path = __file__
    except Exception as e:
        path = pathlib.Path().resolve()
        path = os.path.abspath(os.path.join(path ,"AdvancedBAProject", "Utils" , "getData.py"))
    return path

path = getPath()
dirPath = os.path.abspath(os.path.dirname(path))
dataPath = os.path.abspath(os.path.join(dirPath , ".." , "Data"))

def _toTimeInt(val):
     hours, minutes, seconds = [int(x) for x in val.split(':')]
     x = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
     return x.seconds

def getOrderData():
    orderPath = os.path.abspath(os.path.join(dataPath , "order_master.csv"))
    df = pd.read_csv(orderPath)
    df["ORDER_DATE"] = pd.to_datetime(df["ORDER_DATE"] , format="%Y-%m-%d")
    df["ORDER_TIME_INT"] = df["ORDER_TIME"].apply(_toTimeInt)
    return df


def getProductData():
    orderPath = os.path.abspath(os.path.join(dataPath , "product_master.csv"))
    df = pd.read_csv(orderPath)
    return df
