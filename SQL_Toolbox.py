import pyodbc
import sys

def CreateConnectionString(Server, Database, UserName, Password):
    sConnStr = "Driver={ODBC Driver 18 for SQL Server};Server=" + Server + \
                ";Database=" + Database + \
                ";Uid=" + UserName + \
                ";Pwd=" + Password
    return sConnStr

def ExecuteSelectOnlyQuery(sConnectionString, sSql):
    conn = pyodbc.connect(sConnectionString)
    cursor = conn.cursor()
    cursor.execute(sSql)
    rows = cursor.fetchall()
    return rows

def ExecuteInsertUpdateDeleteQuery(sConnectionString, sSql):
    conn = pyodbc.connect(sConnectionString)
    cursor = conn.cursor()
    cursor.execute(sSql)
    conn.commit()
    cursor.close

if __name__ == '__main__':
    for item in sys.argv:
        print("ITEM: ", item)
    #NumberPlate=sys.argv[1]
    
    #I NEED TO PRINT THE RETURNED OBJECT IN ORDER TO RETURN IT TO EXCEL
    #print("MY RESPONSE: ", MyResponse)

