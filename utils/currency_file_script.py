# Author: Yasser Siddiqui
'''
This script goes through the data dumps provided by poe.ninja and extracts the data needed for this project.
It then compiles the data into 2 different data frames and stores them as parquet files.
'''

# Imports
import pandas as pd
import os

# Functions
def currency_df(league):
    '''
    This function grabs the currency data for a stated league
    both for softcore trade challenge league and softcore standard
    trade league, and turns them into pandas dataframes
    '''
    
    # Setting up the league's folder path
    path = f'../leagues/{league}/'

    for file in os.listdir(path):
        if 'Hardcore' in file:
            continue
        if 'items' in file:
            continue

        file_path = os.path.join(path, file)

        if 'Standard' in file:
            standard_df = pd.read_csv(file_path, delimiter = ';')
            standard_df['Date'] = pd.to_datetime(standard_df['Date'])

        else:
            league_df = pd.read_csv(file_path, delimiter = ';')
            league_df['Date'] = pd.to_datetime(league_df['Date'])

    return standard_df, league_df

# Code
league_path = '../leagues/'
leagues = [d for d in os.listdir(league_path)]

df, df2 = currency_df(leagues[0])

compiled_standard_df = pd.DataFrame(columns=df.columns)

compiled_league_df = pd.DataFrame(columns=df.columns)

del df
del df2

# Path of data folder
path = f'../leagues/'

# Making the two different compiled dataframes
for league in leagues:

    standard_df, league_df = currency_df(league)

    compiled_standard_df = pd.concat([compiled_standard_df, standard_df])
    compiled_league_df = pd.concat([compiled_league_df, league_df])

# Saving Dataframes as parquet files
path = f'../data/'

compiled_standard_df.to_parquet(os.path.join(path, 'standard.parquet'), index = False)

compiled_league_df.to_parquet(os.path.join(path, 'league.parquet'), index = False)
