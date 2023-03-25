from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import requests
import logging
import pyodbc
import pytz


# This function is written to connect to the database...
def connectDB():
    try:
        filename = "external.config"
        data = open(filename).read()
        credentials = eval(data)
        server = credentials['server']
        database = credentials['database']
        user = credentials['user']
        driver = credentials['driver']
        password = credentials['password']

        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + user + ';PWD=' + password)
        logging.info(conn)
        return conn

    except Exception as e:
        logging.info("Error occurred in connectDB function", e)
        print("Error Occurred: ", e)


# This function is written to get the data from the website...
def getData():

    holidays = []

    try:
        URL = 'https://www.icicidirect.com/ilearn/stocks/articles/nse-holidays-2023'
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, 'html.parser')
        contentTable = soup.find_all('table')

        for i in range(0, 2):
            table = contentTable[i]
            rows = table.find_all('tr')
            for i in range(1, len(rows)):
                row = rows[i]
                tds = row.find_all('td')
                group = {
                    'Holidays':tds[1].get_text(),
                    'Date':tds[2].get_text(),
                    'Day':tds[3].get_text(),
                }
                holidays.append(group)
                logging.info(group)

        return holidays

    except Exception as e:
        logging.info("Error occurred in getData function" , e)
        print("Some error occurred: ", e)


# This function is written to transform the data and remove the '/n' from the table scrapped...
def transformData(holidays):

    try:
        df = pd.DataFrame(holidays)
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
        print(df)
        return df
    except Exception as e:
        logging.info("Error occurred in transformData function" , e)
        print("Error Occurred: ", e)


# This function is written to load the data to the database...
def loadDataToDB(df):
    try:

        conn = connectDB()
        cursor = conn.cursor()

        for idx in df.index:
            # Here getting timeStamp according to timeZone...
            timezone = pytz.timezone('Asia/Kolkata')
            string = str(dt.datetime.now(timezone))
            # Writing SQL Query
            sql_cmd_temp = "INSERT INTO [dbo].[holiday_details] (Holiday , Date , Day , TimeStamp) VALUES(? , ? , ? , " \
                           "?);"
            cursor.execute(sql_cmd_temp, df['Holidays'][idx], df['Date'][idx], df['Day'][idx], string)
            logging.info("Inserting Holiday to DB")

    except Exception as e:
        logging.info("Error Occurred in Load data function", e)
        print("Error Occurred : ", e)

    finally:
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == "__main__":

    try:
        logging.basicConfig(filename="task_1_logger", level= logging.DEBUG,
                            format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
        holidays = getData()
        df = transformData(holidays)
        loadDataToDB(df)

    except Exception as e:
        logging.info("Error occurred in main function" , e)
        print("OOPS! , Something went wrong")







