import json
import os

DATA_FILE   = "data/employees.json"

def load_leaves():
    if not os.path.exists(DATA_FILE):
        return[]

    with open(DATA_FILE, "r") as file:
        if os.path.getsize(DATA_FILE) == 0:
            return []
        return json.load(file)

def save_leaves(leaves):
    os.makedirs("data", exist_ok = True)

    with open(DATA_FILE, "w") as file:
        json.dump(leaves, file, indent=4)

def apply_leave():
    
    employee_id = input("Enter Employee ID: ").strip()
    employee_name = input("Enter Employee Name: ").strip()

    print("\nSelect Leave Type:")
    print("1. Casual Leave")
    print("2. Sick Leave")
    print("3. Earned Leave")

    leave_type_choice = input("Enter choice: ").strip()

    leave_types = {
        "1": "Casual Leave",
        "2": "Sick Leave",
        "3": "Earned Leave"
    }
    
    if leave_type_choice not in leave_types:
        print("Invalid Leave type!")
        return

    leave_type = leave_types[leave_type_choice]

    try:
        leave_days = int(input("Enter number of leave days: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    if leave_days <= 0:
        print("Leave days must be more than zero!")
        return

    reason = input("Enter reason for leave: ")

    if leave_days > 5:
        status = "Manager Approval Required"
    else:
        status = "Leave Processed"
    
    leaves = load_leaves()
    max_id = max(
        [int(leave["leave_id"][1:]) for leave in leaves],default=0)
    leave_id = f"L{max_id + 1}"
    
    leave_request = {
        "leave_id": leave_id,
        "employee_id":employee_id,
        "employee_name": employee_name,
        "leave_type": leave_type,
        "reason": reason,
        "leave_days": leave_days,
        "status": status
    }

    leaves.append(leave_request)
    save_leaves(leaves)

    print("\nLeave Application submitted successfuly!")

def view_leaves():
    leaves = load_leaves()

    if not leaves:
        print("\nNo leave applications found.")
        return

    print("\n________Employee Leave Records_______")

    for leave in leaves:
        print("=============================")
        print("Leave ID: ", leave["leave_id"])
        print("Employee ID:", leave["employee_id"])
        print("Employee Name:", leave["employee_name"])
        print("Leave Type:", leave.get("leave_type", "Not specified"))
        print("Leave Days:", leave["leave_days"])
        print("Status:", leave["status"])



def approve_leave():
    leaves = load_leaves()

    pending_requests = [
        (i, leave)
        for i, leave in enumerate(leaves)
        if leave["status"]=="Manager Approval Required"
    ]

    if not pending_requests:
        print("\n No Manager Approvals Pending!")
        return

    print("\n===Manager Approval Requests===")
    for i, leave in pending_requests:
        print(
            f"Leave ID: {leave['leave_id']}"
            f" {leave['employee_name']} - "
            f"{leave['leave_days']} days"
        )

    choice = input("Enter Leave ID to approve: ").strip()

    selected_leave = next(
        (leave for leave in leaves
          if leave["leave_id"]==choice
        and leave["status"]=="Manager Approval Required"),
        None
    )

    if selected_leave is None:
        print("Invalid Leave ID or request not pending!")
        return

    selected_leave["status"]="Approved"
    save_leaves(leaves)
    print("\nLeave request approved successfully!")


def reject_leave():
    pass
def view_leave_balance():
    pass 