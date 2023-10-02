#Submission by: Purvesh Mehta
#Candidate Number: 260867



import tkinter as tk
from Game import Game
from tkinter import *
import logging
import time
import sys


class App():

    try:
    # Creates a Frame for the application and populates the GUI...
        def __init__(self):
            logging.basicConfig(filename="Player_Journey.log",filemode='w',level=logging.INFO)
            self.name_var = ""
            self.player_name =  None
            self.win=tk.Tk()
            self.win.geometry("500x250")
            self.win.configure(bg='gray25')
            self.win.title("Treasure Game")
            self.win.resizable(False, False)
            self.name_var=tk.StringVar()
            self.choose_item =tk.StringVar()
            self.item = None
            self.game = None
            self.player_bag={}
            self.player_bag_weight = 0
            
            label = tk.Label(self.win, text = 'Welcome to the Adventure Game!', font=('calibre',18, 'bold'),fg='white',bg='gray25')
            name_label = tk.Label(self.win, text = 'Enter Player Name', font=('calibre',10, 'bold'),fg='white',bg='gray25')

            name_entry = tk.Entry(self.win,textvariable = self.name_var,width=20, font=('calibre',10,'normal'))

            sub_btn=tk.Button(self.win,text = 'Play',bg='forest green',fg='white',font=('calibre',14, 'bold'),command = self.submit)

            label.pack()
            name_label.pack()
            name_entry.pack()
            sub_btn.pack(padx=(0, 0),pady=(20, 0))
            
    except ValueError as e:
            print(e)
            
           
    def submit(self):
        """ A initial window to ask players name.
            Loggig details


        """
        self.player_name=self.name_var.get()
        logging.info("Player Name:"+self.player_name)
        self.win.destroy()
        self.game = Game(self.player_name)
        self.build_GUI()
  
        
       

    def item_management(self):
        """ Manages all items in room with their 
        weight limit set.

        """
        self.game.item_remove(self.item)
        if self.item=='keys':
            self.player_bag[self.item] = 5
        if self.item=='knife':
            self.player_bag[self.item] = 1
        if self.item=='money':
            self.player_bag[self.item] = 20
        if self.item=='diamonds':
            self.player_bag[self.item] = 15
        if self.item=='towel':
            self.player_bag[self.item] = 4
        if self.item=='jewels':
            self.player_bag[self.item] = 18
        if self.item=='apple':
            self.player_bag[self.item] = 2
        if self.item=='mobile':
           self.player_bag[self.item] = 3
        if self.item=='gold':
            self.player_bag[self.item] = 30
        if 'diamonds' in self.player_bag.keys() and 'money' in self.player_bag.keys():
            self.winning_status.configure(text="You are Winning!!!")
            
        self.player_bag_weight = sum(self.player_bag.values())
        self.btn_itempic.place_forget()
        self.player_bag_label.configure(text="Player Bag:"+str(self.player_bag_weight)+"kg")
        self.bag_items =list(self.player_bag.keys())
        self.player_bag_status.configure(text=self.player_bag)
        
    def changed(self,event):
        """ A player backpack displaying items 
            player picked during the game
        param event: manages the items, removing them
        return: None

        """
        removed_item = self.choose_item.get()
        self.player_bag.pop(removed_item)
        self.player_bag_weight = sum(self.player_bag.values())
        self.player_bag_label.configure(text="Player Bag:"+str(self.player_bag_weight)+"kg")
        self.player_bag_status.configure(text=self.player_bag)
        self.game.item_add(self.item)
        self.drop.place_forget()
                        
    def remove_items(self):
        """A click to remove items present in 
        player backpack
        """
        self.choose_item.set("Choose Item for remove")
        self.bag_items =list(self.player_bag.keys())
        self.drop = OptionMenu(self.root , self.choose_item , *self.bag_items,command=self.changed)
        self.drop.place(x=520,y=470)
        
    def build_GUI(self):
        self.root = tk.Tk()                           # Create a window
        self.root.title("Adventure World with GUI")   # Set window title
        window_width = 700
        window_height = 600

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')     # Set window size
        self.root.resizable(False, False)

        self.frame1 = tk.Frame(self.root, width=500, height=275, bg='WHITE', borderwidth=2)
        self.frame1.pack_propagate(0)  # Prevents resizing
        self.frame2 = tk.Frame(self.root, width=500, height=275, bg='LIGHT GREY', borderwidth=2)
        self.frame2.grid_propagate(0)  # Prevents resizing
        # This packs both frames into the root window...
        self.frame1.pack()
        self.frame2.pack()
        

        self.text_area1 = tk.Label(self.frame1, text='' )
        self.text_area1.pack()
        self.outside_home = PhotoImage(file='imagesGUI/outside.png')
        self.outside_home = self.outside_home.subsample(2, 2)
        self.room = Label(self.frame1, image = self.outside_home)
        self.room.pack()
        
        self.btn_itempic = Button(self.frame1,command=self.item_management)
        self.btn_itempic.place(x=390,y=30)
        
        self.cmd_area = tk.Entry(self.frame2, text='')
        self.cmd_area.pack()
        #self.build_GUI()
        self.player_bag_label = Label(self.root,font=('calibre',12,'bold'),fg='green',text="Player Bag:"+str(self.player_bag_weight)+"kg")
        self.player_bag_label.place(x=100,y=420)
        self.player_bag_status = Label(self.root,font=('calibre',10,'bold'))
        self.player_bag_status.place(x=200,y=460)

        self.remove_item = Button(self.root,fg="white",bg="red",text="Remove Item from Bag",command=self.remove_items)
        self.remove_item.place(x=520,y=420)

        self.winning_status = Label(self.root,font=('calibre',20,'bold'),fg="green")
        self.winning_status.place(x=400,y=550)
        
        

        self.cmd_button = tk.Button(self.frame2, text='Run command',
                                    fg='black', bg='blue',
                                    command=self.do_command)
        self.cmd_button.pack()
        self.goSouth = tk.Button(self.frame2, text='Go South',
                                    fg='black', bg='red',
                                    command=self.processSouth)
        self.goNorth = tk.Button(self.frame2, text='Go North',
                                 fg='black', bg='green',
                                 command=self.processNorth)
        self.goEast = tk.Button(self.frame2, text='Go East',
                                 fg='black', bg='pink',
                                 command=self.processEast)
        self.goWest = tk.Button(self.frame2, text='Go West',
                                 fg='black', bg='orange',
                                 command=self.processWest)
        self.quit = tk.Button(self.frame2, text='Quit',
                                 fg='white', bg='Red',
                                 command=self.quit)
       

        self.goSouth.pack()
        self.goNorth.pack()
        self.goEast.pack()
        self.goWest.pack()
        self.quit.pack()
        # self.getItem.pack()
      
        self.text_area1.configure(text=self.game.print_welcome())
        self.root.mainloop()


    def quit(self):
        """
        Game stops and exits the window
        """
        print("Thanx for playing")
        self.root.destroy()
        
    def processSouth(self):
        """
        Performs log of users journey, places 
        required images in frame 1 as per 
        players location

        """
        logging.info("In South")
        x = self.game.do_go_command('south')
        
        self.text_area1.configure(text=x)
        if 'in the lobby' in x:
            logging.info("in the lobby")
            self.item='keys'
            self.room_pic = PhotoImage(file='imagesGUI/lobby.png')
            self.room_pic = self.room_pic.subsample(2, 2)
            self.room.configure(image=self.room_pic)
            if 'keys' in x:
                self.item_pic = PhotoImage(file='imagesGUI/lobby_item_keys.png')
                self.item_pic = self.item_pic.subsample(11,9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
                
            
        elif 'in the Room 404' in x:
            logging.info("in the room 404")
            self.item='knife'
            self.room_pic = PhotoImage(file='imagesGUI/Room-404.png')
            self.room.configure(image=self.room_pic)
            if 'knife' in x:
                self.item_pic = PhotoImage(file='imagesGUI/room_404_item_knife.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Red Room' in x:
            logging.info("in the red room")
            self.item='money'
            self.room_pic = PhotoImage(file='imagesGUI/red_room.png')
            self.room.configure(image=self.room_pic)
            if 'money' in x:
                self.item_pic = PhotoImage(file='imagesGUI/red_room_item_money.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Luxury Room' in x:
            logging.info("in the luxury room")
            self.item='jewels'
            self.room_pic = PhotoImage(file='imagesGUI/luxury_room.png')
            self.room.configure(image=self.room_pic)
            if 'jewels' in x:
                self.item_pic = PhotoImage(file='imagesGUI/luxury_room_item_jewels.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Hidden Temple' in x:
            logging.info("in the hidden temple")
            self.item='diamonds'
            self.room_pic = PhotoImage(file='imagesGUI/hidden_temple.png')
            self.room.configure(image=self.room_pic)
            if 'diamonds' in x:
                self.item_pic = PhotoImage(file='imagesGUI/hidden_temple_item_diamonds.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
     
        elif 'in the  Bathroom' in x:
            logging.info("in the bathroom")
            self.item='towel'
            
            self.room_pic = PhotoImage(file='imagesGUI/bath_room.png')
            self.room.configure(image=self.room_pic)
            if 'towel' in x:
                self.item_pic = PhotoImage(file='imagesGUI/bath_room_item_towel.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Break Room' in x:
            logging.info("in the breakroom")
            self.item='apple'
            self.room_pic = PhotoImage(file='imagesGUI/break_room.png')
            self.room.configure(image=self.room_pic)
            if 'apple' in x:
                self.item_pic = PhotoImage(file='imagesGUI/break_room_item_apple.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the PhoneBooth Room' in x:
            logging.info("in the phonebooth room")
            self.item='mobile'
            self.room_pic = PhotoImage(file='imagesGUI/phonebooth_room.png')
            self.room.configure(image=self.room_pic)
            if 'mobile' in x:
                self.item_pic = PhotoImage(file='imagesGUI/phonebooth_room_item_mobile.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Two Way Room' in x:
            logging.info("in the two way room")
            self.item='gold'
            self.room_pic = PhotoImage(file='imagesGUI/twoway_room.png')
            self.room.configure(image=self.room_pic)
            if 'gold' in x:
                self.item_pic = PhotoImage(file='imagesGUI/twoway_room_item_gold.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            

    def processNorth(self):
        """
        Performs log of users journey, places 
        required images in frame 1 as per 
        players location

        """
        logging.info("In North")
        x = self.game.do_go_command('north')
        self.text_area1.configure(text=x)
        if 'in the lobby' in x:
            logging.info("in the lobby")
            self.item='keys'
            self.room_pic = PhotoImage(file='imagesGUI/lobby.png')
            self.room_pic = self.room_pic.subsample(2, 2)
            self.room.configure(image=self.room_pic)
            if 'keys' in x:
                self.item_pic = PhotoImage(file='imagesGUI/lobby_item_keys.png')
                self.item_pic = self.item_pic.subsample(11,9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
                
            
        elif 'in the Room 404' in x:
            logging.info("in the Room 404")
            self.item='knife'
            self.room_pic = PhotoImage(file='imagesGUI/Room-404.png')
            self.room.configure(image=self.room_pic)
            if 'knife' in x:
                self.item_pic = PhotoImage(file='imagesGUI/room_404_item_knife.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Red Room' in x:
            logging.info("in the two red room")
            self.item='money'
            self.room_pic = PhotoImage(file='imagesGUI/red_room.png')
            self.room.configure(image=self.room_pic)
            if 'money' in x:
                self.item_pic = PhotoImage(file='imagesGUI/red_room_item_money.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Luxury Room' in x:
            logging.info("in the luxury room")
            self.item='jewels'
            self.room_pic = PhotoImage(file='imagesGUI/luxury_room.png')
            self.room.configure(image=self.room_pic)
            if 'jewels' in x:
                self.item_pic = PhotoImage(file='imagesGUI/luxury_room_item_jewels.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Hidden Temple' in x:
            logging.info("in the hidden temple")
            self.item='diamonds'
            self.room_pic = PhotoImage(file='imagesGUI/hidden_temple.png')
            self.room.configure(image=self.room_pic)
            if 'diamonds' in x:
                self.item_pic = PhotoImage(file='imagesGUI/hidden_temple_item_diamonds.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
     
        elif 'in the  Bathroom' in x:
            logging.info("in the bathroom")
            self.item='towel'
            self.room_pic = PhotoImage(file='imagesGUI/bath_room.png')
            self.room.configure(image=self.room_pic)
            if 'towel' in x:
                self.item_pic = PhotoImage(file='imagesGUI/bath_room_item_towel.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Break Room' in x:
            logging.info("in the break room")
            self.item='apple'
            self.room_pic = PhotoImage(file='imagesGUI/break_room.png')
            self.room.configure(image=self.room_pic)
            if 'apple' in x:
                self.item_pic = PhotoImage(file='imagesGUI/break_room_item_apple.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the PhoneBooth Room' in x:
            logging.info("in the phonebooth room")
            self.item='mobile'
            self.room_pic = PhotoImage(file='imagesGUI/phonebooth_room.png')
            self.room.configure(image=self.room_pic)
            if 'mobile' in x:
                self.item_pic = PhotoImage(file='imagesGUI/phonebooth_room_item_mobile.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Two Way Room' in x:
            logging.info("in the two way room")
            self.item='gold'
            self.room_pic = PhotoImage(file='imagesGUI/twoway_room.png')
            self.room.configure(image=self.room_pic)
            if 'gold' in x:
                self.item_pic = PhotoImage(file='imagesGUI/twoway_room_item_gold.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
        
        
           

    def processEast(self):
        """
        Performs log of users journey, places 
        required images in frame 1 as per 
        players location

        """
        logging.info("In east")
        x = self.game.do_go_command('east')
        self.text_area1.configure(text = x)
        if 'in the lobby' in x:
            logging.info("in the lobby")
            self.item='keys'
            self.room_pic = PhotoImage(file='imagesGUI/lobby.png')
            self.room_pic = self.room_pic.subsample(2, 2)
            self.room.configure(image=self.room_pic)
            if 'keys' in x:
                self.item_pic = PhotoImage(file='imagesGUI/lobby_item_keys.png')
                self.item_pic = self.item_pic.subsample(11,9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
                
            
        elif 'in the Room 404' in x:
            logging.info("in the room 404")
            self.item='knife'
            self.room_pic = PhotoImage(file='imagesGUI/Room-404.png')
            self.room.configure(image=self.room_pic)
            if 'knife' in x:
                self.item_pic = PhotoImage(file='imagesGUI/room_404_item_knife.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Red Room' in x:
            logging.info("in the red room")
            self.item='money'
            self.room_pic = PhotoImage(file='imagesGUI/red_room.png')
            self.room.configure(image=self.room_pic)
            if 'money' in x:
                self.item_pic = PhotoImage(file='imagesGUI/red_room_item_money.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Luxury Room' in x:
            logging.info("in the luxury room")
            self.item='jewels'
            self.room_pic = PhotoImage(file='imagesGUI/luxury_room.png')
            self.room.configure(image=self.room_pic)
            if 'jewels' in x:
                self.item_pic = PhotoImage(file='imagesGUI/luxury_room_item_jewels.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Hidden Temple' in x:
            logging.info("in the hidden temple")
            self.item='diamonds'
            self.room_pic = PhotoImage(file='imagesGUI/hidden_temple.png')
            self.room.configure(image=self.room_pic)
            if 'diamonds' in x:
                self.item_pic = PhotoImage(file='imagesGUI/hidden_temple_item_diamonds.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
     
        elif 'in the  Bathroom' in x:
            logging.info("in the bathroom")
            self.item='towel'
            self.room_pic = PhotoImage(file='imagesGUI/bath_room.png')
            self.room.configure(image=self.room_pic)
            if 'towel' in x:
                self.item_pic = PhotoImage(file='imagesGUI/bath_room_item_towel.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Break Room' in x:
            logging.info("in the breakroom")
            self.item='apple'
            self.room_pic = PhotoImage(file='imagesGUI/break_room.png')
            self.room.configure(image=self.room_pic)
            if 'apple' in x:
                self.item_pic = PhotoImage(file='imagesGUI/break_room_item_apple.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the PhoneBooth Room' in x:
            logging.info("in the phonebooth room")
            self.item='mobile'
            self.room_pic = PhotoImage(file='imagesGUI/phonebooth_room.png')
            self.room.configure(image=self.room_pic)
            if 'mobile' in x:
                self.item_pic = PhotoImage(file='imagesGUI/phonebooth_room_item_mobile.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Two Way Room' in x:
            logging.info("in the two way room")
            self.item='gold'
            self.room_pic = PhotoImage(file='imagesGUI/twoway_room.png')
            self.room.configure(image=self.room_pic)
            if 'gold' in x:
                self.item_pic = PhotoImage(file='imagesGUI/twoway_room_item_gold.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
        
    def processWest(self):
        """
        Performs log of users journey, places 
        required images in frame 1 as per 
        players location

        """
        logging.info("In west")
        x = self.game.do_go_command('west')
        self.text_area1.configure(text = x)
        if 'in the lobby' in x:
            logging.info("In Looby")
            self.item='keys'
            self.room_pic = PhotoImage(file='imagesGUI/lobby.png')
            self.room_pic = self.room_pic.subsample(2, 2)
            self.room.configure(image=self.room_pic)
            if 'keys' in x:
                self.item_pic = PhotoImage(file='imagesGUI/lobby_item_keys.png')
                self.item_pic = self.item_pic.subsample(11,9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
                
            
        elif 'in the Room 404' in x:
            logging.info("In Room 404")
            self.item='knife'
            self.room_pic = PhotoImage(file='imagesGUI/Room-404.png')
            self.room.configure(image=self.room_pic)
            if 'knife' in x:
                self.item_pic = PhotoImage(file='imagesGUI/room_404_item_knife.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Red Room' in x:
            logging.info("In the red room")
            self.item='money'
            self.room_pic = PhotoImage(file='imagesGUI/red_room.png')
            self.room.configure(image=self.room_pic)
            if 'money' in x:
                self.item_pic = PhotoImage(file='imagesGUI/red_room_item_money.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Luxury Room' in x:
            logging.info("In the luxury room")
            self.item='jewels'
            self.room_pic = PhotoImage(file='imagesGUI/luxury_room.png')
            self.room.configure(image=self.room_pic)
            if 'jewels' in x:
                self.item_pic = PhotoImage(file='imagesGUI/luxury_room_item_jewels.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
        elif 'in the Hidden Temple' in x:
            logging.info("In the hidden temple")
            self.item='diamonds'
            self.room_pic = PhotoImage(file='imagesGUI/hidden_temple.png')
            self.room.configure(image=self.room_pic)
            if 'diamonds' in x:
                self.item_pic = PhotoImage(file='imagesGUI/hidden_temple_item_diamonds.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
            
     
        elif 'in the  Bathroom' in x:
            logging.info("In the bathroom")
            self.item='towel'
            self.room_pic = PhotoImage(file='imagesGUI/bath_room.png')
            self.room.configure(image=self.room_pic)
            if 'towel' in x:
                self.item_pic = PhotoImage(file='imagesGUI/bath_room_item_towel.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Break Room' in x:
            logging.info("In the breakroom")
            self.item='apple'
            self.room_pic = PhotoImage(file='imagesGUI/break_room.png')
            self.room.configure(image=self.room_pic)
            if 'apple' in x:
                self.item_pic = PhotoImage(file='imagesGUI/break_room_item_apple.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the PhoneBooth Room' in x:
            logging.info("In the phonebooth room")
            self.item='mobile'
            self.room_pic = PhotoImage(file='imagesGUI/phonebooth_room.png')
            self.room.configure(image=self.room_pic)
            if 'mobile' in x:
                self.item_pic = PhotoImage(file='imagesGUI/phonebooth_room_item_mobile.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
            
        elif 'in the Two Way Room' in x:
            logging.info("In the two way room")
            self.item='gold'
            self.room_pic = PhotoImage(file='imagesGUI/twoway_room.png')
            self.room.configure(image=self.room_pic)
            if 'gold' in x:
                self.item_pic = PhotoImage(file='imagesGUI/twoway_room_item_gold.png')
                self.item_pic = self.item_pic.subsample(11, 9)
                self.btn_itempic.place(x=390,y=30)
                self.btn_itempic.configure(image=self.item_pic)
            else:
                self.btn_itempic.place_forget()
        
    def do_command(self):
        command = self.cmd_area.get()  # Returns a 2-tuple
        self.process_command(command)

    def get_command_string(self, input_line):
        """
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)

    def process_command(self, command):
        """
            Process a command.
        :param command: a 2-tuple of the form (command_word, second_word)
        """
        command_word, second_word = self.get_command_string(command)
        if command_word != None:
            command_word = command_word.upper()
            if command_word == "HELP":
                self.text_area1.configure(text=self.game.print_help())
            elif command_word == "GO":
                self.text_area1.configure(text=self.game.do_go_command(second_word))
            elif command_word == "GET":
                self.text_area1.configure(text=self.do_get_command(second_word))
            else:
                # Unknown command...
                self.text_area1.configure(text="Don't know what you mean.")



if __name__ == "__main__":
    myApp = App()
   
