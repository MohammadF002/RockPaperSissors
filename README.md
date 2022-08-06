# RockPaperSissors
This is a cli game and it's based on the famous Rock,Paper,Sissors game but with some more amazing options
First the records of all players are saved in an ".dat" file when you want to delete the records you can remove that file and records will be reset
There is also an score board where you can compare your stats with your friends and enjoy the game even more
enjoy the game
#Tech part
I have used oop basics to make this game there are two classes in this program User and Menu
User is the object of user containing all of a user properties that a user needs to have
Menu is a group of static methods that display different pages and menus
The way tha the User data is stored is by pickling it to the file "user.dat"
Every time the program is executed it will check if there is the user.dat file in the program directory if not it will make one and initializes it
And if it exists ther it initializes users list and every time when the program is terminated users.dat will be updated
