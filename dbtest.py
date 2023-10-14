import pyodbc
cnxn_str = (
    r'Driver={ODBC Driver 17 for SQL Server};'
    r'Server=sqldb-2022;'
    r'Database=master;'
    r'UID=sa;'
    r'PWD=Passw0rd;'
)
try:
    cnxn: pyodbc.Connection = pyodbc.connect(cnxn_str)
    cursor: pyodbc.Cursor = cnxn.cursor()
    cursor.execute('SELECT @@VERSION, SYSDATETIME()')
    records = cursor.fetchall()
    for r in records:
        print(f"----------------------- CONNECTED TO SQLDB ---------------------------------------------")
        print(r)
    print(f"----------------------- CLOSING CONNECTION ---------------------------------------------")
    cursor.close()
except Exception as error:
    print (error)