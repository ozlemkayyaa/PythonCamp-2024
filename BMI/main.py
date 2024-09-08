from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=65, pady=65)

weight = Label(text="Enter your weight (kg)")
weight.pack()

entry_weight = Entry(width=10)
entry_weight.pack()

height = Label(text="Enter your height (cm)")
height.pack()

entry_height = Entry(width=10)
entry_height.pack()

result = Label()
result.pack()


def calculate_bmi():
    global height
    global weight
    height = float(entry_height.get()) / 100
    weight = float(entry_weight.get())

    if height == "" and weight == "":
        result.config(text="Enter both weight and height!")
    else:
        try:
            bmi = weight / (height*height)
            result_string = write_result(bmi)
            result.config(text=result_string)
        except:
            result.config(text="Enter a valid number")


my_button = Button(text="Calculate", command=calculate_bmi)
my_button.pack()


def write_result(bmi):
    result_string = f"Your BMI is: {round(bmi, 2)}. You are "
    if bmi < 18.5:
        result_string += "Underweight"
    elif 18.5 < bmi <= 24.9:
        result_string += "Normal"
    elif 25 < bmi <= 29.9:
        result_string += "OverWeight"
    elif 30 < bmi <= 34.9:
        result_string += "Obese"
    elif bmi > 35:
        result_string += "Extremely Obese"
    return result_string


window.mainloop()
