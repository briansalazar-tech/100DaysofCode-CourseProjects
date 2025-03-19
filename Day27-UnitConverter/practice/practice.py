import tkinter


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Window
window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20) # Add padding

# Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.config(text="Some more text")

# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50) # Add padding

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
























### *args
# def add(*args):
#     return sum(args)

# print(add(1, 2, 3, 4, 5, 6))


### **kwargs
# def calculate(n, **kwargs):
#     print(kwargs)
#     print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply =5)

# class Car:

#     def __init__(self, **kwarg):
#         self.make = kwarg.get("make") # Benefit of using .get() is that if value is not passed, it will return None instead of an error
#         self.model = kwarg.get("model")
#         self.color = kwarg.get("color")
#         self.engine = kwarg.get("engine")
#         self.seats = kwarg.get("seats")

# my_car = Car(make="Nissan")#, model="GT-R")
# print(my_car.model)