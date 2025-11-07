# Project Structure

from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')         # As you are in current dir, now his path take it form here
    items = list(path.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")



def creatFile():
    try:
        readFileAndFolder()
        name = input("Please tell you file name: ")
        p = Path(name)

        if not p.exists() and p.is_file():
            with open(p, "w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")

        else:
            print("This file is already exist")

    except Exception as err:
        print(f"An error occured as {err}")



def readFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("READED SUCCESSFULLY")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"An error occured as {err}")


def updateFile():

    try:
        readFileAndFolder()
        name = input("Tell which file you want to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content in your file")

            res = int(input("Enter your response"))

            if res == 1:
                name2 = input("Tell you new file name: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write, this is overwrite the data")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append, this is append the data")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error occured {err}")


def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File has been remove successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error occured {err}")



print("press 1 for crating a file: ")
print("press 2 for reading a file: ")
print("press 3 for updating a file: ")
print("press 3 for deleting a file: ")


check = int(input("Enter your respone: "))

if check == 1:
    creatFile()

if check == 2:
    readFile()

if check == 3:
    updateFile()

if check == 4:
    deleteFile()

