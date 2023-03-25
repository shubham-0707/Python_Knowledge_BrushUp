from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import requests
import pyodbc
import pytz


try:
    URL = 'https://www.icicidirect.com/ilearn/stocks/articles/nse-holidays-2023'
    content = requests.get(URL)
except Exception as e:
    print("Error occured: ", e)


try:
    soup = BeautifulSoup(content.text,'html.parser')
except Exception as e:
    print("Error Occured: ", e)


try:
    contentTable = soup.find_all('table')
    table1 = contentTable[0]
    rows = table1.find_all('tr')
except Exception as e:
    print("Error occured: ", e)


#this is table 1 i.e. Table for all the holidays occuring on non Saturday and Sunday...

holidays = []
try:
    for i in range(1 , len(rows)):
        row = rows[i]
        tds = row.find_all('td')
        group= {
            'Holidays':tds[1].get_text(),
            'Date':tds[2].get_text(),
            'Day':tds[3].get_text(),
        }
        holidays.append(group)
except Exception as e:
    print("Error Occured: ", e)


#This is table 2 i.e. Holidays occuring on Saturdays and Sundays...
try:
    table2 = contentTable[1]
    rows = table2.find_all('tr')
    for i in range(1, len(rows)):
        row = rows[i]
        tds = row.find_all('td')
        group = {
            'Holidays':tds[1].get_text(),
            'Date':tds[2].get_text(),
            'Day':tds[3].get_text(),
        }
        holidays.append(group)

except Exception as e:
    print("Error Occured: ", e)


try:
    df = pd.DataFrame(holidays)
    df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
    print(df)
except Exception as e:
    print("Error Occured: ", e)


# Connecting with database and inserting data to the table. The SQL Server is hosted on Microsoft Azure...
try:
    driver = '{ODBC Driver 17 for SQL Server}'
    server = "sqlserver0707.database.windows.net"
    database = "Holidays"
    user = "shubham"
    password = "1237Aman"

    for idx in df.index:
        # Here getting timeStamp according to timeZone...
        timezone = pytz.timezone('Asia/Kolkata')
        string = str(dt.datetime.now(timezone))

        # Writing SQL Query
        sql_cmd_temp = "INSERT INTO [dbo].[holiday_details] (Holiday , Date , Day , TimeStamp) VALUES(? , ? , ? , ?);"
        conn = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + user + ';PWD=' + password)
        cursor = conn.cursor()
        cursor.execute(sql_cmd_temp, df['Holidays'][idx], df['Date'][idx], df['Day'][idx], string)
        conn.commit()
        cursor.close()
        conn.close()

except Exception as e:
    print("Error Occured : ", e)



