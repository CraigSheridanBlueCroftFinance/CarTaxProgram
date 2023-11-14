import SQL_Toolbox
import DatabaseConstants as DC

sConnectionString=SQL_Toolbox.CreateConnectionString(DC.Server, DC.Database, DC.UserName, DC.Password)

def GetNumberPlatesFromTheDatabase():
    sSql=""
    sSql+=" SELECT"
    sSql+=" NumberPlate"
    sSql+=" FROM NumberPlates"
    sSql+=" ORDER BY 1"

    DataArray=SQL_Toolbox.ExecuteSelectOnlyQuery(sConnectionString, sSql)

    return DataArray

if __name__ == '__main__':
    MyResponse= GetNumberPlatesFromTheDatabase()
    #I NEED TO PRINT THE RETURNED OBJECT IN ORDER TO RETURN IT TO EXCEL
    print("MY RESPONSE: ", MyResponse)



