import yfinance as yf
import datetime
import pandas as pd
from matplotlib import pyplot as plt
import mplfinance as mpl


ticket = "^TWII"
str_start="2023-08-01"
data = yf.download(ticket, start=str_start, end=datetime.date.today())
print(data)

symbol = yf.Ticker(ticket)
print(symbol.history(period="1wk").info())

# 數據資料使用 pandas DataFrame 分析
pd_data= pd.DataFrame(data)
print(pd_data)
print(pd_data.index) # 資料索引
pd_data.to_csv("2330_tw.csv") # 轉存 csv 檔
print("==================================================================================================")
print(pd_data.loc['2023-08-25']) # 取指定日期資料
print(len(pd_data))
print(pd_data.iloc[17])  # 取指定日期資料
print(pd_data.iloc[:]) # python 切片特性
print("==================================================================================================")
symbol = yf.Ticker(ticket)
history_data = symbol.history(period="5y")
pd_data= pd.DataFrame(history_data)
print(pd_data.sort_values("Dividends", ascending=True)) # 排序低至高 近五年現金分紅
print("==================================================================================================")
pd_data.sort_values("Dividends", ascending=True)
# pd_data["Close"].plot() # 使用 matplot 畫收盤價
# plt.show()
print("==================================================================================================")
mpl.plot(pd_data, type="line") # 使用金融分析可視化模組 畫K線圖
plt.show()