# file = open("./Day24-MailMerger/my_file.txt")
# with open("./Day24-MailMerger/my_file.txt") as file:
#     content = file.read()
#     print(content)
# file.close()

with open("./Day24-MailMerger/new_file.txt", mode="a") as file:
    file.write("\nNew text.")
    
    # print(content)