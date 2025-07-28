import os
# Create the file and write the first line
with open("motto.txt", "w") as motto:
    motto.write("Fiat Lux!\n")

# Append to the file
with open("motto.txt", "a") as motto:
    motto.write("Let there be light!\n")

# Read the file and prints its contents
with open("motto.txt", "r") as motto:
    contents = motto.read()
    print(contents)