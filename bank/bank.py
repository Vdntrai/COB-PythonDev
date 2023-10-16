import sqlite3
import random

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number INTEGER PRIMARY KEY,
        account_holder TEXT,
        balance REAL
    )
''')
conn.commit()

def generate_account_number():
    return random.randint(1000, 9999)

def create_account():
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    account_number = generate_account_number()
    cursor.execute("INSERT INTO accounts (account_number, account_holder, balance) VALUES (?, ?, ?)", (account_number, account_holder, initial_balance))
    conn.commit()
    print(f"Account number {account_number} created for {account_holder} with an initial balance of ₹{initial_balance:.2f}")

def display_balance(account_number):
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()
    if balance:
        print(f"Account balance: ₹{balance[0]:.2f}")
    else:
        print("Account not found.")

def withdraw_money(account_number):
    amount = float(input("Enter the withdrawal amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    current_balance = cursor.fetchone()
    if current_balance:
        current_balance = current_balance[0]
        if current_balance >= amount:
            new_balance = current_balance - amount
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
            conn.commit()
            print(f"Withdrew ₹{amount:.2f}. New balance: ₹{new_balance:.2f}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def deposit_money(account_number):
    amount = float(input("Enter the deposit amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    current_balance = cursor.fetchone()
    if current_balance:
        current_balance = current_balance[0]
        new_balance = current_balance + amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
        conn.commit()
        print(f"Deposited ₹{amount:.2f}. New balance: ₹{new_balance:.2f}")
    else:
        print("Account not found.")

def update_account_details(account_number):
    new_account_holder = input("Enter the new account holder's name: ")
    cursor.execute("UPDATE accounts SET account_holder = ? WHERE account_number = ?", (new_account_holder, account_number))
    conn.commit()
    print("Account details updated.")

def transfer_money(sender_account):
    receiver_account = int(input("Enter the receiver's account number: "))
    amount = float(input("Enter the transfer amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (sender_account,))
    sender_balance = cursor.fetchone()
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (receiver_account,))
    receiver_balance = cursor.fetchone()
    if sender_balance and receiver_balance:
        sender_balance = sender_balance[0]
        receiver_balance = receiver_balance[0]
        if sender_balance >= amount:
            sender_new_balance = sender_balance - amount
            receiver_new_balance = receiver_balance + amount
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (sender_new_balance, sender_account))
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (receiver_new_balance, receiver_account))
            conn.commit()
            print(f"Transferred ₹{amount:.2f} from account {sender_account} to account {receiver_account}.")
        else:
            print("Insufficient balance for the transfer.")
    else:
        print("One or both accounts not found.")

def close_connection():
    conn.close()

while True:
    print("\nBanking Management System Menu:")
    print("1. Create Account")
    print("2. Display Balance")
    print("3. Withdraw Money")
    print("4. Deposit Money")
    print("5. Update Account Details")
    print("6. Transfer Money")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        account_number = int(input("Enter your account number: "))
        display_balance(account_number)
    elif choice == '3':
        account_number = int(input("Enter your account number: "))
        withdraw_money(account_number)
    elif choice == '4':
        account_number = int(input("Enter your account number: "))
        deposit_money(account_number)
    elif choice == '5':
        account_number = int(input("Enter your account number: "))
        update_account_details(account_number)
    elif choice == '6':
        account_number = int(input("Enter your sender account number: "))
        transfer_money(account_number)
    elif choice == '7':
        close_connection()
        print("Banking System is closed. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
