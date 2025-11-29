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
        self.PhotoFrame.grid(row=1, column=3, columnspan=1, sticky="wnse")


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
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var)
        self.entry_var.trace_add('write', self.on_change)

        self.current_option = tk.StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.current_option)
        self.combobox['values'] = ('Celsius', 'Fahrenheit', 'Kelvin')
        self.combobox.set('+ select unit +')

        self.current_option.trace_add('write', self.on_change)

        #second row---------
        # self.config(bg="midnight blue")
        # USE AFTER -> text_color = "white"

        self.Celsius = tk.Label(self, text="Celsius", font="Arial", justify=tk.LEFT)
        self.Celsiusoutput = tk.Label(self, text="", font="Arial")

        self.Fahrenheit = tk.Label(self, text="Fahrenheit", font="Arial", justify=tk.LEFT)
        self.Fahrenheitoutput = tk.Label(self, text="", font="Arial")

        self.Kelvin = tk.Label(self, text="Kelvin", font="Arial", justify=tk.LEFT)
        self.Kelvinoutput = tk.Label(self, text="", font="Arial")

        #third row--------
        self.sliderLabel = tk.Label(self, text="Celsius Slider :D", font="Arial", justify=tk.LEFT)
        self.slider = tk.Scale(self, from_=-273, to=200, orient=tk.HORIZONTAL,
                               command=self.slider_change)

        self.place_widgets()


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

        self.sliderLabel.grid(row=4, column=0, **settings)
        self.slider.grid(row=4, column=1, columnspan=2, **settings)


    def on_change(self, *args):
        #value = self.entry_var.get()
        option = self.current_option.get().lower()

        if self.entry.get() == "":
            temp = Temperature(celsius=0)
        elif option == "celsius":
            temp = Temperature(celsius=int(self.entry.get()))
        elif option == "fahrenheit":
            temp = Temperature(fahrenheit=int(self.entry.get()))
        elif option == "kelvin":
            temp = Temperature(kelvin=int(self.entry.get()))

        self.Celsiusoutput.config(text=temp.celsius)
        self.Fahrenheitoutput.config(text=temp.fahrenheit)
        self.Kelvinoutput.config(text=temp.kelvin)

        self.change_bg_colours(temp)
        self.master.PhotoFrame.update_photo(temp)

    def slider_change(self, value, *args):
        temp = Temperature(celsius=float(value))

        self.Celsiusoutput.config(text=temp.celsius)
        self.Fahrenheitoutput.config(text=temp.fahrenheit)
        self.Kelvinoutput.config(text=temp.kelvin)

        self.change_bg_colours(temp)
        self.master.PhotoFrame.update_photo(temp)

    def change_bg_colours(self, temp):

        min_temp = -273
        mid_temp = 20
        max_temp = 200

        if temp.celsiusint <= mid_temp: #blue
            ratio = (temp.celsiusint - min_temp) / (mid_temp - min_temp)
            ratio = max(0, min(ratio, 1))
            red = int(255 * ratio)
            green = int(255 * ratio)
            blue = int(255)
        else: #red
            ratio = (temp.celsiusint - mid_temp) / (max_temp - mid_temp)
            ratio = max(0, min(ratio, 1))
            red = 255
            green = int(255 * (1 - ratio))
            blue = int(255 * (1 - ratio))

        colour_hex = f'#{red:02x}{green:02x}{blue:02x}'
        #frame_colour_hex = f'#{red//3:02x}{green//3:02x}{blue//3:02x}'

        self.master.config(bg=colour_hex)
        #self.config(bg=frame_colour_hex)



class PhotoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.photo_label = tk.Label(self)
        self.photo_label.grid(row=0, column=0, padx=10, pady=10)
        self.current_photo = None

    def update_photo(self, temp):
        if temp.celsiusint >= 22:
            photo_file = "hawt.png"
        elif temp.celsiusint < 4:
            photo_file = "kalt.png"
        else:
            photo_file = "leaf.png"

        self.current_photo = tk.PhotoImage(file=photo_file,size)
        self.photo_label.config(image=self.current_photo)


if __name__ == '__main__':

    app = Mainapp()
    app.title("THE temperature conversion app")
    temp = Temperature(25,"celsius")
    app.geometry('550x500+100+100')

    app.mainloop()