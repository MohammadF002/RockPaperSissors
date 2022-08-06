import os
import pickle
import random
import sys
import time
def clear() :
    if os.name == 'posix' :
        os.system('clear')
    elif os.name == 'nt' :
        os.system('cls')


class User :
    all_users = []
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.number_of_wins = 0
        self.number_of_losses = 0
        self.number_of_games = 0
        User.all_users.append(self)


    def get_password(self):
        return self.password

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_number_of_wins(self):
        return self.number_of_wins
    
    def get_number_of_losses(self):
        return self.number_of_losses

    def get_number_of_games(self):
        return self.number_of_games

    def get_win_rate(self):
        if self.number_of_games == 0:
            return None
        return int((self.number_of_wins / self.number_of_games)*100)

    def set_number_of_wins(self, number_of_wins):
        self.number_of_wins = number_of_wins

    def set_number_of_losses(self, number_of_losses):
        self.number_of_losses = number_of_losses

    def set_number_of_games(self, number_of_games):
        self.number_of_games = number_of_games

    @classmethod
    def set_all_users(cls, all_users):
        cls.all_users = all_users

    @classmethod
    def get_all_users(cls):
        return cls.all_users


    @staticmethod
    def get_user_by_username(username):
        for user in User.all_users:
            if user.username == username:
                return user
        return None

class Menu :

    @staticmethod
    def run() :
        while True:
            print("Main Menu:" + "\n" + "1. Signup" + "\n" + "2. Login" + "\n" + "3. Scoreboard" + "\n" + "4. Exit")
            choice = int(input())
            if choice == 1 :
                clear()
                Menu.SignUp()
            elif choice == 2:
                clear()
                Menu.Login()
            elif choice == 3:
                clear()
                Menu.print_scoreboard()
            elif choice == 4:
                clear()
                with open('users.dat', 'wb') as f:
                    pickle.dump(User.get_all_users(), f)
                sys.exit(0)

    @staticmethod
    def print_scoreboard():
        all_users = User.get_all_users()
        print("Username\tWinrate\tWins\tLosses")
        for user in all_users:
            print(user.get_username() + "\t" + str(user.get_win_rate()) + "\t" + str(user.get_number_of_wins()) + "\t" + str(user.get_number_of_losses()))

    @staticmethod
    def SignUp() :
        print("Signup page")
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        if User.get_user_by_username(username) == None:
            User(name, username, password)
        else:
            print("This Username is used before!")
            time.sleep(3)
        clear()
        Menu.run()

    @staticmethod
    def Login():
        print("Login page")
        username = input("Username: ")
        password = input("Password: ")
        user = User.get_user_by_username(username)
        if user == None:
            print("Username doesn't exists")
        elif user.get_password() != password:
            print("Invalid password")
        else:
            clear()
            Menu.Userpanel(user)
        time.sleep(2)
        clear()
        Menu.run()

    @staticmethod
    def Userpanel(user):
        print("Welcome " + user.get_name())
        print("1. Start Game\n" + "2. Stats\n" + "3. Logout")
        choice = int(input())
        if choice == 1:
            clear()
            user.set_number_of_games(user.get_number_of_games() + 1)
            Menu.start_game(user)

        elif choice == 2:
            wins = user.get_number_of_wins()
            losses = user.get_number_of_losses()
            win_rate = user.get_win_rate()
            print("Number of wins: " + str(wins) + "\nNumber of losses: " + str(losses) + "\nWin rate: " + str(win_rate))
            print("Press Enter to exit")
            input()
            clear()
            Menu.Userpanel(user)
        elif choice == 3:
            clear()
            Menu.run()

    @staticmethod
    def start_game(user):
        score_limit = int(input("Set score limit: "))
        computer_score = 0
        user_score = 0
        rps = ["Rock", "Paper", "Sissors"]
        while computer_score < score_limit and user_score < score_limit:
            print("Computer: " + str(computer_score) + "\t" + user.get_name() + ": " + str(user_score))
            print("1. Rock\n" + "2. Paper\n" + "3. Sissors")
            user_choice = int(input())
            computer_choice = random.randint(1, 3)
            if user_choice == computer_choice:
                print("Equal")
                time.sleep(2)
                clear()
                continue
            if user_choice - computer_choice == 1 or user_choice - computer_choice == -2:
                user_score += 1
            else:
                computer_score += 1
            print("Your choice: " + rps[user_choice - 1] + "\n" "Computer choice: " + rps[computer_choice - 1])
            time.sleep(2)
            clear()
        if computer_score < user_score:
            print("You Won!")
            user.set_number_of_losses(user.get_number_of_wins() + 1)
        elif computer_score > user_score :
            print("You Lost!")
            user.set_number_of_wins(user.get_number_of_losses() + 1)
        time.sleep(2)
        clear()
        Menu.Userpanel(user)
        


if not os.path.exists('users.dat'):
    open('users.dat', 'a+')
    with open('users.dat', 'wb') as f:
        pickle.dump([], f)
with open('users.dat', 'rb') as f:
    User.set_all_users(pickle.load(f))

Menu.run()