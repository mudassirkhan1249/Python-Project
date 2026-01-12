import json
import time
import os

def signup():
    pin = input("Enter your 4 digits pin :-")
    with open("masterpin.json", "r") as f:
        data = json.load(f)
        for i in range(len(data)):
            if pin in data["masterPassword"][i]:
                print("This pin is Exist in database Please Enter New pin :)")
                signup()
            else:
                DATA = {
                    "1234":{
                        "gmail":"ghjegf"
                    }
                }
                d = data["masterPassword"]
                 

def findData(usrinp):
    with open("masterpin.json", "r") as f:
        data = json.load(f)
        for i in range(len(data)):
            if usrinp in data["masterPassword"][i]:
                for key, value in data["masterPassword"][i][usrinp].items():
                    print(f"{key} : {value}")
            else:
                signup()

def main():
    userInput = input("Enter your Master pin here:-")
    findData(userInput)

main()
