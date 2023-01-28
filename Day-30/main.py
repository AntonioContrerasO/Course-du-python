# try:
#     file = open("a_file.txt")
#     a_dictionary = {"Key":"Value"}
#     print(a_dictionary["Key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     contents = file.read()
#     print(contents)
# finally:
#     raise TypeError("This is an error that I made up")
#     # file.close()
#     # print("File was close")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2

print(bmi)
