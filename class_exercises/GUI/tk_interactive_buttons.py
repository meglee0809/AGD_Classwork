import tkinter as tk
import random

class ClickApp(tk.Tk):
    """ Button clicker application """

    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()

        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.radio_colour_frame = RadioColorFrame(self)

        self.radio_colour_frame.pack(side=tk.LEFT)
        self.clicker_frame.pack(side=tk.LEFT, expand=True)

class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, text = "Cooler background changer \n"
                                           "V235.3536")
        self.hextext = tk.Label(self, text = "HEX CODE :D")

        self.counter = 0
        self.btn = tk.Button(self, text="click me",
                             fg="white", bg="red",
                             activeforeground="white", activebackground="red",
                             command=self.click_button_B)
        self.response_txt = tk.Label(self, text = ":)")
        self.randomiser_btn = tk.Button(self, text="randomiser",
                             fg="white", bg="red",
                             activeforeground="white", activebackground="red",
                             command=self.click_button_randomiser)
        self.reset_btn = tk.Button(self, text="reset teehee",
                             fg="white", bg="red",
                             activeforeground="white", activebackground="red",
                             command=self.click_button_reset)

        self.slider = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL,
                               command=self.sliderchange)
        self.entry = tk.Entry(self)
        self.note_label = tk.Label(self, text="note: effects are only applied \n"
                                             "with the slider moved\n"
                                             "good luck lol")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.label.grid(row=0,column=0,**settings)
        self.hextext.grid(row=0,column=1,**settings)
        self.btn.grid(row=1, column=0, **settings)
        self.response_txt.grid(row=1, column=1, **settings)
        self.randomiser_btn.grid(row=2, column=0, **settings)
        self.reset_btn.grid(row=2, column=1, **settings)
        self.slider.grid(row=3,column=0, **settings)
        self.entry.grid(row=4, column=0, **settings)
        self.note_label.grid(row=5, column=0, **settings)

    def click_button_B(self):
        self.counter += 1
        self.response_txt.config(text = self.counter)

    def click_button_reset(self):
        self.counter = 0
        self.response_txt.config(text=":)")
        self.hextext.config(text = "HEX CODE :D")
        self.master.config(bg="white")

    def click_button_randomiser(self):
        num = random.randint(0,255)
        self.counter = num
        self.response_txt.config(text = self.counter)

    def sliderchange(self,colour_rgb):
        if self.entry.get() == "":
            entry_colour = 0
        else:
            entry_colour = int(self.entry.get())

        if entry_colour > 255:
            entry_colour = int(self.entry.get())% 255
        elif entry_colour < 0:
            entry_colour += 255

        colour_hex = f'#{int(self.counter):02x}{int(colour_rgb):02x}{entry_colour:02x}'
        self.master.config(bg=colour_hex)
        self.hextext.config(text = colour_hex)
        #self.rgbtext.config(text=f"{int(self.counter)},{int(colour_rgb)},{int(entry_colour)}")

class RadioColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.Label = tk.Label(self, justify= "left",text = "Background Colour changer\n"
                                           "V43.355")

        # Color choices
        self.colors = ['red', 'yellow', 'green','cool']

        # Create a tk variable which will hold the value of the selected color
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color)
                                             for color in self.colors]
        self.response_txt = tk.Label(self, text=" ")

        self.place_widgets()

    def place_widgets(self):
        self.Label.pack(side=tk.TOP)
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(10, 10), pady=5)
        self.response_txt.pack(side=tk.TOP)

    def change_color(self):
        color = self.selected_color.get() #gets the selected radio button's colour
        self.response_txt.config(justify ="left",text="You thought you could change\n"
                                      "the main background?\n"
                                      "you so silly ")
        if color == "cool":
            color = "cyan"
        self.config(bg=color)

if __name__ == '__main__':

    app = ClickApp()
    app.title("just a background changer game (to cure all ailments)")
    app.geometry('550x500+100+100')

    app.mainloop()