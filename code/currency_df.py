import pandas as pd

import os

def get_league_df(league='standard', currency='all'):
    '''
    This function serves to get the specific dataframe needed by
    the user at the time. It takes in which league the use wants to 
    work with and what currency they want to work with as arguements to
    retrieve the correct dataframe.
    '''
    path = os.path.join(path, f'{league}')

    if league != 'standard' & league != 'compile':
        if currency != 'all':
            for league_dir in listdir(path):
                if league == league_dir:
                    df = pd.read_parquet(os.path.join(path, f'{league}_{currency}.parquet'))
        else:
            for league_dir in listdir(path):
                if league == league_dir:
                    df = pd.read_parquet(os.path.join(path, f'{league}.parquet'))
    
        return df

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

