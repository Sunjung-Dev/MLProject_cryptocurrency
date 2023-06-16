from upbit import Upbit
import matplotlib.pyplot as plt

# y축은 종가, x 축은 24시간이기 대문에 24시간에 대한 시간 
# 10일치 데이터의 평균 

def get_min_data():
    time_for_data = dict()
    upbit_b = Upbit()
    json_data = upbit_b.fetch_as_df("KRW-BTC")
    for i in range(len(json_data)):
        time_format = json_data.iloc[i]['Time'].split("T")[1]
        time_for_data[time_format] = 0
        # 시간별로의 종가 계산 
        time_for_close_value = 0
        for j in range(0, len(json_data), 24):
            time_for_close_value += json_data.iloc[j]['Close']
        time_for_data[time_format] = time_for_close_value
    return time_for_data

def data_for_matplotlib(data):
    return 


if __name__ == "__main__":
    get_min_data()


