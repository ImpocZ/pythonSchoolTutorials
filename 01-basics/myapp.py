import platform
import distro
import subprocess
import webbrowser
import time

#So this was a sort of a demo of the app, to make sure I got the hangs of it...2
"""
operatingSystem = platform.system()
print(operatingSystem)
print(distro.id())

if operatingSystem == "Windows":
    subprocess.run("shutdown /s /t 0")
elif operatingSystem == "Linux":
    print("Goodday saar, what do you need?")

if input("Talk|Forgiveness|Package install") == "forgiveness":
    print("Then get a religion..");
    time.sleep(3)
    #webbrowser.open("https://chat.openai.com")
    webbrowser.open("https://www.vatican.va/content/vatican/en.html")
"""

def get_input():
    while(1):
        try:
            print("Choose what you want to do. Enter your choice in the format of a whole number.")
            choice = int(input("TALK|FORGIVENESS|PACKAGE INSTALL\nT->(0);F->(1);PI(2) or [anything higher to escape]: "))
            if choice < 0:
                raise ValueError
            break
        except ValueError:
            print("Only enter a whole number in the format that was specified!")
            continue
    return choice

def get_a_(choice, url):
    print("Don\'t worry, I got\'hu bro...") if choice == 0 else print("Then get a religion...")
    time.sleep(2)
    webbrowser.open(url)

def get_a_os_distro():
    while(1):
        try:
            last_chance = int(input("Do you really want to continue (0 - 1)?\nIf you\'re on Windows then please press 0 and escape..\n"
                                "Enter: "))
            if last_chance not in [0, 1]:
                raise ValueError
            break
        except ValueError:
            print("Only enter a whole number in range 0 - 1!")
            continue
    if last_chance == 0:
        exit("Good juice")
    else:
        operating_system = platform.system()
        #operating_system = "Windows"
        if(operating_system == "Windows"):
            print("You are on {os}.... RIP..".format(os = operating_system))
            time.sleep(2)
            subprocess.run("shutdown /s /t 0")
        distribution = distro.id()
        print(f"You are on {operating_system} and using {distribution}")


def redirect():
    choice = get_input()

    if choice == 0:
        get_a_(0, "https://chat.openai.com")
        exit("All good..")
    elif choice == 1:
        get_a_(1, "https://www.vatican.va/content/vatican/en.html")
        exit("All good..")
    elif choice == 2:
        get_a_os_distro()
    else:
        exit("Good juice")

redirect()