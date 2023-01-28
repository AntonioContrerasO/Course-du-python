# import another_module
# from turtle import Turtle, Screen
#
# print(another_module.another_variable)
#
# timmy = Turtle()
#
# print(timmy)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.shape("turtle")
#
#
# timmy.color("OrangeRed","DeepSkyBlue2")
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = 'l'
print(table)

