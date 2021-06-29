import os
from time import sleep
from rich.console import Console


def startUp():
    print("Welcome to DupsRemover!\n")
    while True:
        terms = input("This program requests to read your file and folder names. Do you wish to continue?\n> ")
        if terms.lower() not in ["yes", "no", "y", "n"]:
            print("You must respond with \"yes\" or \"no\"\n")
            continue
        else:
            if terms.lower() in ["yes", "y"]:
                # will go to next prompt, function, whatever if startUp() == True
                return True
            else:
                # quits the application
                print("No worries, hope to see you back soon!")
                return False

def loadingAnimation():
    console = Console()
    tasks = [f"task {n}" for n in range(1, 11)]

    with console.status("[bold blue]Working on tasks...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log("Searching for duplicates: [bold green]Completed")

def scanner(path, list_duplicates = []):
    # while loop from loadingAnimation() will be called here. Until that is finished, it will call loading animation
    for item in os.listdir(path):
        '''
        Need to look inside of the directories (possibly recursively) WITHIN the itemPath
        and check out those directories and files (if the directories are NOT duplicates)
        '''
        if item[0] != '.':
            itemPath = os.path.join(path, item)
            if os.path.isdir(itemPath):
                if itemPath.endswith(" (1)"):
                    list_duplicates.append(itemPath)
            elif os.path.isfile(itemPath):
                if "(1)" in itemPath:
                    list_duplicates.append(itemPath)

    if len(list_duplicates) > 0:
        return True
    else: # didn't find any duplicates
        return False

def showDups(list_duplicates):
    console = Console()
    console.log(f"Duplicate items are listed here: [yellow]{list_duplicates}")

def removing(list_duplicates):
# FILES: os.remove(filepath)
# DIRECTORIES: os.rmdir(directorypath)
    # while loop from loadingAnimation() will be called here. Until that is finished, it will call loading animation
    while True:
        remove = input("Would you like to remove all of the listed items?\n> ")
        if remove.lower() not in ["yes", "no", "y", "n"]:
                print("You must respond with \"yes\" or \"no\"\n")
                continue
        else:
            if remove.lower() in ["yes", "y"]:
                break
            else:
                print("That's okay. Exiting the application.")
                return False

    if remove.lower() in ["yes", "y"]:
        for itemPath in list_duplicates:
            if os.path.isdir(itemPath):
                os.rmdir(itemPath)
            elif os.path.isfile(itemPath):
                os.remove(itemPath)
        return True

def run():
    agree = startUp()
    if agree == True: # if user agrees, continue. If not, nothing happens; ends at startUp()
        path = input("Enter the path where I should look for duplicates.\n> ")
        list_duplicates = []
        scanning = scanner(path, list_duplicates)
        if scanning == True:
            showDups(list_duplicates)
            remove_process = removing(list_duplicates)
            if remove_process == True:
                print(f"Program is finished, there are no more duplicates within {path}.")

run()