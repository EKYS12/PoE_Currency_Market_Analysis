# Author: Yasser Siddiqui
'''
This script goes through the data dumps provided by poe.ninja and extracts the data needed for this project.
'''

# Imports
import pandas as pd
import os

# Functions
def currency_df(league):
    '''
    This function grabs the currency data for a stated league
    both for league softcore and standard softcore, and turns
    them into a pandas dataframe
    '''
    
    # Setting up the league's folder path
    path = f'./leagues/{league}/'

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


def exalt_df(currency_df):
    '''
    This function will take the full currency data for a league
    and extracts only the chaos orb to exalted orb ratio
    '''

    get_exalt_df = currency_df[currency_df['Get'] == 'Exalted Orb'].copy() 
    pay_exalt_df = currency_df[currency_df['Pay'] == 'Exalted Orb'].copy()

    exalt_df = pd.concat([get_exalt_df, pay_exalt_df])

    return exalt_df

def divine_df(currency_df):
    '''
    This function will take the full currency data for a league
    and extracts only the chaos orb to divine orb ratio
    '''

    get_divine_df = currency_df[currency_df['Get'] == 'Divine Orb'].copy() 
    pay_divine_df = currency_df[currency_df['Pay'] == 'Divine Orb'].copy()

    divine_df = pd.concat([get_divine_df, pay_divine_df])

    return divine_df

def mirror_df(currency_df):
    '''
    This function will take the full currency data for a league
    and extracts only the chaos orb to mirror ratio
    '''

    get_mirror_df = currency_df[currency_df['Get'] == 'Mirror of Kalandra'].copy() 
    pay_mirror_df = currency_df[currency_df['Pay'] == 'Mirror of Kalandra'].copy()

    mirror_df = pd.concat([get_mirror_df, pay_mirror_df])

    return mirror_df


# Code
league_path = './leagues/'
leagues = [d for d in os.listdir(league_path)]

df, df2 = currency_df(leagues[0])

perm_standard_df = pd.DataFrame(columns=df.columns)

perm_league_df = pd.DataFrame(columns=df.columns)

perm_standard_exalt = pd.DataFrame(columns=df.columns)

perm_league_exalt = pd.DataFrame(columns=df.columns)

perm_standard_divine = pd.DataFrame(columns=df.columns)

perm_league_divine = pd.DataFrame(columns=df.columns)

perm_standard_mirror = pd.DataFrame(columns=df.columns)

perm_league_mirror = pd.DataFrame(columns=df.columns)


del df
del df2

# Path of data folder
path = f'./data/leagues/'

for league in leagues:

    standard_df, league_df = currency_df(league)
    
    standard_exalt = exalt_df(standard_df)
    league_exalt = exalt_df(league_df)
    standard_divine = divine_df(standard_df)
    league_divine = divine_df(league_df)
    standard_mirror = mirror_df(standard_df)
    league_mirror = mirror_df(league_df)


    # saving individual league dataframes as parquet files

    league_dir = os.path.join(path, league)
    os.makedirs(league_dir, exist_ok=True)  # create directory if it does not exist

    league_df.to_parquet(f'{league_dir}/{league}.parquet', index = False)
    league_exalt.to_parquet(f'{league_dir}/{league}_exalt.parquet', index = False)
    league_divine.to_parquet(f'{league_dir}/{league}_divine.parquet', index = False)
    league_mirror.to_parquet(f'{league_dir}/{league}_mirror.parquet', index = False)
    
    perm_standard_df = pd.concat([perm_standard_df, standard_df])
    perm_league_df = pd.concat([perm_league_df, league_df])
    perm_standard_exalt = pd.concat([perm_standard_exalt, standard_exalt])
    perm_league_exalt = pd.concat([perm_league_exalt, league_exalt])
    perm_standard_divine = pd.concat([perm_standard_divine, standard_divine])
    perm_league_divine = pd.concat([perm_league_divine, league_divine])
    perm_standard_mirror = pd.concat([perm_standard_mirror, standard_mirror])
    perm_league_mirror = pd.concat([perm_league_mirror, league_mirror])

# Saving Dataframes as parquet files
path = f'./data/'

standard_dir = os.path.join(path, 'standard')
os.makedirs(standard_dir, exist_ok=True)  # create directory if it does not exist

perm_standard_df.to_parquet(os.path.join(standard_dir, 'standard.parquet'), index = False)
perm_standard_exalt.to_parquet(os.path.join(standard_dir, 'standard_exalt.parquet'), index = False)
perm_standard_divine.to_parquet(os.path.join(standard_dir, 'standard_divine.parquet'), index = False)
perm_standard_mirror.to_parquet(os.path.join(standard_dir, 'standard_mirror.parquet'), index = False)

compile_league_dir = os.path.join(path, 'compiled_league')
os.makedirs(compile_league_dir, exist_ok=True)  # create directory if it does not exist

perm_league_df.to_parquet(os.path.join(compile_league_dir, 'league.parquet'), index = False)
perm_league_exalt.to_parquet(os.path.join(compile_league_dir, 'league_exalt.parquet'), index = False)
perm_league_divine.to_parquet(os.path.join(compile_league_dir, 'league_divine.parquet'), index = False)
perm_league_mirror.to_parquet(os.path.join(compile_league_dir, 'league_mirror.parquet'), index = False)
