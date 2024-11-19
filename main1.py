import banking_system

def main():
    print("Welcome to the Bank")
    account = banking_system.create_account()
    print(f"Account created successfully: {account}\n")

    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        
        elif choice == '3':
            print(account.check_balance())
        
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
