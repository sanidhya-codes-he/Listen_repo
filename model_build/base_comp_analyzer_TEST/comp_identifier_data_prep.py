import numpy as np
import pandas as pd
import xgboost as xgb

fan_id_00_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id00_abnormal")
fan_id_00_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id00_normal")
fan_id_02_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id02_abnormal")
fan_id_02_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id02_normal")
fan_id_04_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id04_abnormal")
fan_id_04_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id04_normal")
fan_id_06_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id06_abnormal")
fan_id_06_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\fan_csv\\fan_id06_normal")

pump_id_00_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_00_abnormal")
pump_id_00_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_00_normal")
pump_id_02_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_02_abnormal")
pump_id_02_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_02_normal")
pump_id_04_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_04_abnormal")
pump_id_04_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_04_normal")
pump_id_06_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_06_abnormal")
pump_id_06_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\pump_csv\\pump_id_06_normal")

slider_id_00_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_00_abnormal")
slider_id_00_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_00_normal")
slider_id_02_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_02_abnormal")
slider_id_02_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_02_normal")
slider_id_04_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_04_abnormal")
slider_id_04_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_04_normal")
slider_id_06_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_06_abnormal")
slider_id_06_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\slider_csv\\slider_id_06_normal")

valve_id_00_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id00_abnormal")
valve_id_00_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id00_normal")
valve_id_02_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id02_abnormal")
valve_id_02_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id02_normal")
valve_id_04_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id04_abnormal")
valve_id_04_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id04_normal")
valve_id_06_abnormal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id06_abnormal")
valve_id_06_normal = pd.read_csv("C:\\Users\\sanid\\PycharmProjects\\Listen\\Listen_repo\\valve_csv\\valve_id06_normal")

valve = pd.concat([valve_id_04_abnormal,valve_id_04_normal,valve_id_02_abnormal,valve_id_02_normal,valve_id_06_abnormal,valve_id_06_normal,valve_id_00_abnormal,valve_id_00_normal],ignore_index=True)

slider = pd.concat([slider_id_04_abnormal,slider_id_04_normal,slider_id_02_abnormal,slider_id_02_normal,slider_id_06_abnormal,slider_id_06_normal,slider_id_00_abnormal,slider_id_00_normal],ignore_index=True)

pump = pd.concat([pump_id_04_abnormal,pump_id_04_normal,pump_id_02_abnormal,pump_id_02_normal,pump_id_06_abnormal,pump_id_06_normal,pump_id_00_abnormal,pump_id_00_normal],ignore_index=True)

fan = pd.concat([fan_id_04_abnormal,fan_id_04_normal,fan_id_02_abnormal,fan_id_02_normal,fan_id_06_abnormal,fan_id_06_normal,fan_id_00_abnormal,fan_id_00_normal],ignore_index=True)

valve['comp_id'] = 0
slider['comp_id'] = 1
pump['comp_id'] = 2
fan['comp_id'] = 3

data = pd.concat([valve,slider,pump,fan],ignore_index=True)

data.to_csv("allComp_data.csv",index=False)

