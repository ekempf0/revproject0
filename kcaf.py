#Functions(In this case just menus)

#First Manager Menu
def menu():
    print("[1] Find an existing Employee")
    print("[2] Alter an existing Employee")
    print("[3] Remove an existing Employee")
    print("[4] Add a new Employee")
    print("[5] Close the Program")

#Manager Menu for Altering Employees specifically
def menu2():
    print("\nPlease select the information you want to alter:\t")
    print("[1] Employee ID")
    print("[2] Employee First Name")
    print("[3] Employee Last Name")
    print("[4] Salary")
    print("[5] Managerial Status")
    print("[6] Close the Program")

#Menu for regular Employees
def emp_menu():
    print("[1] Create a Sale")
    print("[2] Search Customer's and their previous Purchases")
    print("[3] Close the Program")


        # Ideas for Manager check on login
        # for line ~30 and 31 
        # x = db.Employees.aggregate([{"is_Manager": {"$eq": "Yes"}}])
        # print(x)