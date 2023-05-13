class Voting:

    def __init__(self):
        print("voting program is starting now")
        self.students = {
                            0: {"name": "James", "v_mark": 0, "voter": []},
                            1: {"name": "Alex", "v_mark": 0, "voter": []},
                            2: {"name": "John", "v_mark": 0, "voter": []},
                            3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                            4: {"name": "Messi", "v_mark": 0, "voter": []},
                        }
        self.db: dict = {}
        self.id: int = 0
        self.l_id = -1

    def main_option(self):

        try:
            option = int(input("press 1 to Register: \npress 2 to Login: \npress 3 to Exit: "))

            if option == 1:
                self.register()
            elif option == 2:
                self.login()
            elif option == 3:
                exit(1)
            else:
                print("Invalid option!")
                self.main_option()
        except Exception as err:
            print("Only given numbers can be enter.Please try again!")
            self.main_option()

    def register(self):
        print("This is Register option")
        is_int = False
        r_name = input("Enter your name: ")
        r_email = input("Enter your email: ")
        r_phone = -1
        while is_int is False:
            try:
                r_phone = int(input("Enter your phone: "))
                is_int = True
            except Exception as err:
                print("phone number field must be integer!")
        r_address = input("Enter your address: ")
        r_pass1 = input("Enter your password: ")
        r_pass2 = input("Enter your confirm password: ")

        if r_pass1 != r_pass2:
            print("Your password doesn't match.Please try again!")
            self.register()
        else:
            self.id = len(self.db)
            data_form: dict = {self.id:{"name": r_name,"email": r_email,"phone": r_phone,"address": r_address,"password": r_pass1}}
            self.db.update(data_form)

        option_check = False
        while option_check is False:
            try:
                u_option = int(input("Press 1 to Login: \nPress 2 to Main_menu: \nPress 3 to Exit: "))

                if u_option == 1:
                    self.login()
                    option_check = True
                elif u_option == 2:
                    self.main_option()
                    option_check = True
                elif u_option == 3:
                    exit(1)
                else:
                    print("Invalid option!")
            except Exception as err:
                print("Only given numbers can be enter.Please try again!")
    def login(self):
        print("This is Login option")
        pass_match = -1
        l_email = input("Enter your email to Login: ")
        l_pass = input("Enter your password to Login: ")

        length = len(self.db)
        for i in range(length):
            if l_email == self.db[i]["email"] and l_pass == self.db[i]["password"]:
                self.l_id = i
                pass_match = i
        if pass_match != -1:
            self.user_info(self.l_id)
        else:
            print("The credential doesn't match.Please try again!")
            self.login()

    def user_info(self,l_id):
        print("Welcome, ", self.db[l_id]["name"])

        print("Just select one")
        for i in range(len(self.students)):
            print("Id: {} Name: {} Current Voting Mark- {}".format(i, self.students[i]["name"], self.students[i]["v_mark"]))

        v_check = False
        while v_check is False:
            try:
                v_id = int(input("Just Enter Id to Vote: "))
                self.students[v_id]["v_mark"] += 1
                print("Congratulation your are voted")

                print("{} Now Voting Mark is - {}".format(self.students[v_id]["name"],self.students[v_id]["v_mark"]))

                self.students[v_id]["voter"].append(self.db[l_id]["name"])

                for i in  self.students[v_id]["voter"]:
                    print("Voter: ", i)

                while True:
                    try:
                        vote_option = int(
                            input("Press 1 to Vote Again: \nPress 2 to Main Option: \nPress 3 to Force Quit: "))
                        if vote_option == 1:
                            self.user_info(l_id)
                            break
                        elif vote_option == 2:
                            self.main_option()
                            break
                        elif vote_option == 3:
                            exit(1)
                        else:
                            print("Invalid Option!")
                    except Exception as err:
                        print(err)

                v_check = True
            except Exception as err:
                print("Only numbers can be enter")