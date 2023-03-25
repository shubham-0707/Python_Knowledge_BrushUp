import datetime as dt
import pandas as pd
import logging
import pyodbc
import pytz


# This function is made to make a connection with the Azure SQL Database hosted on Azure Portal
def connectDB():
    try:
        filename = "external.config"
        data = open(filename).read()
        content = eval(data)
        driver = content['driver']
        database = content['database']
        user = content['user']
        password = content['password']
        server = content['server']
        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' +
                              user + ';PWD=' + password)
        logging.info(conn)
        return conn
    except Exception as e:
        logging.info("Error Occurred in connectDB function", e)
        print('Something went wrong')


# This function is made to load the whole chunk at once to the 'NSE Data' database.
def loadData(records, cursor):
    try:
        # Writing SQL Query
        sql_cmd_temp = "INSERT INTO [dbo].[StockInfo] (Index_Name , Index_Date , Open_Index , High_Index , Low_Index " \
                       ", Closing_Index , Points_Change , Change_Percentage , Volume , TurnOver , PbyE , PbyB , " \
                       "Div_Yield , TimeStamp) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ?);"
        cursor.executemany(sql_cmd_temp , records)
        logging.info("inserting chunk to DB i.e. NSEData")

    except Exception as e:
        logging.info("Error Occurred in loadData", e)
        print("Something went wrong", e)


if __name__ == "__main__":

    try:
        df = pd.read_csv("NSE_Daily_date.csv", chunksize=20)
        logging.basicConfig(filename="task_2_logger", level=logging.DEBUG,
                            format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
        conn = connectDB()
        cursor = conn.cursor()

        for chunk in df:

            # Here getting timeStamp according to timeZone...
            timezone = pytz.timezone('Asia/Kolkata')
            string = str(dt.datetime.now(timezone))

            # Converting chunk again to a DataFrame...
            temp = pd.DataFrame(chunk)

            # Adding the timeStamp column in the dataframe...
            temp['TimeStamp'] = string

            # Making list of all the rows in a chunk to process at once...
            records = temp.values.tolist()

            # Inserting a chunk at once in the database...
            loadData(records, cursor)

    except Exception as e:
        logging.info("Error Occurred in main function", e)
        print("Something went wrong", e)

    finally:
        conn.commit()
        cursor.close()
        conn.close()