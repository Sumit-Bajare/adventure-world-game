from TextUI import TextUI
import time
import unittest # importing the inbuilt class for unit testing


class Game():
    def __init__(self,health,gold):

        self.health=health
        self.gold=gold
        self.textUI = TextUI()

    def printWelcome(self):
        """
            Displays a welcome message
            This gives the description of the game.
        :return:
        """
        self.textUI.printtoTextUI("Welcome to the world of Goblins")
        self.textUI.printtoTextUI("You are a Goblin Slayer.")
        self.textUI.printtoTextUI("The main objective of the game is to enter the Dungeon and kill the goblins to claim the treasure.")
        self.textUI.printtoTextUI("The Dungeon consists of 11 floors, the treasure is on the last floor.\nYou will be carrying a backpack to store your Health Portion and the Gold you collect on the way.")
        self.textUI.printtoTextUI("Everytime you get a hit, you will loose some health. If you kill Goblins you will get Gold as a reward")

        wants_to_play = input("Do you want to play? ").lower() #converting the input into lower case to prevent errors. (Error Handeling )

        if (wants_to_play == "yes") or (wants_to_play == "y"):   #input validation
            print("Starting...\n")
            time.sleep(1)  # Adding delays for dramatic effects
            print("Please wait!")
            time.sleep(1)
            count = 0
            while count != 5:
                print(".", end="")      #making it look like the Game is loading
                time.sleep(2 / 5)
                count += 1
        else:
            self.textUI.printtoTextUI("Hope to see you next time Thanks for playing.")
            quit() #this Function will exit the code

        self.textUI.printtoTextUI("\nCurrent Player Stats: \n Health = 10000 \n Gold = 0")
        print("Let's play!\n")
        time.sleep(2)

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['help', 'quit','next floor']

    def processCommand(self):
        """
            Process a command from the TextUI

        :return: none
        """
        play=False
        while play!=True:
            self.textUI.printtoTextUI(f"Your command words are: {self.showCommandWords()}")
            choice  = input("Please Enter your command: ").upper()

            if choice == "HELP":
                self.doPrintHelp()
                play=True
            elif choice == "QUIT":
                quit()
                play=True
            elif choice == "NEXT FLOOR":
                self.get_exit()
                play=True
            else:
                # Unknown command ...
                self.textUI.printtoTextUI("Don't know what you mean")
                self.textUI.printtoTextUI("Please Enter the correct command")


    def doPrintHelp(self):
        """
            Display some useful help text
        :return: None
        """
        self.textUI.printtoTextUI("You are a Goblin Slayer.")
        self.textUI.printtoTextUI("The main objective of the game is to enter the Dungeon and kill the goblins to claim the treasure. ")
        self.textUI.printtoTextUI("The Dungeon consists of 11 floors, the treasure is on the last floor. \nYou will be carrying a backpack to store your Health Portion and the Gold you collect on the way.")
        self.textUI.printtoTextUI("Everytime you get a hit, you will loose some health. If you kill Goblins you will get Gold as a reward.")

        self.processCommand()

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''
        # this while loop will repeat till we get the answer we need from the user
        play =False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):   #input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                play=True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")



