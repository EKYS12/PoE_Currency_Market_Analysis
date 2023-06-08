import pandas as pd
import numpy as np

import os

def league_df(league='standard', currency='all'):
    '''
    This function serves to get the specific dataframe needed by
    the user at the time. It takes in which league the use wants to 
    work with and what currency they want to work with as arguements to
    retrieve the correct dataframe.

    league: Default 'standard', but can also put in a challenge league.

    currency: Default 'all', but can put in a specific currency instead.
    '''

    path = '../data/'

    if league == 'standard':
        df = pd.read_parquet(os.path.join(path, 'standard.parquet'))
    else:
        df = pd.read_parquet(os.path.join(path, 'league.parquet'))
        df = df[df['League'] == league].copy()

    if currency != 'all':
        df1 = df[df['Get'] == currency].copy()
        df2 = df[df['Pay'] == currency].copy()
        df = pd.concat([df1, df2])

    return df
    
def trade_ratio(df, average=False):
    '''
    This function takes a raw df and produces new columns in the dataframe
    for the ratio of trade between the two currencies.

    df: dataframe being transformed.
    '''

    df['Ratio'] = np.nan

    df['Ratio'] = np.where(df['Get'] == 'Chaos Orb', 1/df['Value'], df['Value'])

    if average:
        df = average_ratio(df)

    return df

def average_ratio(df):
    '''
    This function takes the 2 different ratios that are gotten from the
    trade_ratio function and returns an average trade ratio between the two.

    This function is only for dataframes that only contain rows of observations
    between chaos orbs and one other currency. It should not be used on a dataframe
    with multiple different currencies.

    df: dataframe being transformed.
    '''

    df = df.groupby('Date', as_index=False).agg({'Ratio': 'mean'})

    return df
    

def league_day(df):
    '''
    This function takes the df and gives it a day column that counts the
    numerical day of the league.

    df: dataframe being transformed.
    '''

    unique_dates = sorted(set(df['Date']))

    day_count_dict = {Date: i+1 for i, Date in enumerate(unique_dates)}
    
    df['Day'] = df['Date'].map(day_count_dict)

    return df

