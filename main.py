from leave import(
    apply_leave,
    view_leaves,
    approve_leave,
    reject_leave,
    view_leave_balance, 
)


def main():
    print("Welcome to Employee Leave Management System!")
    while True:
        print("\nEMPLOYEE LEAVE MANAGEMENT SYSTEM")
        print("1. Apply for Leave")
        print("2. View Leave Applications")
        print("3. Manager Approval")
        print("4. Reject Leave Request")
        print("5. View Leave Balance")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice =="1":
            apply_leave()

        elif choice =="2":
            view_leaves()
        
        elif choice=="3":
            approve_leave()

        elif choice=="4":
            reject_leave()

        elif choice =="5":
            view_leave_balance()

        elif choice =="6":
            print("Exiting application...")
            break

        else:
            print("Invlaid Choice. Please try again.")
        

if __name__ =="__main__":
    main()
