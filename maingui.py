# importing all the required files and packages
from tkinter import *  # tkinter package is a python interface to the tk GUI toolkit
from tkinter import ttk  # ttk is used for themed widgets
from tkinter import messagebox  # messagebox for pop up
# PIl is Python Imaging Library. It is used to add image processing capabilities to the Python interpreter
from PIL import ImageTk, Image


class App:
    def __init__(self, root):
        '''

            This is the constructor method

        :param root: the window of the app
        '''

        self.root = root
        # Initial health of the player
        self.health = 10000
        # Initial gold of the player
        self.gold = 0
        # backpack is used to store the healing portions
        self.backpack = 0
        # you can store items in the inventory
        self.inventory = []

        # adding a scroll bar

        # Creating a main frame
        self.main_frame = Frame(root)
        self.main_frame.pack(fill=BOTH, expand=1)

        # Creating a Canvas
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Adding a scrollbar to the canvas
        self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure the canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        # binding the canvas with the scrollbar using bbox (binding box)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # creating another frame inside the canvas
        # All the widgets will go in this frame so that scrollbar can be seen
        self.second_frame = Frame(self.my_canvas)

        # Add the second frame to a window in the canvas
        # (0,0) is the position for top right corner, nw = north West again the top right corner
        self.my_canvas.create_window((0,0),window=self.second_frame,anchor='nw')

        self.create_menu()  # This function will display the menu

        # Configure a grid layout with 3 columns and 20 rows
        self.second_frame.columnconfigure(0, pad=40)
        self.second_frame.columnconfigure(1, pad=40)
        self.second_frame.columnconfigure(2, pad=40)

        # using list comprehension to configure the rows
        [self.second_frame.rowconfigure(row, pad=30) for row in range(0, 120)]

        # Displaying the Game Logo/Image
        # Create the PIL image object
        self.bgi = Image.open('Images/Goblin_Slayer_cover.jpeg')
        # resizing the image
        self.bgi_re = self.bgi.resize((400, 300), Image.ANTIALIAS)
        self.bgimage = ImageTk.PhotoImage(self.bgi_re)

        # creating the image Label
        self.bgimageLabel = Label(self.second_frame, image=self.bgimage)
        # storing a reference to a photoimage
        self.bgimageLabel.image = self.bgimage
        self.bgimageLabel.grid(row=0, column=2)

        # Opening a text file in append mode
        # so that the text will be added at the end of the file.
        self.file = open("Game_log.txt",'w')

        # creating and displaying the Label using grid() on the second _frame
        self.name_label = Label(self.second_frame, text="Enter your Name")
        self.name_label.grid(row=2, column=2)

        # creating and displaying the Entry to get user input
        self.name = Entry(self.second_frame)
        self.name.grid(row=3, column=2)

        # creating and display the button that will call the age_function
        self.name_submit_button = Button(self.second_frame, text="Submit", command=self.age_function)
        self.name_submit_button.grid(row=4, column=2)

        self.print_welcome()  # calling the printWelcome function to display the welcome message

        for i in range(300):
            my_label = Label(self.second_frame, text=" ")
            my_label .grid(row=i, column=1)

    def check_age(self):
        '''

            Checking the age of the adventurer.
            The adventurer should be more than 18 to play this game.

        :return: None
        '''
        # using Exception handling
        # It will pop a messagebox if the user has entered wrong input
        try:

            age_integer = int(self.age.get())
            if age_integer >= 18:
                # creating and displaying the Label using grid() on the second _frame
                welcome_label = Label(self.second_frame, text="You are eligible to play the game.")
                welcome_label.grid(row=7, column=2)

                # creating and display the button that will call the function first_floor
                play_game_button = Button(self.second_frame, text="Enter", command=self.first_floor, fg="GREEN")
                play_game_button.grid(row=8, column=2)
            else:
                self.exit_game1()  # Quit the game

        except ValueError:
            self.age.configure(text='')  # This will clear the entry, to reenter the age
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error", "Age should have only Numbers")

    def create_menu(self):
        '''
            Adding, Configuring and Cascading the menu

        :return: None
        '''

        self.my_menu = Menu(self.root)  # Adding a top level menu
        self.root.config(menu=self.my_menu)  # configuring the menu

        # Creating a menu item
        self.quit_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Quit', menu=self.quit_menu)
        self.quit_menu.add_command(label='Quit the Game', command=self.root.quit)

        # Creating a menu item
        self.help_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='HELP', menu=self.help_menu)
        self.help_menu.add_command(label='About the Game', command=lambda: self.do_print_help())
        self.help_menu.add_separator()  # adding a separator between the menu items
        self.help_menu.add_command(label='Player Status', command=lambda: self.get_player_status())

    def add_heal_to_menu(self):
        '''

            This method will add and cascade a new menu item

        :return:
        '''

        # Creating a menu item
        self.heal_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="HEAL", menu = self.heal_menu)
        self.heal_menu.add_command(label="Use Healing Potion", command=lambda: self.use_healing_potion())
        self.help_menu.add_separator()  # adding a separator between the menu items

    def age_function(self):
        '''
            Ask the adventurer for his age and call the
            check_age function to check if he can play the game or not

        :return: None
        '''

        # creating and displaying the Label using grid() on the second _frame
        age_label = Label(self.second_frame, text="Hi, "+self.name.get()+" What's your age?")
        age_label.grid(row=4 ,column=2)

        # This variable will store teh age of the adventurer
        # creating and displaying the Entry to get user input
        self.age = Entry(self.second_frame)
        self.age.grid(row=5, column=2)

        # creating and display the button that will call the function check_age
        self.age_submit_button = Button(self.second_frame, text="Submit", command=self.check_age)
        self.age_submit_button.grid(row=6, column=2)

    def print_welcome(self):
        """
                Displays a welcome message
                This gives the description of the game.

            :return: none
        """
        msg = \
            f"Welcome to the world of Goblins \n \
            You are a Goblin Slayer.\n \
            The main objective of the game is to enter the Dungeon and kill the goblins to claim the treasure.\n \
            The Dungeon consists of 11 floors, the treasure is on the last floor.\nYou will be carrying a backpack to store your Health Portion and the Gold you collect on the way.\n \
            Everytime you get a hit, you will loose some health. If you kill Goblins you will get Gold as a reward.\n" \
            f"ALL COMMANDS are present in the menu bar at the top of the window\n" \
            f"Use the scrollbar at the top right corner for best game experience."

        # creating and displaying the Label using grid() on the second _frame
        welcome_label = Label(self.second_frame, text=msg)
        welcome_label.grid(row=1, column=2)

    def do_print_help(self):
        '''

                This function will display the Objectives of the game

        :return: None
        '''

        msg = \
            f"Welcome to the world of Goblins \n \
            You are a Goblin Slayer.\n \
            The main objective of the game is to enter the Dungeon and kill the goblins to claim the treasure.\n \
            The Dungeon consists of 11 floors, the treasure is on the last floor.\nYou will be carrying a backpack to store your Health Portion and the Gold you collect on the way.\n \
            Everytime you get a hit, you will loose some health. If you kill Goblins you will get Gold as a reward.\n" \
            f"ALL COMMANDS are present in the menu bar at the top of the window\n" \
            f"Use the scrollbar at the top right corner for best game experience."
        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("HELP", msg)

    def get_player_status(self):
        '''

            This method will display the player status which is the
            health the player has left,
            gold the player collected and
            healing portion the playing is carrying in the backpack.

        :return:none
        '''

        msg = f"HEALTH ={self.health}\n" \
              f"GOLD={self.gold}\n" \
              f"Healing Potions={self.backpack}"
        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("Status", msg)

    def use_healing_potion(self):
        '''

            This method is used to heal the player

        :return: none
        '''

        if self.backpack != 0:
            msg = f"You can only use 1 Healing portion at a time." \
                f"You have {self.backpack} Healing portions.\n\n" \
                f"Used 1 Healing Portion"
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Healing potion", msg)
            self.backpack -= 1  # reducing 1 health portion
        else:
            # messagebox will pop to guide the adventurer with message
             messagebox.showinfo("Status", "You don't have Healing potion")

    def exit_game1(self):
        '''
            Display a message using messagebox and exit the game

        :return: None
        '''
        # Entering data into the file
        self.file.write(f"\n Game Exit")

        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("Exit", "Sorry you have to wait till you turn 18\n Thank you for playing")
        self.second_frame.quit()  # end the game by destroying the window

    def exit_game2(self):
        '''
            Display a message using messagebox and exit the game

        :return: None
        '''

        # Entering data into the file
        self.file.write(f"\n Game Exit")

        msg = f"The dragon has killed you.\n" \
              f"If you had Hagboon as friend he would have helped you in the battle.\n" \
              f"You have lost the game.\n\n" \
              f"Thanks for playing!"
        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("ERROR", msg)
        self.second_frame.quit()  # end the game by destroying the window

    def exit_game3(self):
        '''
            Display a message using messagebox and exit the game

        :return: None
        '''

        # Entering data into the file
        self.file.write(f"\n Game Exit")

        msg = f"If you had Hagboon as friend he would have helped you in the battle.\n" \
              f"You have lost the game.\n" \
              f"Thanks for playing!"
        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("ERROR", msg)
        self.second_frame.quit()  # end the game by destroying the window

    def exit_game4(self):
        '''
            Display a message using messagebox and exit the game

        :return: None
        '''

        # Entering data into the file
        self.file.write(f"\n Game Exit")

        msg = f"The dragon takes this opportunity and attacks you.\n" \
              f"You die defending its attacks.\n" \
              f"Health=0\n\n" \
              f"Thanks for playing."
        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("ERROR", msg)
        self.second_frame.quit()  # end the game by destroying the window

    def exit_game5(self):
        '''
            Display a message using messagebox and exit the game

        :return: None
        '''

        # Entering data into the file
        self.file.write(f"\n Game Exit")

        msg = f"You have completed the objective of the game.\n" \
              f"Enjoy the rewards."
        # messagebox will pop to guide the adventurer with message
        messagebox.showinfo("ERROR", msg)
        self.second_frame.quit()  # end the game by destroying the window

    def first_floor(self):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :return: none
        '''

        msg=\
            f"This is the First Floor of the Dungeon. \n " \
            f"On this floor all the adventures get to pick up a weapon to fight with the goblins.\n" \
            f"You have a sword on the left and Magic Staff on the right."

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=9, column=2)

        # Entering data into the file
        self.file.write(msg)

        # displaying the image of sword and magic staff
        # Create the PIL image object
        self.sword = Image.open('Images/weapon.JPG')
        # resizing the image
        self.sword_re = self.sword.resize((200, 200), Image.ANTIALIAS)
        self.sword_image = ImageTk.PhotoImage(self.sword_re)

        # creating the image Label
        self.sword_image_Label = Label(self.second_frame, image=self.sword_image)
        # storing a reference to a photoimage
        self.sword_image_Label.image = self.sword_image
        self.sword_image_Label.grid(row=10, column=2)

        # using Exception handling
        # It will pop a messagebox if the user has entered wrong input
        try:
            # creating and displaying the Label using grid() on the second _frame
            self.choice = Label(self.second_frame, text="Which one will you choose (Sword/Magic staff):")
            self.choice.grid(row=11, column=2)
            # creating and displaying the Entry to get user input
            self.weapon = Entry(self.second_frame)
            self.weapon.grid(row=12, column=2)
            self.confirm = Button(self.second_frame, text="Confirm", command=self.user_weapon)
            self.confirm.grid(row=13, column=2)
        except ValueError:
            messagebox.showinfo("Wrong Input", "Please enter the correct option ")

    def user_weapon(self):
        '''

                This method will store the picked weapon

        :return: none
        '''

        weapon=self.weapon.get().lower()  # converting into lower case to avoid casing error

        if (weapon == 'sword') or (weapon == 'magic staff'):
            # creating and displaying the Label using grid() on the second _frame
            text = Label(self.second_frame,
                         text=f"Congratulations Adventurer on picking up the right weapon for you. \nThis {weapon.upper()} will help you kill the Goblins you encountered")
            text.grid(row=14, column=2)

            # Entering data into the file
            self.file.write("\nWeapon= Sword")
        else:
            # creating and displaying the Label using grid() on the second _frame
            text = Label(self.second_frame, text = "Please pick the correct weapon")
            text.grid(row=15, column=2)

            # Entering data into the file
            self.file.write(f"\n Player entered incorrect input")

        # creating and display the button that will call the function second_floor
        self.second = Button(self.second_frame, text="Enter Second Floor", command=self.second_floor,fg="GREEN")
        self.second.grid(row=16, column=2)


    def second_floor(self):
        '''

            This method will enter the next floor and display the objectives of the new floor

        :return: none
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()
        msg = \
        f"Welcome! to the second floor.\n" \
        f"It is very dark on this floor, so keep your guard up.\n" \
        f"Goblins are know to attack in the dark. While walking to encounter a low level goblin.\n" \
        f"These creatures are devious, mischievous and pure creatures.\n"

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=17, column=2)

        # Entering data into the file
        self.file.write(f'\n {msg}')

                # image of low level goblin

        # Create the PIL image object
        self.goblin1 = Image.open('Images/low_level_goblin.jpeg')
        # resizing the image
        self.goblin1_re = self.goblin1.resize((200, 200), Image.ANTIALIAS)
        self.goblin1_image = ImageTk.PhotoImage(self.goblin1_re)

        # creating the image Label
        self.goblin1_image_Label = Label(self.second_frame, image=self.goblin1_image)
        # storing a reference to a photoimage
        self.goblin1_image_Label.image = self.goblin1_image
        self.goblin1_image_Label.grid(row=18, column=2)


        # creating and displaying the Label using grid() on the second _frame
        self.choice = Label(self.second_frame, text="Will you kill it or run from it? (kill/run)").grid(row=19,column=2)

        # creating and displaying the Entry to get user input
        self.choice2 = Entry(self.second_frame)
        self.choice2.grid(row=20,column=2)

        # creating and display the button that will call the function second_floor1
        second = Button(self.second_frame, text="Enter", command=self.second_floor1)
        second.grid(row=21, column=2)

    def second_floor1(self):
        '''

            This method will check the option entered by the user

        :return: none
        '''

        choice2 =self.choice2.get().lower()  # converting into lower case to avoid casing error

        if (choice2 == 'kill') or (choice2 == 'run'):  # input validation
            if choice2 == 'kill':
                msg = f"Since it was a low level Goblin you could easy kill it. \nHence no health loss. \nAs a reward you receive 10 GOLD coins"
                # creating and displaying the Label using grid() on the second _frame
                text = Label(self.second_frame, text=msg)
                text.grid(row=22, column=2)
                self.gold += 10 # Adding Gold for the achievement

                # Entering data into the file
                self.file.write("Killed the goblin")
            else:
                # creating and displaying the Label using grid() on the second _frame
                text = Label(self.second_frame, text="WOW!! you can run fast, but everytime you won't be this lucky.")
                text.grid(row=22, column=2)

                # Entering data into the file
                self.file.write("Ran away from the Goblin")

            # creating and display the button that will call the function thrid_floor
            self.third = Button(self.second_frame, text="Enter Third Floor", command=self.thrid_floor, fg="GREEN")
            self.third.grid(row=23, column=2)

        else:
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("ERROR....", "Please enter the right choice.")

    def thrid_floor(self):
        '''

            This method will enter the next floor and display the objectives of the new floor

        :return:
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()
        msg=f"The THIRD FLOOR is not dark, there are lights on this floor. " \
            f"\nBut the floor is full with water which contains Sharks.\n" \
            f"You have two options: \n\t " \
            f"1. You can choose to buy a boat from the inventory which will cost 5 gold.\n\t " \
            f"2.you can swim in the water where you can loose 1000 hit points as the sharks will bite you.\n\t " \
            f"What do you choose (1/2): "
        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=24, column=2)

        # Entering data into the file
        self.file.write(msg)

        # creating and displaying the Entry to get user input
        self.choice3 = Entry(self.second_frame)
        self.choice3.grid(row=25, column=2)

        # creating and display the button that will call the function third_floor_1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.third_floor_1)
        button.grid(row=26, column=2)


    def third_floor_1(self):
        '''

            This method will check the option entered by the user

        :return: none
        '''

        choice= int(self.choice3.get()) # fetching the value from the entry

        # using Exception handling
        # It will pop a messagebox if the user has entered wrong input
        try:

            if choice == 1:
                if self.gold >= 5:
                    msg=f"The boat has arrived.\n" \
                        f"It will take a few minutes to cross the water."
                    # creating and displaying the Label using grid() on the second _frame
                    msg_label = Label(self.second_frame, text=msg)
                    msg_label.grid(row=27, column=2)
                    self.gold -= 5

                    # Entering data into the file
                    self.file.write("\nChoose option 1")

                else:
                    # Entering data into the file
                    self.file.write(f"\n Player entered incorrect input")

                    # messagebox will pop to guide the adventurer with message
                    messagebox.showinfo("Error", "You don't have enough Gold to buy a boat. Reconsider your options")

            else:
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text = "You have crossed the water. That was a long swim. \nTake a deep breath and relax your self.")
                msg_label.grid(row=29, column=2)
                self.health -= 1000  # Reducing the health of the player fro the hit

                # Entering data into the file
                self.file.write("Choose option 2")

        except ValueError:
            messagebox.showinfo("Error", "INVALID INPUTS")

        finally:
            # creating and display the button that will call the function fourth_floor
            self.fourth = Button(self.second_frame, text="Enter Fourth Floor", command=self.fourth_floor, fg="GREEN")
            self.fourth.grid(row=30, column=2)


    def fourth_floor(self):
        """

            This method will enter the next floor and display the objectives of the new floor

        :return: none
        """

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()

                  # image of Hobglobin

        # Create the PIL image object
        self.goblin3 = Image.open('Images/hobgoblin.jpeg')
        # resizing the image
        self.goblin3_re = self.goblin3.resize((400, 300), Image.ANTIALIAS)
        self.goblin3_image = ImageTk.PhotoImage(self.goblin3_re)

        # creating the image Label
        self.goblin3_image_Label = Label(self.second_frame, image=self.goblin3_image)
        # storing a reference to a photoimage
        self.goblin3_image_Label.image = self.goblin3_image
        self.goblin3_image_Label.grid(row=31, column=2)


        msg=f"At the entrance of the fourth floor there is a Hobgoblin waiting for you.\n" \
            f"This Hobgoblin is at a higher level than the goblin you previously meet.\n" \
            f"There is no way you can run away from him.\n" \
            f"You have to kill him to move ahead.\n" \
            f"Do you want to kill it? (yes/no)"
        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=32, column=2)

        # Entering data into the file
        self.file.write(msg)

        # creating and displaying the Entry to get user input
        self.choice4 = Entry(self.second_frame)
        self.choice4.grid(row=33, column=2)

        # creating and display the button that will call the function fourth_floor_1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.fourth_floor_1)
        button.grid(row=34, column=2)


    def fourth_floor_1(self):
        '''

            This method will check the option entered by the user

        :return: none
        '''

        option=self.choice4.get().lower()  # converting into lower case to avoid casing error

        # using Exception handling
        # It will pop a messagebox if the user has entered wrong input
        try:

            if (option == "yes") or (option == "y"):  # input validation
                msg = f"Great!! you have killed a high level Goblin. \n" \
                    f"You are getting an option to pick either:\n" \
                    f"1. gold key. \n" \
                    f"2. get 2 healing potion (1,000 each).\n" \
                    f"Which one do you choose? (1/2): "
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text=msg)
                msg_label.grid(row=35, column=2)
                self.file.write(f"\n User chose to kill the goblin\n {msg}")

                # image of the options (gold key and health portions)
                # Create the PIL image object
                self.image = Image.open('Images/fourth.JPG')
                # resizing the image
                self.image_re = self.image.resize((200, 300), Image.ANTIALIAS)
                self.image_image = ImageTk.PhotoImage(self.image_re)

                # creating the image Label
                self.image_image_Label = Label(self.second_frame, image=self.image_image)
                # storing a reference to a photo image
                self.image_image_Label.image = self.image_image
                self.image_image_Label.grid(row=36, column=2)

                # creating and displaying the Entry to get user input
                self.choice5 = Entry(self.second_frame)
                self.choice5.grid(row=37, column=2)

                # creating and display the button that will call the function fourth_floor_2
                button = Button(self.second_frame, text="Enter Your Choice", command=self.fourth_floor_2)
                button.grid(row=38, column=2)
            else:
                # Entering data into the file
                self.file.write(f"\n Player entered incorrect input")

                # messagebox will pop to guide the adventurer with message
                messagebox.showinfo("Error", "You have to kill the Hobgoblin to move ahead.")

        except ValueError:
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error", "INVALID INPUTS")


    def fourth_floor_2(self):
        '''

            This method will check the option entered by the user

        :return: none
        '''
        choice=int(self.choice5.get())  # fetching the value from the entry
        self.add_heal_to_menu()  # Calling the function to add new menu item

        # using Exception handling
        # It will pop a messagebox if the user has entered wrong input
        try:
            if choice == 1:
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text= "This Gold key might help you in the future. It is kept in the inventory")
                msg_label.grid(row=39, column=2)
                self.inventory.append("Gold key")  # Adding the item to the list
                self.file.write("\nChoose the Gold Key")
            elif choice == 2:
                msg=f"2 Health potion is added to you backpack.\n" \
                    f"You can access healing potion from the menu at the top of the screen. CLICK on \"HEAL\" ."

                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame,text=msg)
                msg_label.grid(row=40, column=2)
                self.backpack += 2
                self.file.write("\n Choose 2 Healing potion")

            else:
                # Entering data into the file
                self.file.write(f"\n Player entered incorrect input")

                # messagebox will pop to guide the adventurer with message
                messagebox.showinfo("Error", "Error.. Wrong option.\nPlease choose the correct option")

        except ValueError:
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error", "INVALID INPUTS")

        # creating and display the button that will call the function fifth_floor
        self.fifth = Button(self.second_frame, text="Enter Fifth Floor", command=self.fifth_floor, fg="GREEN")
        self.fifth.grid(row=41, column=2)

    def fifth_floor(self):
        """

            This method will enter the next floor and display the objectives of the new floor

        :return:none
        """

        # calling the function to display health,gold and healing portion the player has
        self.get_player_status()
        msg=f"You have made it to the FIFTH FLOOR.\n" \
            f"When you enter the floor you see two doors.\n" \
            f"1.Golden door\n2. Normal door.\n" \
            f"Golden door is unlocked by the golden key.\n" \
            f"If you go through this door you will be able to skip the next floor(6th floor).\n" \
            f"There is no Key required to unlock the normal door.\nThis door will lead you the next floor.\n" \
            f"Which door do you pick? (Golden/Normal):"

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=42, column=2)

        self.file.write(msg)

        # Image of both door
        # Create the PIL image object
        self.door = Image.open('Images/doors.jpeg')
        # resizing the image
        self.door_re = self.door.resize((200, 300), Image.ANTIALIAS)
        self.door_image = ImageTk.PhotoImage(self.door_re)

        # creating the image Label
        self.door_image_Label = Label(self.second_frame, image=self.door_image)
        # storing a reference to a photoimage
        self.door_image_Label.image = self.door_image
        self.door_image_Label.grid(row=43, column=2)

        # creating and displaying the Entry to get user input
        self.choice6 = Entry(self.second_frame)
        self.choice6.grid(row=44, column=2)

        # creating and display the button that will call the function fifth_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.fifth_floor1)
        button.grid(row=45, column=2)

    def fifth_floor1(self):
        '''

            This method will check the option entered by the user

        :return:none
        '''

        option= self.choice6.get().lower()  # converting into lower case to avoid casing error
        if option == 'golden':
            if 'Gold key' in self.inventory:
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text="You can skip the next floor")
                msg_label.grid(row=46, column=2)
                self.inventory.pop()  # To remove the key that has been used.
                self.file.write("Used the gold key to open the golden door")
                self.file.write("Gold key pop from the inventory")
            else:
                msg=f"You don't have a golden key to unlock the door.\n" \
                    f"The normal door is unlocked, enter there to get to the next floor"
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text=msg)
                msg_label.grid(row=47, column=2)

                self.file.write(f"\n {msg}")

        elif option == 'normal':
            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text="The door is unlocked.\n You can enter to move to the next floor.")
            msg_label.grid(row=48, column=2)
            self.file.write("\n user choose normal door")

        else:
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error","Invalid input. Please enter the correct option")

        # creating and display the button that will call the function sixth_floor
        self.sixth = Button(self.second_frame, text="Enter Sixth Floor", command=self.sixth_floor, fg="GREEN")
        self.sixth.grid(row=49, column=2)

    def sixth_floor(self):
        '''

                This method will enter the next floor and display the objectives of the new floor

        :return:none
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()

        msg=f"Congratulations!! You have made it half way through the game.\n" \
            f"The sixth floor is dark and gloomy. The air on the floor smells different. " \
            f"\nIt smells likeee....\n\n" \
            f"You have been ambushed by a Boggart.\n"

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=50, column=2)

        # Entering data into the file
        self.file.write(msg)

        #Image of boggart goblin
        # Create the PIL image object
        self.goblin2 = Image.open('Images/boggart.jpeg')
        # resizing the image
        self.goblin2_re = self.goblin2.resize((200, 300), Image.ANTIALIAS)
        self.goblin2_image = ImageTk.PhotoImage(self.goblin2_re)

        # creating the image Label
        self.goblin2_image_Label = Label(self.second_frame, image=self.goblin2_image)
        # storing a reference to a photoimage
        self.goblin2_image_Label.image = self.goblin2_image
        self.goblin2_image_Label.grid(row=51, column=2)


        msg1 = f"You lost 1000 hit points\n" \
            f"Theses are known for attacking adventurers while they are sleeping\n" \
            f"The air contained sleeping gas, to make adventurers sleep which makes it easier for Boggart to attack\n" \
            f"If you defeat the Boggart, you might get gold as a reward.\n" \
            f"You can choose to run away as Boggarts are territorial.\n" \
            f"He will follow you till the end of the floor. You might loose a lot of health.\n" \
            f"Will you attack him or run away? (attack/run):"
        self.health -= 1000
        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg1)
        msg_label.grid(row=52, column=2)

        # Entering data into the file
        self.file.write(f"\n{msg1}")

        # creating and displaying the Entry to get user input
        self.choice7 = Entry(self.second_frame)
        self.choice7.grid(row=53, column=2)

        # creating and display the button that will call the function sixth_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.sixth_floor1)
        button.grid(row=54, column=2)

    def sixth_floor1(self):
        '''

            This method will check the option entered by the user

        :return:none
        '''

        choice=self.choice7.get().lower()  # converting into lower case to avoid casing error
        if choice == 'attack':
            msg=f"You have defeated the Boggart.\n" \
                f"As a reward you receive 100 Gold\n" \
                f"You lost 1000 Hit Points in the attack"
            self.gold += 100  # Adding 100 gold for the achievement
            self.health -= 1000 # reducing 1000 health for the hit

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=55, column=2)

            # Entering data into the file
            self.file.write(msg)

        elif choice == 'run':
            msg=f"The Boggart attacks you.\n" \
                f"You lost 1000 Hit points\n" \
                f"You are still running.\n" \
                f"You lost 1000 Hit points\n" \
                f"You can see the exit door of the floor. The Boggart hits you one last time.\n" \
                f"You lost 1000 Hit points"

            self.health -= 1000  # reducing 1000 health for the hit 1
            self.health -= 1000  # reducing 1000 health for the hit 2
            self.health -= 1000  # reducing 1000 health for the hit 3

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=56, column=2)

            # Entering data into the file
            self.file.write(msg)

        else:
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error","INVALID input")

        # creating and display the button that will call the function seventh_floor
        self.seventh = Button(self.second_frame, text="Enter Seventh Floor", command=self.seventh_floor, fg="GREEN")
        self.seventh.grid(row=57, column=2)

    def seventh_floor(self):
        '''

                This method will enter the next floor and display the objectives of the new floor

        :return:none
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()

        msg = f"Weclome!!\n" \
            f"The 7th floor is a neutral floor where no one will attack you.\n" \
            f"Take your time and rest.\n" \
            f"As a reward for reaching here.\n" \
            f"You can choose:\n" \
            f"1. 100 gold\n" \
            f"2. 1 Healing portion\n" \
            f"Select your reward (1/2): "

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=58, column=2)

        # Entering data into the file
        self.file.write(msg)

                # Image of the rewards (gold and healing portion)

        # Create the PIL image object
        self.reward = Image.open('Images/rewards.JPG')
        # resizing the image
        self.reward_re = self.reward.resize((200, 300), Image.ANTIALIAS)
        self.reward_image = ImageTk.PhotoImage(self.reward_re)

        # creating the image Label
        self.reward_image_Label = Label(self.second_frame, image=self.reward_image)
        # storing a reference to a photoimage
        self.reward_image_Label.image = self.reward_image
        self.reward_image_Label.grid(row=59, column=2)

        # creating and displaying the Entry to get user input
        self.choice8 = Entry(self.second_frame)
        self.choice8.grid(row=60, column=2)

        # creating and display the button that will call the function seventh_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.seventh_floor1)
        button.grid(row=61, column=2)

    def seventh_floor1(self):
        '''

                This method will check the option entered by the user

        :return:
        '''

        # fetching the value from the entry
        choice = int(self.choice8.get())

        # using Exception handling
        # It will pop a messagebox if the user has entered wrong input
        try:
            if choice == 1:
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text="100 GOLD coins is added")
                msg_label.grid(row=62, column=2)
                self.gold += 100 # adding 100 Gold for the achievement

                # Entering data into the file
                self.file.write("\n Choose 100 gold")

            elif choice == 2:
                msg = f"1 Healing portion is added to your backpack\n " \
                    f"You can access healing potion from the menu at the top of the screen. CLICK on \"HEAL\" ."
                # creating and displaying the Label using grid() on the second _frame
                msg_label = Label(self.second_frame, text=msg)
                msg_label.grid(row=63, column=2)
                self.backpack += 1  #adding the healing portion to the backpack

                # Entering data into the file
                self.file.write("\n Player choose healing portion")

            else:
                # Entering data into the file
                self.file.write(f"\n Player entered incorrect input")

                # messagebox will pop to guide the adventurer with message
                messagebox.showinfo("Error","Please enter the right option.")

        except ValueError:
            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error","INVALID INPUTS")

        # creating and display the button that will call the function eight_floor
        self.eight = Button(self.second_frame, text="Enter Eight Floor", command=self.eight_floor, fg="GREEN")
        self.eight.grid(row=64, column=2)

    def eight_floor(self):
        '''

                This method will enter the next floor and display the objectives of the new floor

        :return: none
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()

        msg = f"The Eight Floor has lights, you can see around.\n" \
            f"You have been walking for a while,but you are unable to spot a goblin.\n" \
            f"There is a small house at the one corner of the floor.\n" \
            f"You decide to scout it in the hope of some rewards.\n" \
            f"Inside the house there is a Hogboon goblin, these are friendly goblin who brings luck to you.\n" \
            f"Will you keep him as a friend or wil you kill him for a reward? (friend/reward): "

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=65, column=2)

        # Entering data into the file
        self.file.write(msg)

        # Image of Hogboon
        # Create the PIL image object
        self.hogboon = Image.open('Images/hogboon.jpeg')
        # resizing the image
        self.hogboon_re = self.hogboon.resize((200, 300), Image.ANTIALIAS)
        self.hogboon_image = ImageTk.PhotoImage(self.hogboon_re)

        # creating the image Label
        self.hogboon_image_Label = Label(self.second_frame, image=self.hogboon_image)
        # storing a reference to a photoimage
        self.hogboon_image_Label.image = self.hogboon_image
        self.hogboon_image_Label.grid(row=66, column=2)

        # creating and displaying the Entry to get user input
        self.choice9 = Entry(self.second_frame)
        self.choice9.grid(row=67, column=2)

        # creating and display the button that will call the function eight_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.eight_floor1)
        button.grid(row=68, column=2)

    def eight_floor1(self):
        '''

            This method will check the option entered by the user

        :return:
        '''

        choice=self.choice9.get().lower() # converting into lower case to avoid casing error

        if choice == 'friend':
            msg = f"Congrats! you found a new companion.\n" \
                f"Hogboon are very friendly goblins, they will assist you in the future battles."
            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=69, column=2)
            self.hogboon=True

            # Entering data into the file
            self.file.write(f'\n Hogboon choosen as a friend.\n {msg}')

        elif choice == 'reward':
            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text="You have received 500 Gold")
            msg_label.grid(row=70, column=2)
            self.gold += 500

            # Entering data into the file
            self.file.write("Player choose 500 gold coin")

        else:
            # Entering data into the file
            self.file.write(f"\n Player entered incorrect input")

            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("Error","You can enter either 'friend' or 'reward' ")

        # creating and display the button that will call the function ninth_floor
        self.ninth = Button(self.second_frame, text="Enter Ninth Floor", command=self.ninth_floor, fg="GREEN")
        self.ninth.grid(row=71, column=2)

    def ninth_floor(self):
        '''

                This method will enter the next floor and display the objectives of the new floor

        :return: None
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()

        msg = f"On the Ninth floor, you find your self in a dark forest.\n" \
            f"There is a footpath which might lead you to the last door.\n" \
            f"You decide to follow it. At a distance you can hear crows crawling.\n" \
            f"Right at the center of the floor you find:\n" \
            f"To the LEFT you see a horde of goblins.\n" \
            f"To the RIGHT you see the goblin king.\n" \
            f"In FORWARD of you there is forest.\n" \
            f"And BEHIND you is the path you came from.\n\n" \
            f"Which path do you choose (Left,Right,forward,Behind): "

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=72, column=2)

        # Entering data into the file
        self.file.write(msg)

        # Image of the options (Horde of goblins,Goblin king,forest,path
        # Create the PIL image object
        self.path1 = Image.open('Images/ninthfloor2.JPG')
        # resizing the image
        self.path1_re = self.path1.resize((300, 300), Image.ANTIALIAS)
        self.path1_image = ImageTk.PhotoImage(self.path1_re)

        # creating the image Label
        self.path1_image_Label = Label(self.second_frame, image=self.path1_image)
        # storing a reference to a photoimage
        self.path1_image_Label.image = self.path1_image
        self.path1_image_Label.grid(row=73, column=2)

        # Create the PIL image object
        self.path2 = Image.open('Images/ninthfloor1.JPG')
        # resizing the image
        self.path2_re = self.path2.resize((300, 300), Image.ANTIALIAS)
        self.path2_image = ImageTk.PhotoImage(self.path2_re)

        # creating the image Label
        self.path2_image_Label = Label(self.second_frame, image=self.path2_image)
        # storing a reference to a photoimage
        self.path2_image_Label.image = self.path2_image
        self.path2_image_Label.grid(row=74, column=2)

        # creating and displaying the Entry to get user input
        self.choice10 = Entry(self.second_frame)
        self.choice10.grid(row=75, column=2)

        # creating and display the button that will call the function ninth_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.ninth_floor1)
        button.grid(row=76, column=2)


    def ninth_floor1(self):
        '''

            This method will check the option entered by the user

        :return:
        '''

        choice = self.choice10.get().lower()

        if choice == 'left':
            msg = f"WOW now you can call your self a Goblin Slayer.\n" \
                f"That was a lot of Goblins to take on at once.\n" \
                f"That result in loss of hit points by 3000.\n" \
                f"As a reward for defeating them you get 3 Healing portion.\n" \
                f"You can access healing potion from the menu at the top of the screen. CLICK on \"HEAL\" ."

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=77, column=2)
            self.backpack += 3  # Adding 3 Healing portion to the backpack
            self.health -= 3000  # Reducing 3000 health for the hit

            # Entering data into the file
            self.file.write(f"\n Picked left\n {msg}")

        elif choice == 'right':

            msg = f"WOW now you can call your self a Goblin Slayer.\n" \
                f"That was one strong Goblin King to take on.\n" \
                f"That result in loss of hit points by 3000.\n" \
                f"As a reward for defeating him you get 3 Healing portion"
            self.backpack += 3  # Adding 3 Healing portion to the backpack
            self.health -= 3000  # Reducing 3000 health for the hit

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=78, column=2)

            # Entering data into the file
            self.file.write(f"\n Picked right\n {msg}")


        elif choice == 'forward':

            msg = f"After moving forward you find two Goblin Kings.\n" \
                f"There is no way to escape them, you will have to fight them.\n " \
                f"That took a lot of time to defeat them.\n" \
                f"You lost 60000 hit points in that process.\n" \
                f"As a reward for defeating them you get 3 Healing portion"
            self.health -= 6000  # Reducing 6000 health for the hit
            self.backpack += 3  # Adding 3 Healing portion to the backpack

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=79, column=2)

            # Entering data into the file
            self.file.write(f"\n Picked forward\n {msg}")

        elif choice == 'behind':

            # Image of 3 goblin kings
            # Create the PIL image object
            self.king = Image.open('Images/three_king.jpeg')
            # resizing the image
            self.king_re = self.king.resize((400, 400), Image.ANTIALIAS)
            self.king_image = ImageTk.PhotoImage(self.king_re)

            # creating the image Label
            self.king_image_Label = Label(self.second_frame, image=self.king_image)
            # storing a reference to a photoimage
            self.king_image_Label.image = self.king_image
            self.king_image_Label.grid(row=80, column=2)


            msg = f"You trace your steps back and find 3 king goblins surrounding you.\n" \
                f"There is no way to escape them, you will have to fight them.\n" \
                f"After fighting them you lose 8000 health.\n" \
                f"As a reward for defeating them you get 3 Healing portion."
            self.health -= 8000  # Reducing 8000 health for the hit
            self.backpack += 3  # Adding 3 Healing portion to the backpack

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=81, column=2)

            # Entering data into the file
            self.file.write(f"\n Picked behind\n {msg}")
        else:
            # Entering data into the file
            self.file.write(f"\n Player entered incorrect input")

            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("ERROR","Please enter the correct path (Left, Right, Front,Behind)")

        # creating and display the button that will call the function tenth_floor
        self.tenth = Button(self.second_frame, text="Enter Tenth Floor", command=self.tenth_floor, fg="GREEN")
        self.tenth.grid(row=82, column=2)

    def tenth_floor(self):
        '''

            This method will enter the next floor and display the objectives of the new floor

        :return:none
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()
        self.dragon = 10000  # Health of the dragon

                # Image of the dragon

        # Create the PIL image object
        self.dragon1 = Image.open('Images/dragon.jpeg')
        # resizing the image
        self.dragon1_re = self.dragon1.resize((400, 400), Image.ANTIALIAS)
        self.dragon1_image = ImageTk.PhotoImage(self.dragon1_re)

        # creating the image Label
        self.dragon1_image_Label = Label(self.second_frame, image=self.dragon1_image)
        # storing a reference to a photoimage
        self.dragon1_image_Label.image = self.dragon1_image
        self.dragon1_image_Label.grid(row=83, column=2)

        msg = f"Welcome to the second last floor of the dungeon.\n" \
            f"There is Treasure on the floor below this.\n" \
            f"As you are going downstairs. A dragon is at the door to welcome you.\n" \
            f"With its first fire breath you loose 1000 health.\n" \
            f"That was so quick you were unable to react.\n" \
            f"The dragon has a health of 10,000.\n" \
            f"Do you want to attack the dragon? (yes/no): "
        self.health -= 1000  # Reducing 1000 health for the hit

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=84, column=2)

        # Entering data into the file
        self.file.write(f"\n {msg}")

        # creating and displaying the Entry to get user input
        self.choice11 = Entry(self.second_frame)
        self.choice11.grid(row=85, column=2)

        # creating and display the button that will call the function tenth_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.tenth_floor1)
        button.grid(row=86, column=2)

    def tenth_floor1(self):
        '''

            This method will check the option entered by the user

        :return:
        '''

        # converting into lower case to avoid casing error
        choice =self.choice11.get().lower()

        if (choice == 'no') or (choice == 'n'):  #input validation
            self.exit_game2()  # calling the method to exit the game

        elif (choice == 'yes') or (choice == 'y'):
            msg=f"You attack him with the little health you have.\n" \
                f"With few attacks you are able to reduce his health by half but in the process you lose all you health.\n" \
                f"Health=0"
            self.dragon /= 2  # Adventurers damage to the dragon
            self.health = 0  # lost life when health =0

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=87, column=2)

            # Entering data into the file
            self.file.write(f"\n Adventurer chooses to attack the dragon\n {msg}")
        else:
            # Entering data into the file
            self.file.write(f"\n Player entered incorrect input")

            # messagebox will pop to guide the adventurer with message
            messagebox.showinfo("ERROR","Please enter the correct option.")

        if self.hogboon == True:
            msg = f"At a distance you can hear the dragon growling. \n" \
                f"Slowly you open your eyes and see your friend besides you.\n" \
                f"He has risked his life to heal you completely.\n" \
                f"Dragon's Hit points:\n\tHealth = {self.dragon}\n" \
                f" Health= 10000" \
                f"You are pissed off for loosing your friend.\n" \
                f"Do you want to take revenge by killing the dragon and avenging you friend? (yes/no)"
            self.health = 10000  # regained all health

            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text=msg)
            msg_label.grid(row=88, column=2)

            # Entering data into the file
            self.file.write(f"\n {msg}")

            # creating and displaying the Entry to get user input
            self.choice12 = Entry(self.second_frame)
            self.choice12.grid(row=89, column=2)

            # creating and display the button that will call the function tenth_floor2
            button = Button(self.second_frame, text="Enter Your Choice", command=self.tenth_floor2)
            button.grid(row=90, column=2)
        else:
            self.exit_game3()  # calling the method to exit the game

    def tenth_floor2(self):
        '''

            This method will check the option entered by the user

        :return:
        '''

        choice=self.choice12.get().lower()  # converting into lower case to avoid casing error

        # input validation
        if (choice == 'yes') or (choice == 'y'):
            # creating and displaying the Label using grid() on the second _frame
            msg_label = Label(self.second_frame, text="In anger you slay the dragon with one attack.")
            msg_label.grid(row=91, column=2)

            # Entering data into the file
            self.file.write(f"\n Player kills the dragon")
        else:
            self.exit_game4()  # calling the method to exit the game

        # creating and display the button that will call the function eleventh_floor
        self.eleventh = Button(self.second_frame, text="Enter Eleventh Floor", command=self.eleventh_floor, fg="GREEN")
        self.eleventh.grid(row=92, column=2)


    def eleventh_floor(self):
        '''

            This method will enter the next floor and display the objectives of the new floor

        :return: none
        '''

        # calling the function to display health, gold and healing portion the player has
        self.get_player_status()

        #Image of the treasure
        # Create the PIL image object
        self.treasure = Image.open('Images/treasure.jpg')
        # resizing the image
        self.treasure_re = self.treasure.resize((400, 400), Image.ANTIALIAS)
        self.treasure_image = ImageTk.PhotoImage(self.treasure_re)

        # creating the image Label
        self.treasure_image_Label = Label(self.second_frame, image=self.treasure_image)
        # storing a reference to a photoimage
        self.treasure_image_Label.image = self.treasure_image
        self.treasure_image_Label.grid(row=93, column=2)

        msg = f"Congratulations!!\n\n" \
            f"You have found the treasure\n" \
            f"You have completed the objective of the game.\n" \
            f"Do you want to exit? (yes/no): "

        # creating and displaying the Label using grid() on the second _frame
        msg_label = Label(self.second_frame, text=msg)
        msg_label.grid(row=94, column=2)

        # Entering data into the file
        self.file.write(f"\n {msg}")

        # creating and displaying the Entry to get user input
        self.choice13 = Entry(self.second_frame)
        self.choice13.grid(row=95, column=2)

        # creating and display the button that will call the function eleventh_floor1
        button = Button(self.second_frame, text="Enter Your Choice", command=self.eleventh_floor1)
        button.grid(row=96, column=2)

    def eleventh_floor1(self):
        '''

            This method will check the option entered by the user

        :return:none
        '''

        # converting into lower case to avoid casing error
        choice=self.choice13.get().lower()
        if (choice == 'yes') or (choice == 'y'):  # input validation
            # Entering data into the file
            self.file.write(f"\n Entered yes to exit")

            # closed the file
            self.file.close()

            quit()  # this function will close the window
        else:
            self.exit_game5()  # calling the method to exit the game


def main():

    # Initializing the window
    root=Tk() # to create the window
    root.title("Goblin Slayer")  # to display the title of the window
    # adding an icon/symbol for the game by using an ico file
    root.iconbitmap("Images/Goblin_Slayer_cover.ico")
    # Set window size
    root.geometry("900x700")

    myapp = App(root)  # creating an object of the Class

    # Start the GUI
    root.mainloop()  # calling the GUI mainloop

if __name__  ==  "__main__":
    main()  # calling the main function
