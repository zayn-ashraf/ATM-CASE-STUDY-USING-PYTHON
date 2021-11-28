#atm.py
import sys
import mysql.connector
from atm2 import InvalidInputError,InsufficientFundError,withdrawError
from atm0 import menu
from atm1 import deposit,withdraw,balanceEnquiry
print("-"*90)
print("Enter Card Details".center(90," "))
print("-"*90)
try:
    user = input("\t\tusername : ")
    password = int(input("\t\tpassword : "))

    con = mysql.connector.connect(host = 'localhost',user = '{}'.format(user),password = '{}'.format(password) ,database = 'atm')
    cur=con.cursor()
    cur.execute("select bal from user;")
    records = cur.fetchone()
    lst = list(records)
    bal = lst[0]
    print("\n\n\n")
    print("-"*90)

    while True:
        try:
            menu()
            i = int(input("Enter your choice : "))
            if(i not in [1,2,3,4,5]):
                print("choose options 1 to 4")
            elif(i==1):
                try:
                    deposit(bal,con,cur)
                except ValueError:
                    print("Plz dont enter characters (or) special symbols (or)alpha numeric values")
                except InvalidInputError:
                    print("Don't enter negative values or zero ")
            elif i==2:
                try:
                    withdraw(bal,con,cur)
                except ValueError:
                    print("Plz dont enter characters (or) special symbols (or)alpha numeric values")
                except withdrawError:
                    print("Don't Enter negative values or zero to withdraw..")
                except InsufficientFundError:
                    print("Insufficient funds...")
            elif i==3:
                balanceEnquiry(bal)
          
            else :
                inp ="Thanks for using the app"
                print("="*90)
                print("\t\t\t\tATM")
                print("="*90)
                print("\n\n\n\n\n\n\n\n\n\n\n\n")
                print(inp.center(90," "))
                print("\n\n\n\n\n\n\n\n\n\n\n\n")
                print("="*90)
                sys.exit()
                
        except ValueError:
            print("Plz dont enter characters (or) special symbols (or)alpha numeric values")
except mysql.connector.Error as err:
    if err.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno ==errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

