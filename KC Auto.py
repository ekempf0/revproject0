#Imports including functions from kcaf
from kcaf import *
import pymongo
from pymongo import MongoClient

#First input, used to determine type of user
x = str(input("Welcome to KC Auto! \nIf you are a returning customer, please enter your phone number. \nIf you are an employee, please enter your employee ID\n\n"))

#Connection to the DB
client = pymongo.MongoClient("localhost", 27017)
db = client['testdb1']

#Establishing the Loop
end = "t"
while end != "s":

#Checking for user type
    if len(str(x)) < 5:
        db.Employees

#Checking for Manager Status
        if x == "1002" or x == "1006":

#If Manager Status is met, displaying Manager options
            menu()

#Finding Current Employees
            opt1 = str(input("\nPlease enter the number that corresponds with your choice:\t"))
            if opt1 == "1":
                empid = str(input("\nPlease enter the Employee's ID:\t"))
                r =db.Employees.find( { "emp_id" : empid } , {"_id" : 0})
                for i in r:
                    print(i)
                print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                end = str(input())

#Altering Current Employee Information (sub-options provided for each piece of data)
            elif opt1 == "2":
                menu2()
                subopt1 = str(input("\nPlease enter the number that corresponds with your choice:\t"))
                r =db.Employees.find({}, {"_id" : 0})
                for i in r:
                    print(i)
                subx = str(input("\nPlease Select the ID of the Employee you would like to Change:\t"))
                if subopt1 == "1":    
                    myquery = { "emp_id": subx }
                    suby = str(input("\nWhat should their new ID be:\t"))
                    newvalues = { "$set": { "emp_id": suby } }
                    db.Employees.update_one(myquery, newvalues)
                    r =db.Employees.find( { "emp_id" : suby } , {"_id" : 0})
                    for i in r:
                        print(i)
                    print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                    end = str(input())
                elif subopt1 == "2":
                    myquery = { "emp_id": subx }
                    suby = str(input("\nWhat should their First Name acutally be:\t"))
                    newvalues = { "$set": { "emp_fname": suby } }
                    db.Employees.update_one(myquery, newvalues)
                    r =db.Employees.find( { "emp_fname" : suby } , {"_id" : 0})
                    for i in r:
                        print(i)
                    print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                    end = str(input())
                elif subopt1 == "3":
                    myquery = { "emp_id": subx }
                    suby = str(input("\nWhat should their Last Name acutally be:\t"))
                    newvalues = { "$set": { "emp_lname": suby } }
                    db.Employees.update_one(myquery, newvalues)
                    r =db.Employees.find( { "emp_lname" : suby } , {"_id" : 0})
                    for i in r:
                        print(i)
                    print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                    end = str(input())
                elif subopt1 == "4":
                    myquery = { "emp_id": subx }
                    suby = str(input("\nWhat should their Salary acutally be:\t"))
                    newvalues = { "$set": { "emp_salary": suby } }
                    db.Employees.update_one(myquery, newvalues)
                    r =db.Employees.find( { "emp_salary" : suby } , {"_id" : 0})
                    for i in r:
                        print(i)
                    print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                    end = str(input())
                elif subopt1 == "5":
                    myquery = { "emp_id": subx }
                    suby = str(input("\nWhat should their Managerial Status acutally be:\t"))
                    newvalues = { "$set": { "is_Manager": suby } }
                    db.Employees.update_one(myquery, newvalues)
                    r =db.Employees.find( { "is_Manager" : suby } , {"_id" : 0})
                    for i in r:
                        print(i)
                    print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                    end = str(input())
                else:
                    print("Please select one of the options from the menu:\t")

#Removing an Employee from the DB
            elif opt1 == "3":
                r =db.Employees.find({}, {"_id" : 0})
                for i in r:
                    print(i)
                firedemp = str(input("\nPlease Select the ID of the Employee who has been let go:\t"))
                myquery = { "emp_id": firedemp }
                db.Employees.delete_one(myquery)
                print("\nThe Employee Roster has been Updated:")
                r1 =db.Employees.find({}, {"_id" : 0})
                for i in r1:
                    print(i)
                print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                end = str(input())
            
#Adding a New Employee
            elif opt1 == "4":
                eid = str(input("\nPlease Enter the New Employee's ID:\t"))
                efn = str(input("\nPlease Enter the New Employee's First Name:\t"))
                eln = str(input("\nPlease Enter the New Employee's Last Name:\t"))
                esy = str(input("\nPlease Enter the New Employee's Salary:\t"))
                emg = str(input("\nFinally Please Enter Yes or No for the New Employee's Managerial Status:\t"))
                mydict = { "emp_id": eid, "emp_fname": efn, "emp_lname" : eln, "emp_salary" : esy, "is_manager" : emg }
                db.Employees.insert_one(mydict)
                r2 =db.Employees.find({}, {"_id" : 0})
                for i in r2:
                    print(i)
                print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                end = str(input())
    
#Closing the Program
            elif opt1 == "5":
                break

#Simple error catch
            else:
                print("\n Sorry, but you must select one of the options from the Menu")
        
#User type check for Employee but not Manager
        else:
            db.Customers
            emp_menu()
            opt2 = str(input("Please Enter the Number that Corresponds with your choice:\t"))
            
#Creating a New Sale            
            if opt2 == "1":
                print("Please Enter the Customer's Information to Complete the Sale:")
                cfn = str(input("\nPlease Enter the Customer's First Name:\t"))
                cln = str(input("\nPlease Enter the Customer's Last Name:\t"))
                cad = str(input("\nPlease Enter the Customer's Address:\t"))
                cpn = str(input("\nPlease Enter the Customer's Phone Number:\t"))
                vep = str(input("\nPlease Enter the type of Vehicle Purchased:\t"))
                amt = str(input("\nPlease Enter the Amount Paid:\t"))
                mydict = { "cfname": cfn, "clname": cln, "address" : cad, "phone" : cpn, "vehicle_purchased" : vep, "amount paid": amt }
                db.Customers.insert_one(mydict)
                r2 =db.Customers.find({}, {"_id" : 0})
                for i in r2:
                    print(i)
                print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                end = str(input())    
            
#Searching for Previous Sales            
            elif opt2 == "2":
                custpn = str(input("\nPlease enter the Customer's Phone Number:\t"))
                r =db.Customers.find( { "phone" : custpn } , {"_id" : 0})
                for i in r:
                    print(i)
                print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
                end = str(input())
            
#Closing the Program            
            elif opt2 == "3":
                break

#Another Simple Error Catch            
            else:
                print("\n Sorry, but you must select one of the options from the Menu")


#Final check for user type (must be customer)
    else:
        db.Customers
        print("[1] See Your Current Information")
        print("[2] Close the Program")
        opt3 = str(input("Please enter the number that corresponds with your choice:\t"))
        
#Finding their "public facing" records via their phone number        
        if opt3 == "1":
            r =db.Customers.find( { "phone" : x } , {"_id" : 0})
            for i in r:
                print(i)
            print("\nIf you would like to make another selection type c to continue, if you are satisfied type s to close the program.")
            end = str(input())
#Closing the Program        
        elif opt3 == "2":
            break

#The final simple error catch
        else:
            print("\n Sorry, but you must select one of the options from the Menu")
print("Thank you for using KC Auto")



#Improvements for future iterations

    #Login Validation/Stronger Security

    #GUI integration for a better user experience

    #More complex error catching/prevention

    #Integration with a car DB/application for easier purchasing and record keeping