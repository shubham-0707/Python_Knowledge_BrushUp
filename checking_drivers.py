import mysql.connector
from sqlalchemy import create_engine
import pymysql

from bs4 import BeautifulSoup
import requests

URL = 'https://www.icicidirect.com/ilearn/stocks/articles/nse-holidays-2023'
content = requests.get(URL)

soup = BeautifulSoup(content.text ,'html.parser')


contentTable = soup.find_all('table')
table1 = contentTable[0]
rows = table1.find_all('tr')


import pandas as pd
holidays = []
import datetime as dt
import pytz
timezone = pytz.timezone('Asia/Kolkata')
timestamp = pd.Series([dt.datetime.now(timezone)])


#this is table 1 i.e. Table for all the holidays occuring on non Saturday and Sunday...

for i in range(1 , len(rows)):
    row = rows[i]
    tds = row.find_all('td')
    group= {
        'Holidays':tds[1].get_text(),
        'Date':tds[2].get_text(),
        'Day':tds[3].get_text(),
        'TimeStamp':timestamp[0]
    }
    holidays.append(group)



#This is table 2 i.e. Holidays occuring on Saturdays and Sundays...

table2 = contentTable[1]
rows = table2.find_all('tr')
for i in range(1, len(rows)):
    row = rows[i]
    tds = row.find_all('td')
    group = {
        'Holidays':tds[1].get_text(),
        'Date':tds[2].get_text(),
        'Day':tds[3].get_text(),
        'TimeStamp':timestamp[0]
    }
    holidays.append(group)


df = pd.DataFrame(holidays)
print(df)

mydb = mysql.connector.connect(
        host="localhost",
        user="root@",
        password=""
)
print(mydb)


hostname="localhost"
dbname="web_scrapping"
uname="root@"
pwd=""

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))
df.to_sql('holiday_details', engine, index=False, if_exists='append')



