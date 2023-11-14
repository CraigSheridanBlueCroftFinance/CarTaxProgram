import CheckCarRegistrationNumber
import DatabaseConstants
import SQL_Toolbox
from datetime import datetime

Server = DatabaseConstants.Server
Database = DatabaseConstants.Database
UserName = DatabaseConstants.UserName
Password = DatabaseConstants.Password

#-----------------------------------------------------------------
# GET CURRENT DATE TIME 
#-----------------------------------------------------------------
RunDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print("RUN DATE: ", RunDate)
#-----------------------------------------------------------------
# CREATE CONECTION STRING TO THE DATABASE
#-----------------------------------------------------------------
sConnectionString = SQL_Toolbox.CreateConnectionString(Server, Database, UserName, Password)
print("CONNECTION STRING\n", sConnectionString)
#-----------------------------------------------------------------
# GET ALL LICENSE PLATES FROM THE DATABASE
#-----------------------------------------------------------------
sSql="SELECT NumberPlate FROM NumberPlates ORDER BY 1"
NumberPlates=SQL_Toolbox.ExecuteSelectOnlyQuery(sConnectionString, sSql)
print("NUMBER PLATES: ", NumberPlates)
#-----------------------------------------------------------------
# LOOP THROUGH NUMBER PLATES
#-----------------------------------------------------------------
for NumberPlate in NumberPlates:
    MyNumberPlate=NumberPlate[0]
    print("My NUMBER PLATE: ", MyNumberPlate)
    #-----------------------------------------------------------------
    # GET ALL LICENSE PLATES TO GET DATA FROM DVLA WEBSITE FOR.
    #-----------------------------------------------------------------
    Result = CheckCarRegistrationNumber.CheckLicencePlate(MyNumberPlate)
    print("RESULT FROM DVLA: ", Result)
    print("RESULT TYPE: ", type(Result))

    RegistrationNumber=""
    TaxStatus=""
    ArtEndDate=""
    MOTStatus=""
    Make=""
    YearOfManufacture=""
    EngineCapacity=""
    CO2Emissions=""
    FuelType=""
    MarkedForExport=""
    Colour=""
    TypeApproval=""
    RevenueWeight=""
    EuroStatus=""
    DateOfLastV5CIssued=""
    RealDrivingEmissions=""
    WheelPlan=""
    MonthOfFirstRegistration=""
    MonthOfFirstDVLARegistration=""
    
    for key, value in Result.items():
        
        print("KEY: ", key)
        print("VALUE: ", value)
        print("-----------------------------------------")
        if key=="registrationNumber":
            RegistrationNumber=value
        elif key=="taxStatus":
            TaxStatus=value
        elif key=="taxDueDate":
            TaxDueDate=value
        elif key=="artEndDate":
            ArtEndDate=value
        elif key=="motStatus":
            MOTStatus=value
        elif key=="make":
            Make=value
        elif key=="yearOfManufacture":
            YearOfManufacture=value
        elif key=="engineCapacity":
            EngineCapacity=value
        elif key=="co2Emissions":
            CO2Emissions=value
        elif key=="fuelType":
            FuelType=value
        elif key=="markedForExport":
            MarkedForExport=value
        elif key=="colour":
            Colour=value
        elif key=="typeApproval":
            TypeApproval=value
        elif key=="revenueWeight":
            RevenueWeight=value
        elif key=="euroStatus":
            EuroStatus=value
        elif key=="dateOfLastV5CIssued":
            DateOfLastV5CIssued=value
        elif key=="realDrivingEmissions":
            RealDrivingEmissions=value
        elif key=="wheelplan":
            WheelPlan=value
        elif key=="monthOfFirstRegistration":
            MonthOfFirstRegistration=value
        elif key=="monthOfFirstDvlaRegistration":
            MonthOfFirstDVLARegistration=value

            
    #-----------------------------------------------------------------
    # CREATE SQL INSERT STATEMENT
    #-----------------------------------------------------------------
    sSql=""
    sSql+=" INSERT INTO [dbo].[DVLA_Results]" + "\n"
    sSql+=" (" + "\n"
    sSql+=" [RunDate]" + "\n"
    sSql+=" ,[RegistrationNumber]" + "\n"
    sSql+=" ,[ArtEndDate]" + "\n"
    sSql+=" ,[CO2Emissions]" + "\n"
    sSql+=" ,[Colour]" + "\n"
    sSql+=" ,[EngineCapacity]" + "\n"
    sSql+=" ,[FuelType]" + "\n"
    sSql+=" ,[Make]" + "\n"
    sSql+=" ,[MarkedForExport]" + "\n"
    sSql+=" ,[MonthOfFirstRegistration]" + "\n"
    sSql+=" ,[MonthOfFirstDvlaRegistration]" + "\n"
    sSql+=" ,[MOTStatus]" + "\n"
    sSql+=" ,[RevenueWeight]" + "\n"
    sSql+=" ,[TaxDueDate]" + "\n"
    sSql+=" ,[TaxStatus]" + "\n"
    sSql+=" ,[TypeApproval]" + "\n"
    sSql+=" ,[WheelPlan]" + "\n"
    sSql+=" ,[YearOfManufacture]" + "\n"
    sSql+=" ,[EuroStatus]" + "\n"
    sSql+=" ,[RealDrivingEmissions]" + "\n"
    sSql+=" ,[DateOfLastV5CIssued])" + "\n"
    sSql+=" VALUES" + "\n"
    sSql+=" (" + "\n"

    # [RunDate]
    if RunDate=="":
        sSql+=" NULL" + "\n"
    else:
        sSql+="'" + RunDate + "'" + "\n"

    # ,[RegistrationNumber]
    if RegistrationNumber=="":
        sSql+=", NULL" + "\n"
    else:
        sSql+=",'" + RegistrationNumber + "'" + "\n"


    # ,[ArtEndDate]
        if ArtEndDate=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + ArtEndDate + "'" + "\n"

    # ,[CO2Emissions]
        if CO2Emissions=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + str(CO2Emissions) + "'" + "\n"

    # ,[Colour]
        if Colour=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + Colour + "'" + "\n"

    # ,[EngineCapacity]
        if EngineCapacity=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + str(EngineCapacity) + "'" + "\n"

    # ,[FuelType]
        if FuelType=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + FuelType + "'" + "\n"

    # ,[Make]
        if Make=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + Make + "'" + "\n"

    # ,[MarkedForExport]
        if MarkedForExport==False:
            sSql+=", 0" + "\n"
        else:
            sSql+=", 1" + "\n"

    # ,[MonthOfFirstRegistration]
        if MonthOfFirstRegistration=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + MonthOfFirstRegistration + "'" + "\n"

    # ,[MonthOfFirstDVLARegistration]
        if MonthOfFirstDVLARegistration=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + MonthOfFirstDVLARegistration + "'" + "\n"

    # ,[MOTStatus]
        if MOTStatus=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + MOTStatus + "'" + "\n"

    # ,[RevenueWeight]
        if RevenueWeight=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + str(RevenueWeight) + "'" + "\n"

    # ,[TaxDueDate]
        if TaxDueDate=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + TaxDueDate + "'" + "\n"

    # ,[TaxStatus]
        if TaxStatus=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + TaxStatus + "'" + "\n"

    # ,[TypeApproval]
        if TypeApproval=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + TypeApproval + "'" + "\n"

    # ,[WheelPlan]
        if WheelPlan=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + WheelPlan + "'" + "\n"

    # ,[YearOfManufacture]
        if YearOfManufacture=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + str(YearOfManufacture) + "'" + "\n"

    # ,[EuroStatus]
        if EuroStatus=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + EuroStatus + "'" + "\n"

    # ,[RealDrivingEmissions]
        if RealDrivingEmissions=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + RealDrivingEmissions + "'" + "\n"

    # ,[DateOfLastV5CIssued])
        if DateOfLastV5CIssued=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + DateOfLastV5CIssued + "'" + "\n"

        sSql+=");"

        print("----------------------------------------------------------------------")
        print(sSql)
        print("----------------------------------------------------------------------")

        SQL_Toolbox.ExecuteInsertUpdateDeleteQuery(sConnectionString, sSql)