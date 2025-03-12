name_list = []
template = ""

# Read invited_names.txt and add names to name_list
with open("Day24-MailMerger/Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    name_list = names

# Strip newline character from each name
for name in range(len(name_list)):
    name_list[name] = name_list[name].strip("\n")

# Save starting_letter to letter_text
with open("Day24-MailMerger/Input/Letters/starting_letter.txt", mode="r") as letter_file:
        template = letter_file.read()

# Repalce placeholder and sender name in template and create new letter to send
for name in name_list:
    letter_text = template
    letter_text = letter_text.replace("[name]", name)
    letter_text = letter_text.replace("Angela", "Brian")
    # print(letter_text)
    
    # Save the letters in the folder "ReadyToSend"
    with open(f"Day24-MailMerger/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(letter_text)

