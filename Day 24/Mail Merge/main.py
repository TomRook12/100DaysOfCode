#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#open the letter, assign it to a variable
#open the list of names, assign to a list with for loop
#search letter for the text to be replaced, replace the name and then create the file with the name of there person

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    blank_letter = letter.read()

with open("./Input/Names/invited_names.txt", mode="r") as names:
    names = names.readlines()

for i in range(len(names)):
    name = names[i]
    clean_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", mode="w") as to_you:
        to_you.write(blank_letter.replace("[name]", clean_name))



