#atm1.py
import mysql.connector
from atm2 import  InvalidInputError,InsufficientFundError,withdrawError

def deposit(bal,con,cur):
    #global bal,con,cur
    d = float(input("Enter Amount to Deposit : "))
    if d <= 0:
            raise InvalidInputError
    bal =bal +d
    cur.execute("update user set bal={};".format(bal))
    con.commit()
    
    print("Your account is Credited with INR {}".format(d))
    print("Total account balance : {}".format(bal))

def withdraw(bal,con,cur):
    #global bal,con,cur
    w = float(input("Enter Amount to Withdraw : "))
    if (w <=0):
        raise withdrawError
    if (w +499>=bal):
        raise InsufficientFundError
    bal-=w
    cur.execute("update user set bal={};".format(bal))
    con.commit()
    print("Your account is Debited with {}".format(w))
    print("Total account balance : {}".format(bal))
        
def balanceEnquiry(bal):
    #global bal
    print("Total account balance : {}".format(bal))
