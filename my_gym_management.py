import json
class MyGymManagement:
    def __init__(self,userid):
        self.username = userid 
        self.full_name = userid["Name"]
        self.age = userid["Age"]
        self.gender = userid["Gender"]
        self.mobile = userid["Number"]
        self.email = userid["Email"]
        self.height = userid["Height"]
        self.weight = userid["Weight"]
        self.bmi = userid["BMI"]
        self.membership_duration = userid["Months"]
        self.password = userid["Password"]
        self.regimen = userid["Regimen"]
    def print_regimen(self):
        print("\n")
        for i in self.regimen:
            print(i)
    def view_profile(self):
        print("")
        for i in self.username:
            if i !="Password" and i!="Regimen":
                if i =="BMI":
                    j = "{:.2f}".format(self.username[i])
                    print(f"{i} : {j}")
                else:
                    print(f"{i} : {self.username[i]}")
    def update_info(self,info,change):
        with open("userdata.json") as data_file:
            data = json.load(data_file)
        data[self.mobile][info] = change
        data.update(data)
        with open("userdata.json","w") as data_file:
            json.dump(data,data_file,indent= 4)
    def get_regimen(self,bmi):
        if bmi <=18.5:
            return ["Mon: Chest","Tue: Biceps","Wed: Rest","Thu: Back","Fri: Triceps","Sat: Rest","Sun: Rest"]
        elif bmi <=25.0:
            return ["Mon: Chest","Tue: Biceps","Wed: Cardio/Abs","Thu: Back","Fri: Triceps","Sat: Legs","Sun: Rest"]
        elif bmi <=30.0:
            return ["Mon: Chest","Tue: Biceps","Wed: Abs/Cardio","Thu: Back","Fri: Triceps","Sat: Legs","Sun: Cardio"]
        else:
            return ["Mon: Chest","Tue: Biceps","Wed: Cardio","Thu: Back","Fri: Triceps","Sat: Cardio","Sun: Cardio"]
Start = True
while Start:
    user_input = input("1. Member.\n2. Super User.\nQ. Quit\n ")
    if user_input == "1":

        username = input("Enter Mobile number: ")

        try:
            with open("userdata.json") as data:
                json_data = json.load(data)
        except FileNotFoundError:
            print("Database is not found")
            
        if username in json_data:
            member = MyGymManagement(json_data[username])
            password = input("Password: ")
            if password == member.password:
                print(f"Welcome {member.full_name}!")
                loop = True
                while loop:
                    print("")
                    choice = input("1.View My Regimen\n2.View My Profile\n3.Update Profile\n4.Logout")
                    if choice == "1":
                        member.print_regimen()
                    elif choice == "2":
                        member.view_profile()
                    elif choice == "3":
                        info = input("Which information do you want to update\n1.Name\n2.Age\n3.Email\n4.Height(in m)\n5.Weight(in kg)\n6.Password:\n ").title()
                        change = input(f"Please Enter {info}: ")
                        member.update_info(info,change)
                    elif choice == "4":
                        loop = False
            else:
                print("Please check the password")
        else:
            print("User not found.")

    elif user_input == "2":
        loop = True
        while loop:

            with open("userdata.json") as data_file:
                data = json.load(data_file)
            SUPERUSER = MyGymManagement(data["SUPERUSER"])
            choice = input("1.Create Member\n2.View Member\n3.Delete Member\n4.Update Member\n5.Create Regimen\n6.View Regimen\n7.Delete Regimen\n8.Update Regimen\n9.Logout\n ")
            if choice == "9":
                loop = False
            elif choice == "5":
                height = float(input("Heigth in meters: "))
                weight = int(input("weight in kgs: "))
                bmi = round(weight/height**2,2)
                regimen = SUPERUSER.get_regimen(bmi)
                print("")
                for i in regimen:
                    print(i)
            elif choice == "2":
                for i in data:
                    if data[i]["Name"] != "SUPERUSER":
                        for x in data[i]:
                            if x == "Password":
                                pass
                            else:
                                print(f"{x} : {data[i][x]}")
                        print("-----------------------------")
                        print("")
            elif choice == "1":
                name = input("Name: ")
                age = input("Age: ")
                gender = input("Gender: ")
                height = float(input("Height in meters: "))
                weight = int(input("Weight in kgs: "))
                mobilenumber = input("Mobile Number: ")
                membership_months = int(input("Membership Months(1,3,6 or 12): "))
                email = input("Email ID: ")
                password = input("Password: ")
                bmi = round(weight/height**2)
                new_data={ mobilenumber:{"Name":name,
                               "Age":age,
                               "Gender":gender,
                               "Number":mobilenumber,
                               "Email":email,
                               "Height":height,
                               "Weight":weight,
                               "Months":membership_months,
                               "BMI":bmi,
                               "Password":password,
                               "Regimen":SUPERUSER.get_regimen(bmi)
                                         }
                             }
            
                data.update(new_data)
                with open ("userdata.json","w") as data_file:
                    json.dump(data,data_file,indent = 4)
            elif choice == "3":
                with open("userdata.json") as data_file:
                    data = json.load(data_file)
                member_num = input("Type the mobile number to delete the account.")
                del data[member_num]
                data.update(data)
                with open ("userdata.json","w") as data_file:
                    json.dump(data,data_file,indent = 4)
            elif choice == "8":
                with open("userdata.json") as data_file:
                    data = json.load(data_file)
                member_num = input("Type the member's mobile number to update regimen: ")
                height = float(input("Heigth in meters: "))
                weight = int(input("weight in kgs: "))
                bmi = round(weight/height**2,2)
                new_regimen = SUPERUSER.get_regimen(bmi)
                data [member_num]["Height"]=height
                data [member_num]["Weight"]=weight
                data [member_num]["BMI"]=bmi
                data [member_num]["Regimen"]=new_regimen
                data.update(data)
                with open ("userdata.json","w") as data_file:
                    json.dump(data,data_file,indent = 4)
            elif choice=="4":
                with open("userdata.json") as data_file:
                    data = json.load(data_file)
                member_num = input("Enter the mobile Number to Extend the subscription: ")
                if member_num not in data:
                    print("Member not found,please check the number.")
                else:
                    months = int(input("Membership Months(1,3,6 or 12): "))
#                     if months == 1 or months == 3 or months == 6 or months == 12:
#                         print("Please select a valid plan: ")
                data[member_num]["Months"] = months
                data.update(data)
                with open("userdata.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
                print("")
            elif choice =="6":
                with open("userdata.json") as data_file:
                    data = json.load(data_file)
                for i in data:
                    if i != "SUPERUSER":
                        print(f"{data[i]['Number']} : {data[i]['Regimen']}")
            elif choice == "7":
                with open("userdata.json") as data_file:
                    data = json.load(data_file)
                member_num = input("Type the member's mobile number to delete regimen: ")
                del data[member_num]["Regimen"]
                data.update(data)
                with open("userdata.json","w") as data_file:            
                    json.dump(data ,data_file,indent=4)
    elif user_input == "q"or user_input == "Q" :
        Start = False
