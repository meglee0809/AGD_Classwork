import tkinter as tk
from tkinter import ttk

#big frames ----------------------------------------------------------------------------------------------
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.MainTitle = MainTitle(self)
        self.text_labels = TextLabels(self)
        self.entry_boxes = EnterBoxes(self)
        self.radio_boxes = Radio_boxes(self)
        self.checkbox_frame = CheckboxFrame(self)
        self.submit_button = SubmitButton(self)

        self.MainTitle.grid(row=0, column=0)
        self.text_labels.grid(row=1, column=0)
        self.Options.grid(row=1,column=1)
        self.submit_button.grid(row=2, column=0)


class Options(tk.Tk):
    def __init__(self):
        super().__init__()

        self.entry_boxes = EntryBoxes(self)
        self.radio_boxes = Radio_boxes(self)
        self.country_picker = CountryPicker(self)
        self.checkbox_frame = CheckboxFrame(self)

        self.entry_boxes.grid(row=1, column=0)
        self.radio_boxes.grid(row=2, column=0)
        self.country_picker.grid(row=3, column=0)
        self.checkbox_frame.grid(row=4, column=0)


#smol frames ---------------------------------------------------------------------------------------------------
class MainTitle(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)

        self.Mainlabel = tk.Label(self, text = "Registration Form", justify = "left", font = ("Arial",24))

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.Mainlabel.grid(row=0,column=0,**settings)


class TextLabels(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)

        self.fullname_label = tk.Label(self, text = "Full name",justify = "left",font = "Arial")
        self.email_label = tk.Label(self, text="Email", justify = "left",font="Arial")
        self.gender_label = tk.Label(self, text="Gender", justify = "left",font="Arial")
        self.country_label = tk.Label(self, text="Country", justify = "left",font="Arial")
        self.programming_label = tk.Label(self, text="Programming", justify = "left",font="Arial")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.fullname_label.grid(row=0,column=0,**settings)
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


class Radio_boxes(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.colors = ['Male', 'Female']

        self.radio_options = [tk.Radiobutton(self, text=gender,
                                             value=gender,
                                             variable=self.selected_gender)
                              for gender in self.genders]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.LEFT, anchor='w', padx=(10, 10), pady=5)


class CheckboxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create radio buttons (list comprehension)
        self.java_check = ttk.checkbox(self, text="Java")
        self.python_check = ttk.checkbox(self, text="Python")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 5, 'sticky': 'w'}
        self.java_check.grid(row=0, column=0, **settings)
        self.python_check.grid(row=0, column=1, **settings)


class SubmitButton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.submit = tk.Button(self, text="Submit",
                                bg="gray67",fg="gray1",
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