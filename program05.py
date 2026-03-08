#program 05
#using try and except to handle file not found error
file01 = input("enter file name: ")

try:
    with open(file01, "r") as file:
        content = file.read()
    print(content)

except FileNotFoundError as e:
    print("file not found........", e)