class First_floor:
    def __init__(self,health,gold):
        '''

            Constructor method

        :param health: To track the health of the adventurer
        :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python


    def get_description(self):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :return:weapon
        '''

        self.textUI.printtoTextUI("This is the First Floor of the Dungeon.")
        self.textUI.printtoTextUI("On this floor all the adventures get to pick up a weapon to fight with the goblins.")
        self.textUI.printtoTextUI("You have a sword on the right and Magic Staff on the left.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:
            weapon = input("Which one will you choose (Sword/Magic staff): ").lower() # converting into lower case to avoid casing error
            if (weapon=='sword') or (weapon=='magic staff'):
                play=True
                self.textUI.printtoTextUI(f"Congratulations Adventurer on picking up the right weapon for you. \nThis {weapon.upper()} will help you kill the Goblins you encountered")
            else:
                self.textUI.printtoTextUI("Please pick the correct weapon")

        return weapon



    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack =backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portions = {self.backpack}")




class Second_floor:
    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python


    def get_description(self,weapon,gold):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param weapon: Weapon chosen by the adventurer
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :return: The increase in the Gold
        '''

        self.weapon = weapon
        self.textUI.printtoTextUI("Welcome! to the second floor.")
        time.sleep(1)
        self.textUI.printtoTextUI(f"It is very dark on this floor, so keep your guard up with {self.weapon} in hand.")
        self.textUI.printtoTextUI("Goblins are know to attack in the dark. While walking to encounter a low level goblin.")
        self.textUI.printtoTextUI("These creatures are devious, mischievous and pure creatures.\n")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:
            choice = input("Will you kill it or run from it? (kill/run)").lower()
            if (choice=='kill') or (choice=='run'): #input validation
                if (choice=='kill'):
                    self.textUI.printtoTextUI(f"Since it was a low level Goblin you could easy kill it with your {self.weapon}. \nHence no health loss. \nAs a reward you recieve 10 GOLD coins")
                    self.gold+=10
                    return 1
                    play=True
                else:
                    self.textUI.printtoTextUI(f"WOW!! you can run fast, but everytime you won't be this lucky.")
                    play=True
            else:
                self.textUI.printtoTextUI("ERROR....Please enter the right choice.")


    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")

    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack=backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")




class Third_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python


    def get_description(self,health,gold):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param health: To track the health of the adventurer
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :return: gold,health reduced
        '''

        self.textUI.printtoTextUI(f"The THIRD FLOOR is not dark, there are lights on this floor. \nBut the floor is full with water which contains Sharks.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:
            self.textUI.printtoTextUI("You have three options: \n\t 1. You can choose to buy a boat from the inventory which will cost 5 gold.\n\t 2.you can swim in the water where you can losse 1000 hit points as the sharks will bite you.\n\t 3.Go back to the second floor")
            choice = int(input("What do you choose (1/2/3): "))
            if choice==1:
                if self.gold>=5:
                    self.textUI.printtoTextUI("The boat has arrived.")
                    self.textUI.printtoTextUI("It will take a few minutes to cross the water.")
                    time.sleep(2)
                    self.gold-=5
                    return 2
                    play=True

                else:
                    self.textUI.printtoTextUI("You don't have enough Gold to buy a boat. Reconsider your options")
            elif choice==2:
                self.textUI.printtoTextUI("You have crossed the water. That was a long swim. \nTake a deep breath and relax your self.")
                self.health-=1000
                play=True
                return 1
            else:
                # retracing back to the second floor
                second_floor = Second_floor(health, gold)
                gold = second_floor.get_description(weapon, gold)
                second_floor.get_player_stats(health, gold,backpack)
                second_floor.get_exit()


    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user

        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")



class Fourth_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self,health,gold,inventory,backpack):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param health: To track the health of the adventurer
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param inventory: Used to store the gold keys
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.inventory=inventory
        self.backpack = backpack
        self.textUI.printtoTextUI("At the entrance of the fourth floor there is a Hobgoblin waiting for you.")
        self.textUI.printtoTextUI("This Hobgoblin is at a higher level than the goblin you previously meet. There is no way you can run away from him.")
        self.textUI.printtoTextUI("You have to kill him to move ahead.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play != True:
             option = input("Do you want to kill it?")
             if (option == "yes") or (option == "y"):  # input validation
                self.textUI.printtoTextUI("Great!! you have killed a high level Goblin. \nYou are getting an option to pick either:\n\t1. gold key. \n\t2. get 2 health portion (1,000 each).")
                choice = int(input("Which one do you choose? (1/2): "))
                if choice==1:
                    self.textUI.printtoTextUI("This Gold key might help you in the future. It is kept in the inventory")
                    self.inventory.append("Gold key")
                    play = True
                elif choice==2:
                    self.textUI.printtoTextUI("2 Health portion is added to you backpack")
                    self.backpack+=2
                    play = True
                else:
                    self.textUI.printtoTextUI("Error.. Wrong option. Please choose the correct option")

             else:
                self.textUI.printtoTextUI("You have to kill the Hobgoblin to move ahead.")
        return (self.inventory,self.backpack)


    def use_healing_portion(self,backpack):
        '''

            This method is used to heal the player

        :param backpack:
        :return: decreasing healing portion
        '''

        self.backpack=backpack
        if backpack!=0:
            self.textUI.printtoTextUI(f"\n\nYou have {self.backpack} Healing portions")
            self.textUI.printtoTextUI("You can only use 1 Healing portion at a time.")
            choice =input("Do you want to use the Healing Portion? ")
            if (choice =='yes') or (choice=='y'): #input validation

                self.backpack-=1
                self.textUI.printtoTextUI("You have used your Healing portion")
                return 1


    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")



class Fifth_floor():
    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI=TextUI() #Text-based UI builder for Python

    def get_description(self,inventory):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param inventory: Used to store the gold keys
        :return: Boolean, if the user want to skip a floor
        '''

        self.inventory=inventory

        self.textUI.printtoTextUI("You have made it to the FIFTH FLOOR")
        self.textUI.printtoTextUI("When you enter the floor you see two doors.")
        self.textUI.printtoTextUI("1.Golden door\n2. Normal door")
        self.textUI.printtoTextUI("Golden door is unlocked by the golden key.\nIf you go through this door you will be able to skip the next floor(6th floor).")
        self.textUI.printtoTextUI("There is no Key required to unlock the normal door.\nThis door will lead you the next floor.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:

            option = input("Which door do you pick? (Golden/Normal) ").lower() # converting into lower case to avoid casing error
            if option=='golden':
                if ('Gold key' in inventory):
                    self.textUI.printtoTextUI("You can skip the next floor")
                    self.inventory.pop() # To remove the key that has been used.
                    play=True
                    return True
                else:
                    self.textUI.printtoTextUI("You don't have a golden key to unlock the door.")
                    self.textUI.printtoTextUI("The normal door is unlocked, enter there to get to the next floor")
                    play =True
            elif option=='normal':
                self.textUI.printtoTextUI("The door is unlocked. You can enter to move to the next floor.")
                play=True
            else:
                self.textUI.printtoTextUI("Invalid input. Please enter the correct option")


    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")



class Sixth_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self,health,gold):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param health: To track the health of the adventurer
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :return: health loss and gold won
        '''

        self.textUI.printtoTextUI("Congratulations!! You have made it half way through the game.")
        time.sleep(2)
        self.textUI.printtoTextUI("The sixth floor is dark and gloomy. The air on the floor smells different. \nIt smells likeee....")
        time.sleep(3)
        self.textUI.printtoTextUI("You have been ambushed by a Boggart.")
        self.textUI.printtoTextUI("You lost 1000 hit points")
        self.health-=1000
        self.textUI.printtoTextUI("Theses are known for attacking adventurers while they are sleeping")
        self.textUI.printtoTextUI("The air contained sleeping gas, to make adventurers sleep which makes it easier for Boggart to attack")
        self.textUI.printtoTextUI("If you defeat the Boggart, you might get gold as a reward.")
        self.textUI.printtoTextUI("You can choose to run away as Boggarts are territorial.")
        self.textUI.printtoTextUI("He will follow you till the end of the floor. You might loose a lot of health.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play != True:
            choice= input("Will you attack him or run away? (attack/run)").lower() # converting into lower case to avoid casing error
            if choice =='attack':
                time.sleep(1)
                self.textUI.printtoTextUI("You have defeated the Boggart.")
                self.textUI.printtoTextUI("As a reward you receive 100 Gold")
                self.gold+=100
                self.textUI.printtoTextUI("You lost 1000 Hit Points in the attack")
                self.health-=1000
                play=True
                return 1
            elif choice=='run':
                self.textUI.printtoTextUI("The Boggart attacks you.")
                self.textUI.printtoTextUI("You lost 1000 Hit points")
                self.health-=1000
                self.textUI.printtoTextUI("You are still running.")
                self.textUI.printtoTextUI("You lost 1000 Hit points")
                self.health -= 1000
                self.textUI.printtoTextUI("You can see the exit door of the floor. The Boggart hits you one last time.")
                self.textUI.printtoTextUI("You lost 1000 Hit points")
                self.health -= 1000
                play = True
                return 2
            else:
                self.textUI.printtoTextUI("INVALID input")

    def use_healing_portion(self, backpack):
        '''

            This method is used to heal the player

        :param backpack:
        :return: decreasing healing portion
        '''

        self.backpack = backpack
        if backpack != 0:
            self.textUI.printtoTextUI(f"\n\nYou have {self.backpack} Healing portions")
            self.textUI.printtoTextUI("You can only use 1 Healing portion at a time.")
            choice = input("Do you want to use the Healing Portion? ")
            if (choice == 'yes') or (choice == 'y'): #input validation
                self.backpack -= 1
                self.textUI.printtoTextUI("You have used your Healing portion")
                return 1

    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")




class Seventh_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self,gold,backpack):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: Gold and health portion added
        '''

        self.backpack=backpack
        self.textUI.printtoTextUI("Weclome!!")
        self.textUI.printtoTextUI("The 7th floor is a neutral floor where no one will attack you.")
        self.textUI.printtoTextUI("Take your time and rest")
        self.textUI.printtoTextUI("As a reward for reaching here.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:
            self.textUI.printtoTextUI("You can choose:\n\t1. 100 gold\n\t2. 1 Healing portion")
            choice = int(input("Select your reward (1/2)"))
            if choice==1:
                self.textUI.printtoTextUI("100 GOLD coins is added")
                self.gold+=100
                play=True
                return 1
            elif choice==2:
                self.textUI.printtoTextUI("1 Healing portion is added to your backpack")
                self.backpack+=1
                play=True
                return 2
            else:
                self.textUI.printtoTextUI("Please enter the right option.")

    def use_healing_portion(self, backpack):
        '''

            This method is used to heal the player

        :param backpack:
        :return: decreasing healing portion
        '''

        self.backpack = backpack
        if backpack != 0:
            self.textUI.printtoTextUI(f"\n\nYou have {self.backpack} Healing portions")
            self.textUI.printtoTextUI("You can only use 1 Healing portion at a time.")
            choice = input("Do you want to use the Healing Portion? ")
            if (choice == 'yes') or (choice == 'y'): #input validation
                self.backpack -= 1
                self.textUI.printtoTextUI("You have used your Healing portion")
                return 1

    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")

class Eight_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self,gold):
        '''

            This method will fetch the description of the floor and the objective of the floor

        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :return: Boolean, if the adventurer has accepted the friend
        '''

        self.textUI.printtoTextUI("The Eight Floor has lights, you can see around.")
        time.sleep(1)
        self.textUI.printtoTextUI("You have been walking for a while,but you are unable to spot a goblin.")
        self.textUI.printtoTextUI("There is a small house at the one corner of the floor.")
        self.textUI.printtoTextUI("You decide to scout it in the hope of some rewards.")
        self.textUI.printtoTextUI("Inside the house there is a Hogboon goblin, these are friendly goblin who brings luck to you.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:
            choice = input("Will you keep him as a friend or wil you kill him for a reward? (friend/reward)").lower() # converting into lower case to avoid casing error
            if choice =='friend':
                self.textUI.printtoTextUI("Congrats! you found a new companion.")
                self.textUI.printtoTextUI("Hogboon are very friendly goblins, they will assist you in the future battles.")
                play= True
                return True
            elif choice=='reward':
                self.textUI.printtoTextUI("You have received 500 Gold")
                self.gold+=500
                play =False
                return False
            else:
                self.textUI.printtoTextUI("You can enter either 'friend' or 'reward' ")

    def use_healing_portion(self, backpack):
        '''

            This method is used to heal the player

        :param backpack:
        :return: decreasing healing portion
        '''

        self.backpack = backpack
        if backpack != 0:
            self.textUI.printtoTextUI(f"\n\nYou have {self.backpack} Healing portions")
            self.textUI.printtoTextUI("You can only use 1 Healing portion at a time.")
            choice = input("Do you want to use the Healing Portion? ")
            if (choice == 'yes') or (choice == 'y'): #input validation
                self.backpack -= 1
                self.textUI.printtoTextUI("You have used your Healing portion")
                return 1

    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")




class Ninth_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self,backpack):
        '''

            This method well get the description of the floor and the objective of thr floor

        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: It will return the hit points lost by the adventurer
        '''

        self.backpack=backpack
        self.textUI.printtoTextUI("On the Ninth floor, you find your self in a dark forest.")
        self.textUI.printtoTextUI("There is a footpath which might lead you to the last door.")
        self.textUI.printtoTextUI("You decide to follow it. At a distance you can hear crows crawling.")
        self.textUI.printtoTextUI("Right at the center of the floor you find:")
        play = False
        while play!= True:
            self.textUI.printtoTextUI("To the LEFT you see a horde of goblins.")
            self.textUI.printtoTextUI("To the RIGHT you see the goblin king.")
            self.textUI.printtoTextUI("In FRONT of you there is forest.")
            self.textUI.printtoTextUI("And BEHIND you is the path you came from.")
            choice = input("Which path do you choose (Left,Right,front,Behind): ").lower() # converting into lower case to avoid casing error
            if choice == 'left':
                time.sleep(2)
                self.textUI.printtoTextUI("WOW now you can call your self a Goblin Slayer.")
                self.textUI.printtoTextUI("That was a lot of Goblins to take on at once.")
                self.textUI.printtoTextUI("That result in loss of hit points by 3000")
                self.health-=3000
                self.textUI.printtoTextUI("As a reward for defeating them you get 3 Healing portion")
                self.backpack+=3
                play=True
                return 1

            elif choice == 'right':
                time.sleep(2)
                self.textUI.printtoTextUI("WOW now you can call your self a Goblin Slayer.")
                self.textUI.printtoTextUI("That was one strong Goblin King to take on.")
                self.textUI.printtoTextUI("That result in loss of hit points by 3000")
                self.health-=3000
                self.textUI.printtoTextUI("As a reward for defeating him you get 3 Healing portion")
                self.backpack += 3
                play=True
                return 1

            elif choice == 'front':
                time.sleep(2)
                self.textUI.printtoTextUI("After moving forward you find two Goblin Kings.")
                self.textUI.printtoTextUI("There is no way to escape them, you will have to fight them.")
                time.sleep(3)
                self.textUI.printtoTextUI("That took a lot of time to defeat them.")
                self.textUI.printtoTextUI("You lost 60000 hit points in that process")
                self.health-=6000
                self.textUI.printtoTextUI("As a reward for defeating them you get 3 Healing portion")
                self.backpack += 3
                play=True
                return 2

            elif choice == 'behind':
                self.textUI.printtoTextUI("You trace your steps back and find 3 king goblins surrounding you.")
                self.textUI.printtoTextUI("There is no way to escape them, you will have to fight them.")
                self.textUI.printtoTextUI("After fighting them you lose 8000 health")
                self.health-=8000
                self.textUI.printtoTextUI("As a reward for defeating them you get 3 Healing portion")
                self.backpack += 3
                play=True
                return 3
            else:
                self.textUI.printtoTextUI("Please enter the correct path (Left, Right, Front,Behind)")

    def use_healing_portion(self, backpack):
        '''

            This method is used to heal the player

        :param backpack:
        :return: decreasing healing portion
        '''

        self.backpack = backpack
        if backpack != 0:
            self.textUI.printtoTextUI(f"\n\nYou have {self.backpack} Healing portions")
            self.textUI.printtoTextUI("You can only use 1 Healing portion at a time.")
            choice = input("Do you want to use the Healing Portion? ")
            if (choice == 'yes') or (choice == 'y'):  #input validation
                self.backpack -= 1
                self.textUI.printtoTextUI("You have used your Healing portion")
                return 1

    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

                    The exit method is used to exit the current floor

                :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
            if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                self.textUI.printtoTextUI("Initializing...")
                time.sleep(1)
                self.textUI.printtoTextUI("Entering the next floor")
                time.sleep(2)
                play = True
            else:
                self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")




class Tenth_floor():

    def __init__(self,health,gold):
        '''

                Constructor method

            :param health: To track the health of the adventurer
            :param gold: To keep count on the gold the adventurer is carrying
        '''

        self.health=health
        self.gold=gold
        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self,health,gold,hagboon):
        '''

            This method well get the description of the floor and the objective of thr floor

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param hogboon: This is Boolean, it will inform if that adventurer has a Companion or not.
        :return:
        '''
        self.hagboon=hagboon
        self.dragon=10000
        self.textUI.printtoTextUI("Welcome to the second last floor of the dungeon.")
        self.textUI.printtoTextUI("There is Treasure on the floor below this.")
        self.textUI.printtoTextUI("As you are going downstairs. A dragon is at the door to welcome you.")
        self.textUI.printtoTextUI("With its first fire breath you loose 1000 health.")
        self.health-=1000
        self.textUI.printtoTextUI("That was so quick you were unable to react.")
        self.textUI.printtoTextUI("The dragon has a health of 10,000.")

        # this while loop will repeat till we get the answer we need from the user
        play=False
        while play!=True:

            choice = input("Do you want to attack the dragon? (yes/no)").lower() # converting into lower case to avoid casing error
            if (choice =='yes') or (choice =='y'):
                self.textUI.printtoTextUI("You attack him with the little health you have.")
                self.textUI.printtoTextUI("With few attacks you are able to reduce his health by half but in the process you lose all you health.")
                self.dragon /=2
                self.health=0
                time.sleep(5)
                play=True
            elif (choice=='no') or (choice=='n'):  #input validation
                self.textUI.printtoTextUI("The dragon has killed you.")
                self.health =0
                self.textUI.printtoTextUI("If you had Hagboon as friend he would have helped you in the battle.")
                self.textUI.printtoTextUI("You have lost the game.")
                self.textUI.printtoTextUI("Thanks for playing!")
                quit()
                play=True
            else:
                self.textUI.printtoTextUI("Please enter the correct option.")

        if hagboon==True:

            self.textUI.printtoTextUI("At a distance you can hear the dragon growling. Slowly you open your eyes and see your friend besides you.")
            self.textUI.printtoTextUI("He has risked his life to heal you completely.")
            self.health =10000

            self.textUI.printtoTextUI(f"Dragon's Hit points:\n\t Health = {self.dragon}")
            self.textUI.printtoTextUI("You are pissed off for loosing your friend.")
            choice = input("Do you want to take revenge by killing the dragon and avenging you friend?")
            if (choice=='yes') or (choice=='y'):  #input validation
                self.textUI.printtoTextUI("In anger you slay the dragon with one attack.")
        else:
            self.textUI.printtoTextUI("If you had Hagboon as friend he would have helped you in the battle.")
            self.textUI.printtoTextUI("You have lost the game.")
            self.textUI.printtoTextUI("Thanks for playing!")

    def get_player_stats(self,health,gold,backpack):
        '''

            This method id used to display the players status.

        :param health: This parameter is used to track the health of the player
        :param gold: This parameter is used to count the number of gold the adventurer is carrying
        :param backpack: This parameter keeps count of the healing portion collected by the adventurer
        :return: none
        '''

        self.backpack = backpack
        self.textUI.printtoTextUI(f"Player Status: \n\tHealth = {self.health} \n\tGold = {self.gold} \n\tHealing Portion = {self.backpack}")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        # this while loop will repeat till we get the answer we need from the user
        play = False
        while play != True:
            if self.health==0:
                quit()
            else:

                wants_to_play = input("Do you want to move ahead to the next floor?").lower() # converting into lower case to avoid casing error
                if (wants_to_play == "yes") or (wants_to_play == "y"):  # input validation
                    self.textUI.printtoTextUI("Initializing...")
                    time.sleep(1)
                    self.textUI.printtoTextUI("Entering the next floor")
                    time.sleep(2)
                    play = True
                else:
                    self.textUI.printtoTextUI("The Objective of this floor has be completed, you cannot head back.")




class Eleventh_floor():

    def __init__(self):
        '''

            Constructor Method

        '''

        self.textUI = TextUI() #Text-based UI builder for Python

    def get_description(self):
        '''

            This method well get the description of the floor and the objective of thr floor

        :return: none
        '''

        self.textUI.printtoTextUI("Congratulations!!")
        self.textUI.printtoTextUI("You have found the treasure")

    def get_exit(self):
        '''

            The exit method is used to exit the current floor

        :return: none
        '''

        self.textUI.printtoTextUI("You have completed the objective of the game")
        # this while loop will repeat till we get the answer we need from the user

        play=False
        while play!=True:

            choice = input("Do you want to exit?").lower() # converting into lower case to avoid casing error
            if (choice=='yes') or (choice=='y'): #input validation
                quit()
            else:
                self.textUI.printtoTextUI("You have completed the objective of the game.")
                self.textUI.printtoTextUI("Enjoy the rewards.")


def main():

    health= 10000  # The initial hit points of the player
    gold=0 # The initial  gold the player has.
    inventory=[] # to store keys
    backpack=0 # to store health portions. #used int so that i have a count on the number of health portions
    hagboon=False # Hagboon is a friend. If the player accepts it, It will change to True.


    # Creating the Object of Game Class
    # And calling the methods through the object
    game= Game(health,gold)
    game.printWelcome()
    game.processCommand()

    # Creating the Object of First_floor Class
    # And calling the methods through the object
    first_floor = First_floor(health,gold)
    weapon = first_floor.get_description()
    first_floor.get_player_stats(health,gold,backpack)
    game.processCommand()



    # Creating the Object of Second_floor Class
    # And calling the methods through the object
    second_floor=Second_floor(health,gold)
    gold1 = second_floor.get_description(weapon,gold)
    if gold1==1:
        gold+=10 #reward for killing the Goblin
    second_floor.get_player_stats(health,gold,backpack)
    game.processCommand()



    # Creating the Object of Third_floor Class
    # And calling the methods through the object
    third_floor=Third_floor(health,gold)
    answer  = third_floor.get_description(health,gold)
    if answer==1:
        health-=1000 #for swimming through the water
    else:
        gold-=5 # for buying the boat
    third_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # Creating the Object of Fourth_floor Class
    # And calling the methods through the object
    fourth_floor=Fourth_floor(health,gold)
    inventory,backpack=fourth_floor.get_description(health,gold,inventory,backpack)
    no = fourth_floor.use_healing_portion(backpack)
    if no==1:
        backpack-=1
        health+=1000
    fourth_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # Creating the Object of Fifth_floor Class
    # And calling the methods through the object
    fifth_floor=Fifth_floor(health,gold)
    skip_floor = fifth_floor.get_description(inventory)
    fifth_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # if the Player has not taken the golden key and choose to go through the normal door
    # they will have to visit this floor
    if skip_floor != True:

        # Creating the Object of Sixth_floor Class
        # And calling the methods through the object
        sixth_floor=Sixth_floor(health,gold)
        health -= 1000  # getting hit in the sleep
        outcome = sixth_floor.get_description(health,gold)

        if outcome==1:
            health-=1000 #attacking the goblin
            gold+=100 #reward for defeating the Goblin
        else:
            health-=3000 #For running away from the goblin

        number = sixth_floor.use_healing_portion(backpack)
        if number == 1:
            backpack -= 1
            health += 1000

        sixth_floor.get_player_stats(health,gold,backpack)
        game.processCommand()


    # If the player has chosen the golden key and decided to go through the golden door
    # They would directly land on this floor
    # else they would have to travel from the 5th to the 6th floor and then the 7th floor

    # Creating the Object of Seventh_floor Class
    # And calling the methods through the object
    seventh_floor=Seventh_floor(health,gold)
    reward = seventh_floor.get_description(gold,backpack)
    if reward==1:
        gold+=100
    else:
        backpack+=1
        health += 1000

    no1 = seventh_floor.use_healing_portion(backpack)
    if no1==1:
        backpack-=1
        health += 1000

    seventh_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # Creating the Object of Eight_floor Class
    # And calling the methods through the object
    eight_floor=Eight_floor(health,gold)
    hagboon = eight_floor.get_description(gold)
    no2 = eight_floor.use_healing_portion(backpack)
    if no2==1:
        backpack-=1
        health += 1000
    eight_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # Creating the Object of Ninth_floor Class
    # And calling the methods through the object
    ninth_floor=Ninth_floor(health,gold)
    answer = ninth_floor.get_description(backpack)
    backpack+=3
    if answer==1:
        health -=3000
    elif answer==2:
        health-=6000
    else:
        health-=8000
    no3 = ninth_floor.use_healing_portion(backpack)
    if no3==1:
        backpack-=1
        health += 1000
    ninth_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # Creating the Object of Tenth_floor Class
    # And calling the methods through the object
    tenth_floor = Tenth_floor(health,gold)
    tenth_floor.get_description(health,gold,hagboon)
    tenth_floor.get_player_stats(health,gold,backpack)
    game.processCommand()


    # Creating the Object of Eleventh_floor Class
    # And calling the methods through the object
    eleventh_floor= Eleventh_floor()
    eleventh_floor.get_description()
    eleventh_floor.get_exit()

if __name__ == "__main__":
    main()
