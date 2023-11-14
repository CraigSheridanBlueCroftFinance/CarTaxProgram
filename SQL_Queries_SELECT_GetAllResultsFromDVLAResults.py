import SQL_Toolbox
import sys
import DatabaseConstants as DC
from datetime import datetime

def GetAllResultsFromDVLA(NumberPlate):

    sConnectionString=SQL_Toolbox.CreateConnectionString(DC.Server, DC.Database, DC.UserName, DC.Password)

    #-----------------------------------------------------------------
    # CREATE SQL INSERT STATEMENT
    #-----------------------------------------------------------------

    sSql = ""
    sSql+=" SELECT"
    sSql+=" 'Start'"
    sSql+=" ,CONCAT('artEndDate:', [ArtEndDate]) AS ArtEndDate"
    sSql+=" ,CONCAT('co2Emissions:', [CO2Emissions]) AS CO2Emissions"
    sSql+=" ,CONCAT('colour:', [Colour]) AS Colour"
    sSql+=" ,CONCAT('engineCapacity:',[EngineCapacity]) AS EngineCapacity"
    sSql+=" ,CONCAT('fuelType:',[FuelType]) AS FuelType"
    sSql+=" ,CONCAT('make:',[Make]) AS Make"
    sSql+=" ,CONCAT('markedforExport:',[MarkedForExport]) AS MarkedForExport"
    sSql+=" ,CONCAT('monthOfFirstRegistration:',[MonthOfFirstRegistration]) AS MonthOfFirstRegistration"
    sSql+=" ,CONCAT('monthOfFirstDvlaRegistration:',[MonthOfFirstDvlaRegistration]) AS MonthOfFirstDVLARegistration"
    sSql+=" ,CONCAT('motStatus:',[MOTStatus]) AS MOTStatus"
    sSql+=" ,CONCAT('motExpiryDate:',[MOTExpiryDate]) AS MOTExpiryDate"
    sSql+=" ,CONCAT('registrationNumber:',[RegistrationNumber]) AS RegistrationNumber"
    sSql+=" ,CONCAT('revenueWeight:',[RevenueWeight]) AS RevenueWeight"
    sSql+=" ,CONCAT('taxDueDate:',[TaxDueDate]) AS TaxDueDate"
    sSql+=" ,CONCAT('taxStatus:',[TaxStatus]) AS TaxStatus"
    sSql+=" ,CONCAT('typeApproval:',[TypeApproval]) AS TypeApproval"
    sSql+=" ,CONCAT('wheelplan:',[WheelPlan]) AS WheelPlan"
    sSql+=" ,CONCAT('yearOfManufacture:',[YearOfManufacture]) AS YearOfManufacture"
    sSql+=" ,CONCAT('euroStatus:',[EuroStatus]) AS EuroStatus"
    sSql+=" ,CONCAT('realDrivingEmmisions:',[RealDrivingEmissions]) AS RealDrivingEmissions"
    sSql+=" ,CONCAT('dateOfLastV5cIssued:',[DateOfLastV5CIssued]) AS DateOfLastV5CIssued"
    sSql+=" ,CONCAT('RunDate:',CAST(RunDate AS DATE)) AS RunDate" 
    sSql+=" FROM [dbo].[DVLA_Results]"
    sSql+=" WHERE RegistrationNumber = '" + (NumberPlate) + "'"
    sSql+=" ORDER BY RunDate DESC"
    
    print("----------------------------------------------------------------------")
    print(sSql)
    print("----------------------------------------------------------------------")

    DataArray = SQL_Toolbox.ExecuteSelectOnlyQuery(sConnectionString, sSql)

    return DataArray

if __name__ == '__main__':
    NumberPlate=sys.argv[1]
    MyResponse=GetAllResultsFromDVLA(NumberPlate)
    #I NEED TO PRINT THE RETURNED OBJECT IN ORDER TO RETURN IT TO EXCEL
    print("MY RESPONSE: ", MyResponse)