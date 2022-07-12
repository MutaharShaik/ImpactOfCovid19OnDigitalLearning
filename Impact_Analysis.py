# Import related libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os, glob
import plotly.express as px
# from fontTools.misc.symfont import y
from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)




import os
for dirname, _, filenames in os.walk('/Users/mohammedmutaharshaik/Desktop/ImpactofCovid19_OnDigitalLearning/resources'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# Load products_info data file
product_info = pd.read_csv(r'/Users/mohammedmutaharshaik/Desktop/ImpactofCovid19_OnDigitalLearning/resources/products_info.csv')
# Load districts_info data file
districts_info = pd.read_csv(r'/Users/mohammedmutaharshaik/Desktop/ImpactofCovid19_OnDigitalLearning/Resources/districts_info.csv')
districts_info['pct_black/hispanic']=districts_info['pct_black/hispanic'].astype('str')
districts_info['pct_free/reduced']=districts_info['pct_free/reduced'].astype('str')
districts_info['county_connections_ratio']=districts_info['county_connections_ratio'].astype('str')
districts_info['pp_total_raw']=districts_info['pp_total_raw'].astype('str')
# 'pct_free/reduced','county_connections_ratio','pp_total_raw'
mapping_1 = {
    '[0, 0.2[': '0%-20%',
    '[0.2, 0.4[': '20%-40%',
    '[0.4, 0.6[': '40%-60%',
    '[0.6, 0.8[': '60%-80%',
    '[0.8, 1[': '80%-100%'}
mapping_2 = {
    '[4000, 6000[': '4000-6000',
    '[6000, 8000[': '6000-8000',
    '[8000, 10000[': '8000-10000',
    '[10000, 12000[': '10000-12000',
    '[12000, 14000[': '12000-14000',
    '[14000, 16000[': '14000-16000',
    '[16000, 18000[': '16000-18000',
    '[18000, 20000[': '18000-20000',
    '[20000, 22000[': '20000-22000',
    '[22000, 24000[': '22000-24000',
    '[32000, 34000[': '32000-34000'}
mapping_3 =mapping_3 = {
    '[0.18, 1[': '18%-100%',
    '[1, 2[': '100%-200%'
}
districts_info['pct_black/hispanic'] = districts_info['pct_black/hispanic'].map(mapping_1)
districts_info['pct_free/reduced'] = districts_info['pct_free/reduced'].map(mapping_1)
districts_info['county_connections_ratio'] = districts_info['county_connections_ratio'].map(mapping_3)
districts_info['pp_total_raw'] = districts_info['pp_total_raw'].map(mapping_2)
engagement_merged=pd.DataFrame()
address = glob.glob('/Users/mohammedmutaharshaik/Desktop/ImpactofCovid19_OnDigitalLearning/resources/engagementData/*.csv')
count=0
for i in address:
    with open(i, "rb") as data_of_files:
        data=pd.read_csv(data_of_files)
        engagement_merged=pd.concat([engagement_merged,data], axis=0)
        count=count+1
        if count==233:
            break
