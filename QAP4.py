# Description: One Stop Insurane Company Policy Information
# Date: 2024/03/19 - 2024/03/25
# Author: Brian Jackman
 
# Import required libraries
import FormatValues as FV
import datetime

# Program constants.
f = open('def.dat','r')
POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
DISCOUNT_ADDITIONAL_CARS = float(f.readline())
EXTRA_LIABILITY_COVERAGE = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_CAR_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

CUR_DATE = datetime.datetime.now()

# Define required functions.
def GetClaim():
    while True:
        ClaimNum = input("Enter Claim Number (or type 'end' to finish): ")
        if ClaimNum == 'end':
            break
        ClaimDate = input("Enter Claim Date (YYYY-MM-DD): ")
        ClaimAmount = float(input("Enter Claim Amount: $"))
        ClaimNum.append(ClaimNumLst)
        ClaimDate.append(ClaimDateLst)
        ClaimAmount.append(ClaimAmountLst)

def CalculatePremium():
        if ExtLia == "N":
            EXTRA_LIABILITY_COVERAGE = 0
        if OptGlass == "N":
            GLASS_COVERAGE = 0
        if OptLoan == "N": 
            LOANER_CAR_COVERAGE = 0
        if Numcars == 1:
            InsurPrem = BASIC_PREMIUM + EXTRA_LIABILITY_COVERAGE + GLASS_COVERAGE + LOANER_CAR_COVERAGE
        elif NumCars >1:
            InsurPrem = BASIC_PREMIUM + (NumCars - 1)(BASIC_PREMIUM * DISCOUNT_ADDITIONAL_CARS) + EXTRA_LIABILITY_COVERAGE + GLASS_COVERAGE + LOANER_CAR_COVERAGE
        return InsurPrem

def CalculateTotalCost():
        HST = InsurPrem * HST_RATE
        TotalCost = InsurPrem + HST
        return TotalCost

def CalculateMonthlyPayment():
    if PayMeth == "Down pay":
        MonthlyPayment = (TotalCost - DownPayAmt + PROCESSING_FEE) / 8
    elif PayMeth == "Monthly":
        Monthlypayment = (TotalCost + PROCESSING_FEE) / 8

def FirstPaymentDate():
        (dt.replace(day=1) + datetime.timedelta(days = 32)).replace(day = 1)



 
# Main program.
 

#Lists for claim data
ClaimNumLst = ["1942","1943"]
ClaimDateLst = ["2024-03-19","2024-03-20"]
ClaimAmountLst = ["5,000.00","6,000.00"]

print()
while True:


    # Gather user inputs
    print("Input Ccustomer information")
    print()
    CusFirName =  input("Enter the customer's first name: ").title()
    CusLasName = input("Enter the customer's last name: ").title()
    StrAdd = input("Enter the customer's street address: ")
    City = input("Enter the City: ").title()
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    while True:
        Prov = input("Enter the customer province (XX): ").upper()
        if Prov == "":
            print("Error - cannot be blank.")
        elif len(Prov) != 2:
            print("Error - must be 2 characters only.")
        elif Prov not in ProvLst:
            print("Error - invalid province.")
        else:
            break
    PostCode = input("Enter the postal code: ")
    PhoneNum = input("Enter the phone number(999-999-9999): ")
    NumCars = input("Enter the number of cars they wish to insure: ")
    Numcars = int(NumCars)
    ExtLia = input("Do they want extra liability coverage up to $1,000,000.00 (Y/N?): ").upper()
    OptGlass = input("Do they want optional glass coverage(Y/N)?: ").upper()
    OptLoan = input("Do they want an optional loaner car(Y/N)?: ").upper()
    PayMethLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PayMeth = input("Enter the payment method(Full/Monthly/Down Pay)?: ").title()
        if PayMeth == "":
            print("Error - Payment method cannot be blank")
        elif PayMeth not in PayMethLst:
            print("Error - Must enter Full, Monthly or Down Pay")
        else:
            break
        if PayMeth == "Down Pay":
            DownPayAmt = input("Enter the amount of down payment: ")
            DownPayAmt = float(DownPayAmt)
        else:
            break
    print(GetClaim())
    
    # Perform required calculations.
    
    print(CalculatePremium())

    print(CalculateTotalCost())

    print(CalculateMonthlyPayment())

    # Display results.


    print("One Stop Insurane Company ")
    print("--------------------------------------------")
    print(f" Customer's first name:          {CusFirName:<10s}")
    print(f" Customer's last name:           {CusLasName:<10s}")
    print(f" Customer's address:             {StrAdd:<20s}")
    print(f" City:                           {City:<10s}")
    print(f" Province:                       {Prov:<2s}")
    print(f" Postal Code:                    {PostCode:<6s}")
    print(f" Phone Number:                   {PhoneNum:<12s}")
    print(f" Number of cars:                 {NumCars}")
    print(f" Extra Liability Charge:         {FV.FDollar2(EXTRA_LIABILITY_COVERAGE)} ")
    print(f" Optional glass coverage charge: {FV.FDollar2(GLASS_COVERAGE)}")
    print(f" Optional loaner charge:         {FV.FDollar2(LOANER_CAR_COVERAGE)}")
    print(f" Payment method:                 {PayMeth:<8s}")
    print(f" Down pay amout:                 {FV.FDollar2(DownPayAmt)}")
    print(f" Premium:                        {FV.FDollar2(InsurPrem)}")
    print(f" Total Cost:                     {FV.FDollar2(TotalCost)}")
    if PayMeth == "Monthly" or "Down Pay":
        print(f" Monthly payment amount:     {FV.FDollar2(Monthlypayment)}")
    else:   
        break
    print(f" Invoice date:                   {FV.FDateS(datetime.dateime.now)}")
    print(f" First payment due:              {FV.FDateS(FirstPaymentDate)} ")
    print("--------------------------------------------")
    print()
    print(f"Claim #  Claim Date        Amount")
    print("------------------------------------")
    print(f"{ClaimNumLst[0]}   {FV.FDateS(ClaimDateLst[0])}     {FV.FDollar2(ClaimAmountLst[0])}")
    print(f"{ClaimNumLst[1]}   {FV.FDateS(ClaimDateLst[1])}     {FV.FDollar2(ClaimAmountLst[1])}")

    
# Housekeeping   
    POLICY_NUM += 1 

f = open('def.dat','w')
f.write("{}, ".format(str(POLICY_NUM)))
f.close()