import pandas as pd
import numpy as np

import os

def league_df(league='standard', currency='all'):
    '''
    This function serves to get the specific dataframe needed by
    the user at the time. It takes in which league the use wants to 
    work with and what currency they want to work with as arguements to
    retrieve the correct dataframe.
    '''

    path = '../data/'

    if (league != 'standard') & (league != 'compiled'):
        if currency != 'all':
            df = pd.read_parquet(os.path.join(path, f'leagues/{league}/{league}_{currency}.parquet'))
        else:
            df = pd.read_parquet(os.path.join(path, f'leagues/{league}/{league}.parquet'))
    
        return df

    path = os.path.join(path, f'{league}')

    if league == 'compiled':
        if currency != 'all':
            df = pd.read_parquet(os.path.join(path, f'league_{currency}.parquet'))
        else:
            df = pd.read_parquet(os.path.join(path, f'league.parquet'))
    
        return df
    
    if league == 'standard':
        if currency != 'all':
            df = pd.read_parquet(os.path.join(path, f'standard_{currency}.parquet'))
        else:
            df = pd.read_parquet(os.path.join(path, f'standard.parquet'))
    
        return df

def trade_ratio(df):
    '''
    This function takes a raw df and produces new columns in the dataframe
    for the ratio of trade between the two currencies.
    '''

    df['Ratio Label'] = np.nan
    df['Ratio'] = np.nan

    df['Ratio Label'] = df.apply(lambda row: row['Get'][0] + '-' + row['Pay'][0], axis=1)
    df['Ratio'] = np.where(df['Get'] == 'Chaos Orb', 1/df['Value'], df['Value'])

    return df

def day_count(df):
    '''
    This function takes the df and gives it a day column that counts the
    numerical day of the league.
    '''

    unique_dates = sorted(set(df['Date']))

    day_count_dict = {Date: i+1 for i, Date in enumerate(unique_dates)}
    
    df['Day'] = df['Date'].map(day_count_dict)

    return df
