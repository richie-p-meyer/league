import gdown
import pandas as pd
import numpy as np

def update_df():
    '''
    Download most recent csv file, concat with rest of data, return the full df
    '''
    output = "lol_2023.csv" #What to save the downloaded file as
    id = "1XXk2LO0CsNADBB1LRGOV5rUpyZdEZ8s2" #The id from the google drive file
    gdown.download(id=id, output=output, quiet=False)
    
    df_2021 = pd.read_csv('lol_2021.csv')
    df_2022 = pd.read_csv('lol_2022.csv')
    df_2023 = pd.read_csv('lol_2023.csv')
    df = pd.concat([df_2021,df_2022,df_2023])
    return df

def get_wiki():
    '''
    Returns chart from wikipedia containing info for Tier 1 and Tier 2 leagues
    Returns tier1, tier2
    '''
    wiki = pd.read_html('https://en.wikipedia.org/wiki/List_of_League_of_Legends_leagues_and_tournaments')
    return wiki[1], wiki[3]

def wrangle_df(df):
    leagues = ['LCK','LPL','LEC','LCS','PCS','VCS','CBLOL','LJL','LLA'] # These are my 9 tier 1 leagues that I'll keep
    
    df = df[df.league.isin(leagues)]
    df = df[df.position=='team']

    cols = ['teamname','league', 'date', 'side', 'gamelength','game', 'result', 'teamkills', 
            'teamdeaths', 'firstblood', 'position', 'dragons', 'barons', 'opp_barons','towers', 'opp_towers', 
            'inhibitors', 'opp_inhibitors', 'damagetochampions', 'damagetakenperminute', 'wardsplaced', 'wardskilled', 
            'controlwardsbought', 'totalgold', 'gspd']

    df = df[cols]
    df = df.dropna()
    
    df.date = pd.to_datetime(df.date,infer_datetime_format=True)
    del df['position']
    df = df.sort_values(['date','game'])
    df = df.reset_index(drop=True)
    df.side = np.where(df.side=='Blue',1,0)
    df.rename(columns={'side':'blue_side'},inplace = True)
    
    df.to_csv('final.csv')
    
    return df

def get_train(df):
    train_len = int(df.shape[0]*.6)
    train = df.iloc[:train_len]
    return train

def create_target(groupby):
    groupby['target']=groupby['result'].shift(-1)
    return groupby

def add_target(df):
    df = df.groupby('teamname').apply(create_target)
    df.loc[pd.isnull(df.target),'target'] =2
    df.target = df.target.astype(int,errors='ignore')
    return df

def add_opp_name(df): #tup = list of tuples
    # Create an 'opp_name' column for each row
    evens = range(0,df.shape[0],2)
    odds = range(1,df.shape[0],2)
    tup = [(a,b) for a,b in zip(evens,odds)] # list of tuples
    
    for t in tup: #iterate through list of tuples
        a,b= t #unpack each tuple into two values
        df.loc[a,'opp_name']=df.teamname.loc[b] #create new column w/opp_name
        df.loc[b,'opp_name']=df.teamname.loc[a]
        
    return df

def rolling(team):
    rolling = team.rolling(10).mean()
    return rolling

def add_rolling(df):
    cols = ['gamelength','teamkills','teamdeaths','firstblood','dragons','barons','opp_barons','towers','opp_towers',\
       'inhibitors','opp_inhibitors','damagetochampions','damagetakenperminute','wardsplaced','wardskilled',\
       'controlwardsbought','totalgold','gspd']

    df_rolling=df[list(cols)+['teamname']]
    
    
    df_rolling = df_rolling.groupby('teamname',group_keys=False)[cols].apply(rolling)

    rolling_cols = [f'{col}_rolling' for col in df_rolling.columns]
    df_rolling.columns = rolling_cols
    df = pd.concat([df,df_rolling],axis=1)
    return df.dropna()

def next_opp(team):
    team['next_opp'] = team['opp_name'].shift(-1)
    return team
def add_opp(df):
    df = df.groupby('teamname').apply(next_opp)
    df.loc[df.next_opp.isnull(),'next_opp'] = 2
    return df

def next_side(team):
    team['next_blue'] = team['blue_side'].shift(-1)
    return team

def add_next_side(df):
    df = df.groupby('teamname').apply(next_side)
    df.loc[df.next_blue.isnull(),'next_blue']=2
    df.next_blue = df.next_blue.astype(int,errors='ignore')
    return df

def next_date(team):
    team['next_date'] = team['date'].shift(-1)
    return team

def add_next_date(df):
    df = df.groupby('teamname').apply(next_date)
    df.loc[df.next_date.isnull(),'next_date']=2
    return df