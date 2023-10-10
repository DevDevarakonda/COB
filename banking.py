import sqlite3
conn=sqlite3.connect('bank.db')
c=conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS(account_number INTEGER PRIMARY KEY, name TEXT , balance REAL)''')

def create_account():
    name=input("Enter account holders name:")
    balance=float(input("Enter intial balance:"))

    c.execute("INSERT INTO  accounts (name,balance)VALUES(?,?)",(name,balance))

    conn.commit()
    print("Account created succesfully.")


def withdraw_money():
    account_number=int(input("Enter the account number"))
    amount=float(input("Enter the amount:"))


    c.execute("SELECT balance FROM  accounts WHERE accont_number=?",(account_number,))
    balance=c.fetchone()[0]

    if balance>=amount:
        new_balance=balance-amount

        c.execute("UPDATE accounts SET balance=? where account_number=?",(new_balance,account_number))

        conn.commit()
        print("Amount withdrawn succesfully")

    else:
        print("insufficient Balance")




def deposite_money():
    account_number=int(input("Enter the account number:"))
    amount=float(input("Enter the amount:"))

    c.execute("select balance from accounts where account_number=?",(account_number,))
    balance=c.fetchone()[0]

    new_balance=balance+amount

    c.execute("upadate accounts set balance=?",(new_balance,account_number))
    conn.commit()
    print("Amount deposited successfully.")





def update_account_details():
    account_number=int(input("Enter the account number:"))
    new_name=input("Enter the name")

    c.execute("update account set name=? where account_number=?",(new_name,account_number))
    conn.commit()
    print("Account details updated successfully.")





def transfer_money():
    from_account=int(input("Enter the account number to transfer money:"))
    to_account=int(input("Enter the account number to transfer money:"))
    amount=float(input("Enter the amount to transfer money:"))

    c.execute("select balance from account where accoun_number=?",(from_account,))

   


