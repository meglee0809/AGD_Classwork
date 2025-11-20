import tkinter as tk
from tkinter import ttk
''' RESPONSE - “Well done. Your registration form looks great and I really like the careful details, 
such as setting the colors on the submit button. Some pupils did the whole form as one frame, 
and you have gone the other way with including many frames. 
This means that it is hard to make everything line up - 
your response boxes don't quite line up with your labels.
A good tip is to temporarily give every frame a different background, 
and then you will see exactly how the frames are spaced.
A better option would be to use a single grid system for the whole main menu. 
If something doesn't fit in the grid (like the overall title), 
you can spread if over two columns using the COLUMNSPAN option, which is like merging cells in excel. 
The radio boxes and check boxes can be in their own frame, but these frames are placed within the overall grid. 
For check box widgets themselves it's easier to pack them in their frame rather than use the grid geometry.”'''

# big frames ----------------------------------------------------------------------------------------------
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.MainTitle = MainTitle(self)
        self.text_labels = TextLabels(self)
        self.options = Options(self)
        self.submit_button = SubmitButton(self)

        self.MainTitle.grid(row=0, column=0)
        self.text_labels.grid(row=1, column=0, rowspan = 5)
        self.options.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=0)


class Options(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entry_boxes = EnterBoxes(self)
        self.radio_boxes = Radio_boxes(self)
        self.country_picker = CountryPicker(self)
        self.checkbox_frame = CheckboxFrame(self)

        self.entry_boxes.grid(row=1, column=0,rowspan=2)
        self.radio_boxes.grid(row=3, column=0)
        self.country_picker.grid(row=4, column=0)
        self.checkbox_frame.grid(row=5, column=0)


# smol frames ---------------------------------------------------------------------------------------------------
class MainTitle(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)

        self.Mainlabel = tk.Label(self, text="Registration Form", justify="left", font=("Arial", 24))

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.Mainlabel.grid(row=0, column=0, **settings)


class TextLabels(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)

        self.fullname_label = tk.Label(self, text="Full name", justify="left")
        self.email_label = tk.Label(self, text="Email", justify="left")
        self.gender_label = tk.Label(self, text="Gender", justify="left")
        self.country_label = tk.Label(self, text="Country", justify="left")
        self.programming_label = tk.Label(self, text="Programming", justify="left")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 5, 'sticky': 'w'}
        self.fullname_label.grid(row=0, column=0, **settings)
        self.email_label.grid(row=1, column=0, **settings)
        self.gender_label.grid(row=2, column=0, **settings)
        self.country_label.grid(row=3, column=0, **settings)
        self.programming_label.grid(row=4, column=0, **settings)


class EnterBoxes(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)
        self.fullname_entry = tk.Entry(self)
        self.email_entry = tk.Entry(self)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'sticky': 'w'}
        self.fullname_entry.grid(row=0, column=0, pady = 0, **settings)
        self.email_entry.grid(row=1, column=0, pady = 2, **settings)

class CountryPicker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)

        self.current_country = tk.StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.current_country, state='readonly', width=37)

        self.combobox['values'] = ('Malaysia','Anywhere that is not Malaysia')
        self.combobox.set('select your country')

        self.current_value = self.combobox.get()

        self.place_widgets()

    def place_widgets(self):
        self.combobox.grid(row=0, column=0, padx=10, pady=5, sticky='w')


class Radio_boxes(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.genders = ['Male', 'Female']
        self.gender_choice = tk.StringVar()
        self.gender_choice.set(self.genders[0])

        self.gender_options = [tk.Radiobutton(self, text=gender,
                                              value=gender,
                                              variable=self.gender_choice)
                               for gender in self.genders]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.gender_options:
            ro.pack(side=tk.LEFT, anchor='w', padx=(10, 10), pady=5)


class CheckboxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create radio buttons (list comprehension)
        self.java_check = ttk.Checkbutton(self, text="Java")
        self.python_check = ttk.Checkbutton(self, text="Python")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 5, 'sticky': 'w'}
        self.java_check.grid(row=0, column=0, **settings)
        self.python_check.grid(row=0, column=1, **settings)


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


if __name__ == '__main__':
    app = MainApp()
    app.title("Registration Form")
    app.geometry('600x300+100+100')

    app.mainloop()
