from tkinter import *


def convert():
    """Convert miles input to km and display conversion"""
    miles = user_input.get()
    km = float(miles) * 1.60934
    conversion_label.config(text=f"{km}")


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=125)
window.config(padx=20, pady=20)

# Text entry box
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is equal label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Conversion label
conversion_label = Label(text="0")
conversion_label.grid(column=1, row=1)

# Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()