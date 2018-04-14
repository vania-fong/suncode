#!/usr/bin/env python3

import pandas as pd

def read_as_dict(data_df, key):
    keys = data_df[key]
    columns = data_df.columns.tolist()
    d = {}

    for i in range(len(keys)):
        d[keys[i]] = {}
        for c in columns:
            if c != key:
                d[keys[i]][c] = data_df[c][i]

    return d

def add_cols(data_df, source_dict, key):
    columns = data_df.columns.tolist()

    for i in range(len(data_df['JobId'])):
        
        k = data_df[key][i]
        print(str(k))
        # for c in source_dict[k].keys():
        #     if c not in columns:
        #         data_df[c] = 0
        #         columns.append([c])
        #     data_df[c][i] = source_dict[k][c]

data_installed = pd.read_csv('data/PV_installed_customer_details.csv', sep=',', encoding='ISO-8859-1')
data_cancelled = pd.read_csv('data/PV_cancelled_customer_details.csv', sep=',', encoding='ISO-8859-1')

factors = [
    'JobId',
    'EngineeringSoldkWSize',
    'EngineeringSoldAnnualkWh',
    'EnergyConsumption',
#    'Region',
#    'State',
#    'Zip',
#    'Latitude',
#    'Longitude',
#    'AHJ',
#    'RoofType',
    'RoofSqFoot',
    'NumMountingPlanes',
    'NumPanels',
#    'Utility',
#    'ProductTypeAlt',
    'PowerwallCount',
    'UtilityCostPerKWh',
    'OldBill',
    'UtilityRatePlanId',
    'UtilityInflationRate',
    'GasRatePlanID',
    'AverageShading',
    'Reroof',
    'MPU',
#    'NumStories',
]

data_installed = data_installed[factors]
data_cancelled = data_installed[factors]
data_installed['Status'] = 1
data_cancelled['Status'] = 0
data_combined = data_installed.append(data_cancelled)

# data_sunlight = pd.read_csv('data/Google Sunroof_Yearly_Sunlight_by_State.csv', sep=',', encoding='ISO-8859-1')
# data_sunlight = read_as_dict(data_df=data_sunlight, key='State')

# add_cols(data_df=data_combined, source_dict=data_sunlight, key='State')

# print(data_combined.head(n=5))

# for row in range(len(data_combined['JobId'])):
#     
#     state_row = list(data_sunlight['State']).index(state)
#     data_combined['yearly_sunlight_kwh_kw_threshold_avg'][row] = data_sunlight['yearly_sunlight_kwh_kw_threshold_avg'][state_row]

# print(data_combined.head(n=5))

data_out = data_combined.head(n=100).append(data_combined.tail(n=100))
data_out.to_csv('data_combined.csv',sep=',')
