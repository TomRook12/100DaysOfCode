#with open("new_file.txt", mode="w") as file:
#    file.write("\nNew text.")

with open("../../../../tomro/OneDrive/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)
