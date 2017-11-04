import pandas as pd
import numpy as np
import datetime as dt

reading = pd.read_csv('reading.csv')
reading["created_at"]=reading["created_at"].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%dT%H:%M:%S.%f') if len(x)>21 else dt.datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'))
reading["tracking_time"]=reading["tracking_time"].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%dT%H:%M:%S.%f') if len(x)>21 else dt.datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'))
stories = pd.read_csv('stories.csv', sep=';')
stories.rename(columns={"id":"story_id"},inplace=True)
visits = pd.read_csv('visits.csv')

reading_s = pd.merge(reading,stories,how="left", on=["story_id"],).query("category_one=='horror' | category_two=='horror' ")
reading_s["date"]=reading_s["created_at"].apply(lambda x:x.date())

reading_s_h = reading_s.groupby(["visitor_id","date"], ).aggregate({
        'visitor_id': 'count',
    }).rename(columns={'visitor_id': 'quantity_by_day'})

print('Question: how much did they read?, considering that the quantity is entries per visitor')
print(reading_s_h)

reading_s['time']=((reading_s['created_at']-reading_s['tracking_time']).dt.total_seconds())
reading_s_h_time = reading_s.groupby(["visitor_id","date"], ).aggregate({
        'time': np.sum,
    }).rename(columns={'time': 'seconds_by_day'})

print("Question: how much did they read?, considering that the quantity is seconds on the page and there's the posibility to make de calculation with the given variables")
print(reading_s_h_time)

reading_s_reader_day = reading_s.groupby(["date","visitor_id"], ).aggregate({
        'visitor_id': 'count',
    }).groupby(["date"]).aggregate({
        'visitor_id': 'count',
    }).rename(columns={'visitor_id': 'readers_by_day'})

print('Question: how many readers are there?')
print(reading_s_reader_day)

reading_s_countries = pd.merge(reading_s,visits,how='left', on = ['visitor_id'])
reading_s_countries.loc[pd.isnull(reading_s_countries['country']),'country'] = "Null"
reading_s_countries = reading_s_countries.groupby(["visitor_id","country"], ).aggregate({
       'visitor_id': 'count',
    }).rename(columns={'visitor_id': 'readers'})
reading_s_countries.reset_index(inplace=True)
reading_s_countries.drop(axis=1,labels=["readers"], inplace = True)
reading_s_countries

print('Question: what country are the readers from?')
print(reading_s_countries)
