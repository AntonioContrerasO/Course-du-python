# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("Input/Names/invited_names.txt") as names:
#     list_names = []
#     for name in names:
#         new_name = ""
#         for letter in name:
#             if letter == '\n':
#                 break
#             new_name += letter
#         list_names.append(new_name)
#     print(list_names)
#
# with open("Input/Letters/starting_letter.txt") as letter:
#     new_letter = []
#     for sentence in letter:
#         new_letter.append(sentence)
#     for name in list_names:
#         new_letter[0] = f"Dear {name},\n"
#         with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="a") as new_letter_to:
#             for new_sentence in new_letter:
#                 new_letter_to.write(new_sentence)

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    list_names = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in list_names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        with open(f"Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as new_letter_to:
            new_letter_to.write(new_letter)
