# Day 24: Mail Merger Challenge
## Lesson Overview
Day 24 of the 100 Days of Code course focused on working with files and the day’s project was to create a mail merger script.

The concepts covered in this lesson include:
- Working with files
    - Opening files
    - Writing and appending files
    - Opening files using with
- File paths
    - Absolute file paths
    - Relative file paths
## Project
### Project Walkthrough
My spin on this project starts with an empty list called **name_list** and a variable called **template**. **Name_list** stores the names in the **invited_names.txt** file and *template* stores the **starting_letter.txt** file's content.

The script starts by adding the names from **invited_names.txt** to **name_list**. The data needs to be cleaned so the **strip() method** removes new line characters from the names before saving to the variable.

The script then gets the contents of the **starting_letter.txt** file and saves it to the **template** variable.

With the list of names and the letter template saved, the next step is to create the letters to send. Using a For loop on the list of names, the **[name] placeholder** is replaced with the current name. Additionally the **replace() method** replaces “Angela” with my name (Brian) for an added touch. Still working in the for loop, the letter that is created is saved with the name of “**letter_for_[name].txt**” where [name] is the name of the person receiving the letter. 

And with that, the created letters are found in the **ReadyToSend** folder located in the **Output** folder!
