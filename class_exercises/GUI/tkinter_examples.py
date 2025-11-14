import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self, text="Do Not Click The Button"
                                  )
        self.btn = tk.Button(self, text="Do Not Click Me",
                                   fg="white",bg="red2",
                                   activeforeground="white", activebackground="red4") #make a STOP CLICKING ME -> look at what you've done you can do anything else now but click the button. How do you feel. Bored? Surely not. After not following my rules ofr os long you would think not.
        self.edt = tk.Entry(self)  # input box
        self.sld = tk.Scale(self, from_=0, to=100, orient=tk.VERTICAL)

        self.config(bg="gray5") #screen bg

        self.place_widgets() #widget is an item

    def place_widgets(self):
        settings = {'padx': 10, 'pady' : 10, 'sticky': 'nswe'} #pad puts space around the stuff
        self.txt.grid(row=0,column=0, **settings)  # puts it at the top
        self.btn.grid(row=0,column=1, **settings)
        self.edt.grid(row=1,column=1, **settings)
        self.sld.grid(row=1,column=0, **settings)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)

if __name__ == '__main__':
    root = tk.Tk() #gives a blank GUI
    root.geometry('500x500+100+100') #frame
    root.title("The Do Not Press The Button Game (dont press it).exe") #the name of the window
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop() #keeps the program listening dun dun dunnn...