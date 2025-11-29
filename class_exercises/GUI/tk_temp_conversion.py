import tkinter as tk
from tkinter import ttk
from tk_temperature import Temperature
#from class_exercises.photos import GET PHOTOS

#4:51-

class Mainapp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.Heading = Heading(self)
        self.TemperatureFrame = TemperatureFrame(self)
        self.PhotoFrame = PhotoFrame(self)

        self.Heading.grid(row=0, column=0, columnspan=3, sticky="wnse")
        self.TemperatureFrame.grid(row=1, column=0, columnspan=2, sticky="wnse")
        self.PhotoFrame.grid(row=1, column=1, columnspan=1, sticky="wnse")


class Heading(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.heading = tk.Label(self, text="THE Temperature Conversion App", font=("Arial", 20))
        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'w'}
        self.heading.grid(row=0, column=0, **settings)


class TemperatureFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #first row -----------
        self.entry = tk.Entry(self)

        self.current_option = tk.StringVar()
        self.combobox = ttk.Combobox(self)
        self.combobox['values'] = ('Celsius', 'Fahrenheit', 'Kelvin')
        self.combobox.set('+ select unit +')
        self.current_option = self.combobox.get()
        if self.entry.get() == "":
            temp = 0
        else:
            temp = Temperature(int(self.entry.get()),self.current_option.lower())

        #second row---------
        # self.config(bg="midnight blue")
        # USE AFTER -> text_color = "white"
        self.Celsius = tk.Label(self, text="Celsius", font="Arial", justify=tk.LEFT)
        self.Celsiusoutput = tk.Label(self, text=f"{'''temp.celsius'''}", font="Arial")

        self.Fahrenheit = tk.Label(self, text="Fahrenheit", font="Arial", justify=tk.LEFT)
        self.Fahrenheitoutput = tk.Label(self, text=f"{'''temp.fahrenheit'''}", font="Arial")

        self.Kelvin = tk.Label(self, text="Kelvin", font="Arial", justify=tk.LEFT)
        self.Kelvinoutput = tk.Label(self, text=f"{'''temp.kelvin'''}", font="Arial")

        #third row--------
        self.slider = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL,
                               ) #command=self.sliderchange

        self.place_widgets()
        self.change_bg_colours()


    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'w'}
        self.entry.grid(row=0, column=0, **settings)
        self.combobox.grid(row=0, column=1, **settings)

        self.Celsius.grid(row=1, column=0, **settings)
        self.Celsiusoutput.grid(row=1, column=1, **settings)
        self.Fahrenheit.grid(row=2, column=0, **settings)
        self.Fahrenheitoutput.grid(row=2, column=1, **settings)
        self.Kelvin.grid(row=3, column=0, **settings)
        self.Kelvinoutput.grid(row=3, column=1, **settings)

        self.slider.grid(row=4, column=0, columnspan=2, **settings)


    def change_bg_colours(self):
        if self.entry.get() == "":
            colour_hex = f'#{255:02x}{255:02x}{255:02x}'
        else:
            if temp.celsius >= 10:
                colour_hex = f'#{255-(temp.celsius%255):02x}{255-(temp.celsius%255):02x}{255:02x}'
            elif temp.celsius < 10:
                colour_hex = f'#{255:02x}{255 - (temp.celsius % 255):02x}{255 - (temp.celsius % 255):02x}'

        self.master.config(bg=colour_hex)



class PhotoFrame(tk.Frame): #GET PHOTOS
    def __init__(self, master):
        super().__init__(master)
'''
        if temp.celsius >= 22:
            self.photo = tk.PhotoImage(file="hawt.png")
        elif temp.celsius < 4:
            self.photo = tk.PhotoImage(file="kalt.png")
        else:
            self.photo = tk.PhotoImage(file="happikitty.png")
            
        self.photo.grid(row=0, column=0, padx=10, pady=10)
'''



if __name__ == '__main__':

    app = Mainapp()
    app.title("THE temperature conversion app")
    temp = Temperature(25,"celsius")
    app.geometry('550x500+100+100')

    app.mainloop()