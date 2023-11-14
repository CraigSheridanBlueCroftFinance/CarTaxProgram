import SQL_Toolbox
import sys
import DatabaseConstants as DC
from datetime import datetime

def InsertInto_DVLA_Results( \
                                RegistrationNumber, Colour, TaxStatus, TaxDueDate, MOTStatus, MOTExpiryDate, MarkedForExport \
                                ,Make, EngineCapacity, FuelType, ArtEndDate, YearOfManufacture, RealDrivingEmissions, TypeApproval \
                                , RevenueWeight, EuroStatus, WheelPlan, MonthOfFirstRegistration, MonthOfFirstDVLARegistration \
                                , DateOfLastV5CIssued, CO2Emissions \
                            ):

    sConnectionString=SQL_Toolbox.CreateConnectionString(DC.Server, DC.Database, DC.UserName, DC.Password)

    RunDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
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
    sSql+=" ,[MOTExpiryDate]" + "\n"
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
        if MarkedForExport=="False":
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

    # MOT Expiry Date
        if MOTExpiryDate=="":
            sSql+=", NULL" + "\n"
        else:
            sSql+=",'" + MOTExpiryDate + "'" + "\n"

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

if __name__ == '__main__':
    Arguments=sys.argv[1]
    vArguments=Arguments.split("|")
    RegistrationNumber=""
    Colour=""
    TaxStatus=""
    TaxDueDate=""
    MOTStatus=""
    MOTExpiryDate=""
    MarkedforExport=""
    Make=""
    EngineCapacity=""
    FuelType=""
    ArtEndDate=""
    YearOfManufacture=""
    RealDrivingEmissions=""
    TypeApproval=""
    RevenueWeight=""
    EuroStatus=""
    WheelPlan=""
    MonthOfFirstRegistration=""
    MonthOfFirstDVLARegistration=""
    DateOfLastV5CIssued=""
    CO2Emissions=""
    print("===================================================================")
    for item in vArguments:
        
        print("ITEM: ", item)
        
        # REGISTRATION NUMBER
        if item[0:len("registrationNumber")].strip()=="registrationNumber":
            print("REGISTRATION NUMBER TEXT: ", item[0:len("registrationNumber")+1])
            LenDifference=len(item)-len("registrationNumber")-2
            RegistrationNumber=item[-LenDifference:].strip()
            print("RegistrationNumber VALUE: ", RegistrationNumber)
        # COLOUR
        elif item[0:len("colour")+1].strip()=="colour":
            print("COLOUR TEXT: ", item[0:len("colour")+1])
            LenDifference=len(item)-len("colour")-2
            Colour=item[-LenDifference:].strip()
            print("Colour VALUE: ", Colour)
        # TAX STATUS
        elif item[0:len("taxStatus")+1].strip()=="taxStatus":
            print("TAX STATUS TEXT: ", item[0:len("taxStatus")+1])
            LenDifference=len(item)-len("taxStatus")-2
            TaxStatus=item[-LenDifference:].strip()
            print("TaxStatus VALUE: ", TaxStatus)
        # TAX DUE DATE
        elif item[0:len("taxDueDate")+1].strip()=="taxDueDate":
            print("TAX DUE DATE TEXT: ", item[0:len("taxDueDate")+1])
            LenDifference=len(item)-len("taxDueDate")-2
            TaxDueDate=item[-LenDifference:].strip()
            print("Tax Due Date VALUE: ", TaxDueDate)
        # MOT STATUS
        elif item[0:len("motStatus")+1].strip()=="motStatus":
            print("MOT STATUS TEXT: ", item[0:len("motStatus")+1])
            LenDifference=len(item)-len("motStatus")-2
            MOTStatus=item[-LenDifference:].strip()
            print("MOT Status VALUE: ", MOTStatus)
        # MOT EXPIRY DATE
        elif item[0:len("motExpiryDate")+1].strip()=="motExpiryDate":
            print("MOT EXPIRY DATE TEXT: ", item[0:len("motExpiryDate")+1])
            LenDifference=len(item)-len("motExpiryDate")-2
            MOTExpiryDate=item[-LenDifference:].strip()
            print("MOT EXPIRY DATE VALUE: ", MOTExpiryDate)
        # MARKED FOR EXPORT
        elif item[0:len("markedForExport")+1].strip()=="markedForExport":
            print("MARKED FOR EXPORT TEXT: ", item[0:len("markedForExport")+1])
            LenDifference=len(item)-len("markedForExport")-2
            MarkedforExport=item[-LenDifference:].strip()
            print("MARKED FOR EXPORT VALUE: ", MarkedforExport)
        # MAKE
        elif item[0:len("make")+1].strip()=="make":
            print("MAKE TEXT: ", item[0:len("make")+1])
            LenDifference=len(item)-len("make")-2
            Make=item[-LenDifference:].strip()
            print("MAKE VALUE: ", Make)
        # ENGINE CAPACITY
        elif item[0:len("engineCapacity")+1].strip()=="engineCapacity":
            print("ENGINE CAPACITY TEXT: ", item[0:len("engineCapacity")+1])
            LenDifference=len(item)-len("engineCapacity")-2
            EngineCapacity=item[-LenDifference:].strip()
            print("ENGINE CAPACITY  VALUE: ", EngineCapacity)
        # FUEL TYPE
        elif item[0:len("fuelType")+1].strip()=="fuelType":
            print("FUEL TYPE TEXT: ", item[0:len("fuelType")+1])
            LenDifference=len(item)-len("fuelType")-2
            FuelType=item[-LenDifference:].strip()
            print("FUEL TYPE VALUE: ", FuelType)
        # ART END DATE
        elif item[0:len("artEndDate")+1].strip()=="artEndDate":
            print("ART END DATE TEXT: ", item[0:len("artEndDate")+1])
            LenDifference=len(item)-len("artEndDate")-2
            ArtEndDate=item[-LenDifference:].strip()
            print("ART END DATE VALUE: ", ArtEndDate)
        # YEAR OF MANUFACTURE
        elif item[0:len("yearOfManufacture")+1].strip()=="yearOfManufacture":
            print("YEAR OF MANUFACTURE TEXT: ", item[0:len("yearOfManufacture")+1])
            LenDifference=len(item)-len("yearOfManufacture")-2
            YearOfManufacture=item[-LenDifference:].strip()
            print("YEAR OF MANUFACTURE VALUE: ", YearOfManufacture)

        # REAL DRIVING EMISSIONS
        elif item[0:len("realDrivingEmissions")+1].strip()=="realDrivingEmissions":
            print("REAL DRIVING EMISSIONS TEXT: ", item[0:len("realDrivingEmissions")+1])
            LenDifference=len(item)-len("realDrivingEmissions")-2
            RealDrivingEmissions=item[-LenDifference:].strip()
            print("REAL DRIVING EMISSIONS VALUE: ", RealDrivingEmissions)
        # TYPE APPROVAL
        elif item[0:len("typeApproval")+1].strip()=="typeApproval":
            print("TYPE APPROVAL TEXT: ", item[0:len("typeApproval")+1])
            LenDifference=len(item)-len("typeApproval")-2
            TypeApproval=item[-LenDifference:].strip()
            print("TYPE APPROVAL VALUE: ", TypeApproval)
        # REVENUE WEIGHT
        elif item[0:len("revenueWeight")+1].strip()=="revenueWeight":
            print("REVENUE WEIGHT TEXT: ", item[0:len("revenueWeight")+1])
            LenDifference=len(item)-len("revenueWeight")-2
            RevenueWeight=item[-LenDifference:].strip()
            print("REVENUE WEIGHT VALUE: ", RevenueWeight)
        # EURO STATUS
        elif item[0:len("euroStatus")+1].strip()=="euroStatus":
            print("EURO STATUS TEXT: ", item[0:len("euroStatus")+1])
            LenDifference=len(item)-len("euroStatus")-2
            EuroStatus=item[-LenDifference:].strip()
            print("EURO STATUS VALUE: ", EuroStatus)
        # WHEEL PLAN
        elif item[0:len("wheelPlan")+1].strip()=="wheelPlan":
            print("WHEEL PLAN TEXT: ", item[0:len("wheelPlan")+1])
            LenDifference=len(item)-len("wheelPlan")-2
            WheelPlan=item[-LenDifference:].strip()
            print("WHEEL PLAN VALUE: ", WheelPlan)
        # MONTH OF FIRST REGISTRATION
        elif item[0:len("monthOfFirstRegistration")+1].strip()=="monthOfFirstRegistration":
            print("MONTH OF FIRST REGISTRATION TEXT: ", item[0:len("monthOfFirstRegistration")+1])
            LenDifference=len(item)-len("monthOfFirstRegistration")-2
            MonthOfFirstRegistration=item[-LenDifference:].strip()
            print("MONTH OF FIRST REGISTRATION VALUE: ", MonthOfFirstRegistration)
        # MOMNTH OF FIRST DVLA REGISTRATION
        elif item[0:len("monthOfFirstDVLARegistration")+1].strip()=="monthOfFirstDVLARegistration":
            print("MONTH OF FIRST DVLA TEXT: ", item[0:len("monthOfFirstDVLARegistration")+1])
            LenDifference=len(item)-len("monthOfFirstDVLARegistration")-2
            MonthOfFirstDVLARegistration=item[-LenDifference:].strip()
            print("MONTH OF FIRST DVLA REGISTRATION: ", MonthOfFirstDVLARegistration)
        # DATE OF LAST V5C ISSUED
        elif item[0:len("dateOfLastV5CIssued:")+1].strip()=="dateOfLastV5CIssued:":
            print("DATE OF LAST V5C ISSUED TEXT: ", item[0:len("dateOfLastV5CIssued:")+1])
            LenDifference=len(item)-len("dateOfLastV5CIssued:")-2
            DateOfLastV5CIssued=item[-LenDifference:].strip()
            print("DATE OF LAST V5C ISSUED VALUE: ", DateOfLastV5CIssued)
        # CO2 EMISSIONS
        elif item[0:len("co2Emissions")+1].strip()=="co2Emissions":
            print("CO2 EMISSIONS TEXT: ", item[0:len("co2Emissions")+1])
            LenDifference=len(item)-len("co2Emissions")-2
            CO2Emissions=item[-LenDifference:].strip()
            print("CO2 EMISSIONS VALUE: ", CO2Emissions)
    
    InsertInto_DVLA_Results( \
                                RegistrationNumber, Colour, TaxStatus, TaxDueDate, MOTStatus, MOTExpiryDate, MarkedforExport \
                                ,Make, EngineCapacity, FuelType, ArtEndDate, YearOfManufacture, RealDrivingEmissions, TypeApproval \
                                , RevenueWeight, EuroStatus, WheelPlan, MonthOfFirstRegistration, MonthOfFirstDVLARegistration \
                                , DateOfLastV5CIssued, CO2Emissions \
                            )
    #I NEED TO PRINT THE RETURNED OBJECT IN ORDER TO RETURN IT TO EXCEL
    #print("MY RESPONSE: ", MyResponse)