text = input("Enter a text to write to the file: ")

with open("output.txt", "w") as f:
    f.write(text + "\n")
    print("Data successfully written to output.txt.\n")
    
text_append = input("Enter additional text to append: ")

with open("output.txt", "a") as f:
    f.write(text_append + "\n")
    print("Data successfully appended.\n")

with open("output.txt", "r") as f:
    print("Final content of output.txt: ")
    print(f.read())



    