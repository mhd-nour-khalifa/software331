"""
    Stage: Development-01
    @author:Mhd Nour Khalifa
    @author:Huseyin Enes Tandogan
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox

users = [ ('admin','admin')]
class LoginWindow:
    # constructor

    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Library")
        self._initializeGUI()
        self._addGUIElementsToFrame()
        self.window.configure(bg='#333333')
        # start the GUI frame
        self.window.mainloop()

    

    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.lbl02 = tk.Label(text="Password" ,bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        
        self.req = tk.Label(text="")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="Login")
        self.btn02 = tk.Button(text="Register")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)
        
        
        self.exitbtn = tk.Button(text="Exit")
        
        self.exitbtn.bind("<Button-1>", self.handle_click)



   
    def signup(self):
        input_user = self.txt01.get()
        input_pass = self.txt02.get()
        #append it to the users list
        users.extend([(input_user,input_pass)])
        #print that the user is registerd successfully
        print('user {} with pass {} signed up correctly'.format(input_user,input_pass))
        self.req.config(text="signed up correctly")
    
    def login(self):
       input_user = self.txt01.get()
       input_pass = self.txt02.get() 
       #reset the info label
       self.req.config(text="")
       # iterate through the users list for validation
       for user,passw in users:
            if (user,passw) == (input_user,input_pass):
                #open the window and remove the login page
                self.blank_page()
                self.window.destroy()
                self.blank.mainloop()
       


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=15, pady=15)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)
        
        self.req.grid(row=10, column=1, padx=1, pady=1)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)
        
        self.exitbtn.grid(row=3, column=1, padx=10, pady=5)
    def blank_page(self):
            self.blank = tk.Tk()
            self.blank.geometry('700x700')
            self.blank.title('Welcome to the library')
            self._initializeGUI()
            
            self._addGUIElementsToFrame()


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        if(event.widget == self.btn01):
            self.login()
          
        if(event.widget == self.btn02):
            self.signup()  
        elif event.widget == self.exitbtn:
                # call exit method
            self.exit()
        
        pass
    
    def exit(self):
        self.window.destroy()
        



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()





