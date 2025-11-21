import tkinter as tk
from tkinter import ttk
from tk_temperature import *


class Mainapp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.Heading = Heading(self)

        self.Temperatures = Temperatures(self)

        self.Heading.grid(row=0, column=0, columnspan=3)

        self.Temperatures.grid(row=2, column=0)


class Heading(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.heading = tk.Label(self, text="THE Temperature Conversion App", font=("Arial", 20))
        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'w'}
        self.heading.grid(row=0, column=0, **settings)


class EntryBox(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entry = tk.Entry(self)
        self.combobox = ttk.Combobox(self)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'w'}
        self.entry.grid(row=0, column=1, **settings)


class SubmitButton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.submit = tk.Button(self, text="Submit",
                                bg="gray67", fg="gray1",
                                activebackground="red",
                                activeforeground="white")
        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 5, 'sticky': 'w'}
        self.submit.grid(row=0, column=0, **settings)


class Temperatures(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #self.config(bg="midnight blue")
        # USE AFTER -> text_color = "white"
        self.Celcius = tk.Label(self, text="Celcius", font="Arial", justify=tk.LEFT)
        self.Celciusoutput = tk.Label(self, text=f"{temp.celsius}", font="Arial")

        self.Fahrenheit = tk.Label(self, text="Fahrenheit", font="Arial", justify=tk.LEFT)
        self.Fahrenheitoutput = tk.Label(self, text=f"{temp.fahrenheit}", font="Arial")

        self.Kelvin = tk.Label(self, text="Kelvin", font="Arial")
        self.Kelvinoutput = tk.Label(self, text=f"{temp.kelvin}", font="Arial")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 5, 'sticky': 'w'}
        self.Celcius.grid(row=0, column=0, **settings)
        self.Celciusoutput.grid(row=0, column=1, **settings)
        self.Fahrenheit.grid(row=1, column=0, **settings)
        self.Fahrenheitoutput.grid(row=1, column=1, **settings)
        self.Kelvin.grid(row=2, column=0, **settings)
        self.Kelvinoutput.grid(row=2, column=1, **settings)






if __name__ == '__main__':

    app = Mainapp()
    app.title("THE temperature conversion app")
    app.geometry('550x500+100+100')

    app.mainloop()