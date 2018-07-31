import os
import seaborn as sns
import numpy as np
import pandas as pd
from math import log
from scipy import stats

import sys

# sys.argv => filename
def process_excel(filename):
    df_kinetic_total = pd.read_excel(filename, sheet_name = 'Data')

    def get_hrs(time_str):
        h, m, s = time_str.split(':')
        return ((int(h) * 3600 + int(m) * 60 + int(s))/3600)

    def get_minutes(time_str):
        h,m,s = time_str.split(':')
        return (float(h)*60  + float(m) + float(s)/60)
    
    hrs_list = []
    min_list = []
    
    for time in df_kinetic_total['Time']:
        hrs_list.append(get_hrs(str(time)))
        min_list.append(get_minutes(str(time)))
        
    df_kinetic_total['hrs'] = hrs_list
    df_kinetic_total['mins'] = min_list
    
    WT_samples = ['C3', 'D3', 'E3']
    sample_1 = ['C4', 'D4', 'E4', 'C5', 'D5', 'E5', 'C6', 'D6', 'E6']
    sample_2 = ['C7', 'D7', 'E7', 'C8', 'D8', 'E8', 'C9', 'D9', 'E9']
    
    WT_df = df_kinetic_total.loc[:,WT_samples]
    sample_1_df = df_kinetic_total.loc[:, sample_1]
    sample_2_df = df_kinetic_total.loc[:, sample_2]
    
    WT_df_avg = pd.DataFrame()
    WT_df_avg['avg'] = WT_df.mean(axis=1)
    WT_df_avg['std'] = WT_df.std(axis=1)
    WT_df_avg['Hours'] = df_kinetic_total['hrs']
    WT_df_avg['sample'] = 'WT'
    
    
    sample_1_df_avg = pd.DataFrame()
    sample_1_df_avg['avg'] = sample_1_df.mean(axis =1)
    sample_1_df_avg['std'] = sample_1_df.std(axis=1)
    sample_1_df_avg['Hours'] = df_kinetic_total['hrs']
    sample_1_df_avg['sample'] ='D3_1'
    
    sample_2_df_avg = pd.DataFrame()
    sample_2_df_avg['avg'] = sample_2_df.mean(axis=1)
    sample_2_df_avg['std'] = sample_2_df.std(axis=1)
    sample_2_df_avg['Hours'] = df_kinetic_total['hrs']
    sample_2_df_avg['sample'] = 'D3_2'
    
    
    data_dfs = [WT_df_avg, sample_1_df_avg, sample_2_df_avg]
    data_final = pd.concat(data_dfs)
    data_final['time'] = df_kinetic_total['hrs']

    data_final.to_csv('growth_kinetic.csv')

if __name__ == '__main__':
    process_excel(sys.argv[1])
