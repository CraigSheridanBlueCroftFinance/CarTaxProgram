import CheckCarRegistrationNumber
import DatabaseConstants
import SQL_Toolbox

Server = DatabaseConstants.Server
Database = DatabaseConstants.Database
UserName = DatabaseConstants.UserName
Password = DatabaseConstants.Password

#NumberPlate = "LSJ3"
NumberPlate="YF64PWL"

Result = CheckCarRegistrationNumber.CheckLicencePlate(NumberPlate)
print("RESULT FROM DVLA: ", Result)
# ===============================================================
# sConnectionString = SQL_Toolbox.CreateConnectionString(Server, Database, UserName, Password)
# print("CONNECTION STRING\n", sConnectionString)

# sSql="SELECT NumberPlate FROM NumberPlates"
# NumberPlates=SQL_Toolbox.ExecuteSelectOnlyQuery(sConnectionString, sSql)
# print("NUMBER PLATES: ", NumberPlates)


