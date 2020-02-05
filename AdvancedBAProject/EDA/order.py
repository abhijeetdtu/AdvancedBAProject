%load_ext autoreload
%autoreload 2

from AdvancedBAProject.Utils.getData import getOrderData , getProductData

import pandas as pd
from plotnine import *

df = getOrderData()

df.head()
df.shape[0]

smDf = df.sample(10000)

groupedAgg = smDf.groupby("ORDER_PLATFORM") \
                 .agg(ORDER_COUNT = ("ORDER_NBR" , "count")
                  , TOTAL_LINE_AMT_MEAN = ("TOTAL_LINE_AMT" , "mean")
                  , TOTAL_LINE_AMT_SUM = ("TOTAL_LINE_AMT" , "sum"))

groupedAgg = groupedAgg.reset_index()

(ggplot(groupedAgg , aes(x="ORDER_PLATFORM" , y="ORDER_COUNT")) + geom_col() )

(ggplot(groupedAgg , aes(x="ORDER_PLATFORM" , y="TOTAL_LINE_AMT_MEAN" )) + geom_col() )


(ggplot( groupedAgg, aes(x = "ORDER_PLATFORM" , y="TOTAL_LINE_AMT_SUM")) + geom_col())


productsDf = getProductData()

orderProduct = pd.merge(productsDf , smDf , on="PRODUCT_NBR")
orderProduct


(ggplot( orderProduct,
   aes(x = "ORDER_PLATFORM" , y="TOTAL_LINE_AMT" , color="PRODUCT_CATEGORY"))
 + geom_jitter())


brandGroup = orderProduct.groupby(["BRAND_NAME" , "PRODUCT_CATEGORY"]) \
                         .agg(unitsSold = ("ORDER_NBR" , "count")
                             ,totalAmount = ("TOTAL_LINE_AMT" , "sum"))
brandGroup = brandGroup.reset_index()

topBrands = brandGroup.sort_values("totalAmount" , ascending=False).head(20)

(ggplot(topBrands,
   aes(x = "totalAmount" , y="unitsSold" , color="BRAND_NAME"))
 + geom_point())


categoryByPlatform = orderProduct.groupby(["PRODUCT_CATEGORY" , "ORDER_PLATFORM"]) \
                         .agg(unitsSold = ("ORDER_NBR" , "count")
                             ,totalAmount = ("TOTAL_LINE_AMT" , "sum"))

categoryByPlatform = categoryByPlatform.reset_index()
(ggplot(categoryByPlatform,
   aes(x = "ORDER_PLATFORM" , y="PRODUCT_CATEGORY" , fill="totalAmount"))
 + geom_tile())


(ggplot(orderProduct,
   aes(x = "ORDER_TIME_INT/(60*60)" , y="ORDER_PLATFORM" , size="TOTAL_LINE_AMT" , color="PRODUCT_CATEGORY"))
 + geom_point())


(ggplot(orderProduct,
   aes(x = "ORDER_TIME_INT/(60*60)" , y="TOTAL_LINE_AMT" , color="PRODUCT_CATEGORY"))
 + geom_line()
 + facet_wrap("~ORDER_PLATFORM" , ncol=1))
