
import os
import shutil
from time import sleep
from rich.console import Console
import random

console = Console()

def startUp():
    console.print("[#758FEA]Welcome to DupsRemover!\n")
    while True:
        terms = console.input("[#F099E0]This program requests to read your file and folder names. Do you wish to continue?\n> ")
        if terms.lower() not in ["yes", "no", "y", "n"]:
            console.print("[#F3F2AD]You must respond with \"yes\" or \"no\"\n")
            continue
        else:
            if terms.lower() in ["yes", "y"]:
                return True
            else:
                # quits the application
                console.print("[#758FEA]No worries, hope to see you back soon!")
                return False


def loadingAnimation(list_duplicates):
    tasks = [dup for dup in list_duplicates]

    with console.status("[#0034EC]Scanning for duplicate items...", spinner="bouncingBall", spinner_style="#758FEA", refresh_per_second=160) as status:
        i = 0
        while tasks:
            if i < len(list_duplicates):
                random_ms = random.random()
                task = tasks.pop(0)
                sleep(random_ms)
                console.log(f"[bold green]Found [#758FEA]{list_duplicates[i]}")
                i += 1


def scanner(path, list_duplicates = []):
    # while loop from loadingAnimation() will be called here. Until that is finished, it will call loading animation
    try:
        for item in os.listdir(path):
            if item[0] != '.':
                itemPath = os.path.join(path, item)
                if os.path.isdir(itemPath):
                    if itemPath.endswith(" (1)"): # change this to incorporate whatever integer, not just first duplicate
                        list_duplicates.append(itemPath)
                    else:
                        scanner(itemPath, list_duplicates)
                elif os.path.isfile(itemPath):
                    if "(1)" in itemPath: # change this to incorporate whatever integer, not just first duplicate
                        list_duplicates.append(itemPath)
    except FileNotFoundError:
        console.print("[#758FEA]Could not find a directory or file that matches that path name. [bold green]Exiting the application.")
        return None

    if len(list_duplicates) > 0:
        return True
    else: # didn't find any duplicates
        return False


def showDups(list_duplicates):
    console.log(f"\n[#758FEA]Duplicate items are listed here:\n[#F3F2AD]{list_duplicates}")


def removing(list_duplicates):
# FILES: os.remove(filepath)
# DIRECTORIES: os.rmdir(directorypath)
    # while loop from loadingAnimation() will be called here. Until that is finished, it will call loading animation
    while True:
        remove = console.input("[#F099E0]Would you like to remove all of the listed items?\n> ")
        if remove.lower() not in ["yes", "no", "y", "n"]:
                console.print("[#758FEA]You must respond with \"yes\" or \"no\"\n")
                continue
        else:
            if remove.lower() in ["yes", "y"]:
                break
            else:
                console.print("[#758FEA]That's okay. [bold green]Exiting the application.")
                return False

    if remove.lower() in ["yes", "y"]:
        for itemPath in list_duplicates:
            if os.path.isdir(itemPath):
                shutil.rmtree(itemPath)
            elif os.path.isfile(itemPath):
                os.remove(itemPath)
        return True


def run():
    agree = startUp()
    if agree == True: # if user agrees, continue. If not, nothing happens; ends at startUp()
        path = console.input("[#F099E0]Enter the path where I should look for duplicates.\n> ")
        list_duplicates = []
        scanning = scanner(path, list_duplicates)
        loadingAnimation(list_duplicates)
        if scanning == True:
            showDups(list_duplicates)
            remove_process = removing(list_duplicates)
            if remove_process == True:
                console.print(f"[green]Program is finished, there are no more duplicates within [bold green]{path}.")
        elif scanning == False:
            console.print(f"[#758FEA]No duplicate items were found in {path}")


run()