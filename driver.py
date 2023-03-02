import pyodbc

for driver in pyodbc.drivers():
    print(driver)

server = "localhost"
db1 = "web_scrapping"
tcon="yes"
uname="root"
pword = "pass"
prt = "3306"

cnxn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host=server, database=db1, port=prt,  user=uname, password=pword)