import ast


class Voting:

    def __init__(self):
        print("voting program is starting now")
        self.students: dict = {
                            0: {"name": "James", "v_mark": 0, "points": 0, "voter": []},
                            1: {"name": "Alex", "v_mark": 0, "points": 0, "voter": []},
                            2: {"name": "John", "v_mark": 0, "points": 0, "voter": []},
                            3: {"name": "Ronaldo", "v_mark": 0, "points": 0, "voter": []},
                            4: {"name": "Messi", "v_mark": 0, "points": 0, "voter": []},
                        }

        self.db: dict = {}
        self.id: int = 0
        self.l_id = -1
        self.item = []

    def main_option(self):

        try:
            option = int(input("press 1 to Register: \npress 2 to Login: \npress 3 to Exit: "))

            if option == 1:
                self.register()
            elif option == 2:
                self.login()
            elif option == 3:
                self.recording_all_data()
                exit(1)
            else:
                print("Invalid option!")
                self.main_option()
        except Exception as err:
            print(err,"Only given numbers can be enter.Please try again!")
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
            data_form: dict = {self.id:{"name": r_name,"email": r_email,"phone": r_phone,"address": r_address,"show_money": 5000,"points": 0,"password": r_pass1}}
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
                    self.recording_all_data()
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

        v_check = False
        while v_check is False:
            print("Welcome {} Your total amount - ${}  ".format(self.db[l_id]["name"], self.db[l_id]["show_money"]))
            print("Your total point - ", self.db[l_id]["points"])

            print("Just select one")
            for i in range(len(self.students)):
                print("Id: {} Name: {} Current Voting Mark- {}".format(i, self.students[i]["name"],
                                                                       self.students[i]["v_mark"]))
            try:
                v_id = int(input("Just Enter Id to Vote: "))
                if self.db[l_id]["points"] != 0:
                    self.students[v_id]["v_mark"] += 1
                    self.students[v_id]["points"] += 1
                    self.students[v_id]["voter"].append(self.db[l_id]["name"])
                    self.db[l_id]["points"] -= 1

                    print("Congratulation your are voted")

                    print(
                        "{} Now Voting Mark is - {}".format(self.students[v_id]["name"], self.students[v_id]["v_mark"]))

                    for i in self.students[v_id]["voter"]:
                        print("Voter: ", i)

                    # v_check = True
                else:
                    print("You don't have point.Please buy a point first!($500 PER POINT)")
                    self.buy_point(l_id)

                while True:
                    try:
                        vote_option = int(
                            input(
                                "Press 1 to Vote Again: \nPress 2 to Main Option: \nPress 3 to Force Quit: "))
                        if vote_option == 1:
                            self.user_info(l_id)
                            break
                        elif vote_option == 2:
                            self.main_option()
                            break
                        elif vote_option == 3:
                            self.recording_all_data()
                            exit(1)
                        else:
                            print("Invalid Option!")
                    except Exception as err:
                        print(err)

            except Exception as err:
                print("Only numbers can be enter")

    def buy_point(self,l_id):
        print("Your total amount - ${}".format(self.db[l_id]["show_money"]))
        while True:
            try:
                point = int(input("Buy Point: "))
                if self.db[l_id]["show_money"] != 0:
                    if point <= 0:
                        print("please buy a point!")
                    else:
                        if point * 500 > self.db[l_id]["show_money"]:
                            print("Not Enough Money")
                            print("Mininum 1 POINT && Maximun 10 POINTS PER USER")
                        else:
                            self.db[l_id]["points"] = point
                            self.db[l_id]["show_money"] -= point * 500
                            break
                else:
                    print("You don't left money to buy vote.")
                    print("Thank for your participation:)")
                    break
            except Exception as err:
                print(err)

    def seeding_students(self):
        with open("voting.txt",'a') as stud:
            for i in range(len(self.students)):
                s_name = self.students[i]["name"]
                v_mark = self.students[i]["v_mark"]
                voter = self.students[i]["voter"]
                s_points = self.students[i]["points"]
                student_form = s_name+'^'+str(v_mark)+'^'+str(voter)+'^'+str(s_points)+'^'
                stud.write(student_form)
                stud.write('\n')

    def recording_all_data(self):
        with open("voting-db.txt",'w') as db:
            for i in range(len(self.students)):
                db.write(str(self.students[i])+'^')
                db.write('\n')

            db.write('===')
            db.write('\n')

            for i in range(len(self.db)):
                db.write(str(self.db[i])+'^')
                db.write('\n')


    def loading_all_data(self):
        if len(self.db) != 0:
            voting_txt = ""
            with open("voting-db.txt", 'r') as db:
                datas = db.readlines()
                for i in datas:
                    i = i.replace('\n', '')
                    voting_txt += i.ljust(1)

            voting_txt = voting_txt.split('===')
            db_students = voting_txt[0].split('^')
            db_students.pop(len(db_students) - 1)
            self.students = {}
            for student in db_students:
                self.id = len(self.students)
                data_form = {self.id: ast.literal_eval(student)}
                self.students.update(data_form)

            db_users = voting_txt[1].split('^')
            db_users.pop(len(db_users) - 1)
            for user in db_users:
                self.id = len(self.db)
                data_form = {self.id: ast.literal_eval(user)}
                self.db.update(data_form)