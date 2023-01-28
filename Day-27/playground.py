# def add(*numbers):
#     print(sum(numbers))
#     return sum(numbers)
#
# add(1,2,3,4,5,5)

def calculate(n,**kwargs):
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)


calculate(2,add = 3, multiply = 5)

class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("steats")


my_car = Car(make="Nissan")
print(my_car.model)

# # Label
#
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.config(text="New txt")
# my_label.grid(column=0,row=0)
# my_label.config(padx=50,pady=50)
#
#
# def button_clicked():
#     my_label.config(text=input.get())
# def random_pos():
#     button2.grid(column=random.randint(0,4),row=random.randint(0,4))
#
# # Button
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1,row=1)
# button2 = Button(text="Click Me", command=random_pos)
# button2.grid(column=2,row=0)
#
# # Entry
# input = Entry(width=10)
# input.grid(column=4,row=2)
