import pyinputplus as pyip

name = pyip.inputStr("Name please: ")
age = pyip.inputInt("Age please: ",
                    min=3,
                    max=100,
                    )