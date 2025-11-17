import tkinter as tk

class Mainapp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.heading = Heading(self)

        self.heading.grid(row=0, column=0)

class Heading(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.heading = tk.Label(self, text="THE Temperature Conversion App", font=("Arial", 20))

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.heading.grid(row=0, column=0, **settings)












if __name__ == '__main__':

    app = Mainapp()
    app.title("THE temperature conversion app")
    app.geometry('550x500+100+100')

    app.mainloop()