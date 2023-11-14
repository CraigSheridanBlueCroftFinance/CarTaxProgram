import SQL_Toolbox
import sys
import DatabaseConstants as DC

def InsertInto_NumberPlateTable(NumberPlate):

    sConnectionString=SQL_Toolbox.CreateConnectionString(DC.Server, DC.Database, DC.UserName, DC.Password)
    
    #-----------------------------------------------------------------
    # CREATE SQL INSERT STATEMENT
    #-----------------------------------------------------------------
    sSql=""
    sSql+=" INSERT INTO NumberPlates"
    sSql+=" ("
    sSql+=" NumberPlate"
    sSql+=" , IncludeInOvernightAnalysis"
    sSql+=" )"
    sSql+=" VALUES"
    sSql+=" ("
    sSql+= " '" + NumberPlate + "'"
    sSql+=" , '1'"
    sSql+= " );"

    print("----------------------------------------------------------------------")
    print(sSql)
    print("----------------------------------------------------------------------")

    SQL_Toolbox.ExecuteInsertUpdateDeleteQuery(sConnectionString, sSql)

if __name__ == '__main__':
    NumberPlate=sys.argv[1]
       
    InsertInto_NumberPlateTable(NumberPlate)
    #I NEED TO PRINT THE RETURNED OBJECT IN ORDER TO RETURN IT TO EXCEL
    #print("MY RESPONSE: ", MyResponse)