import tkinter as tk
from tkinter import ttk


# big frames ----------------------------------------------------------------------------------------------
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.MainTitle = MainTitle(self)
        self.text_labels = TextLabels(self)
        self.options = Options(self)
        self.submit_button = SubmitButton(self)

        self.MainTitle.grid(row=0, column=0)
        self.text_labels.grid(row=1, column=0)
        self.options.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=0)


class Options(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entry_boxes = EnterBoxes(self)
        self.radio_boxes = Radio_boxes(self)
        self.country_picker = CountryPicker(self)
        self.checkbox_frame = CheckboxFrame(self)

        self.entry_boxes.grid(row=1, column=0)
        self.radio_boxes.grid(row=2, column=0)
        self.country_picker.grid(row=3, column=0)
        self.checkbox_frame.grid(row=4, column=0)


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
        settings = {'padx': 10, 'pady': 9, 'sticky': 'nswe'}
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
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.fullname_entry.grid(row=0, column=0, **settings)
        self.email_entry.grid(row=1, column=0, **settings)

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
    app.geometry('550x500+100+100')

    app.mainloop()