import os
import numpy as np
import random
import time

names = ["Ishhal Ali", "Mudassir Khan", "Khizar Khan", "Mubassir", "Ashir", "Ayesha", "Sajid", "Raees", "Sohail"]
age = np.linspace(18, 60, 43)
designation = ["Software Engineer", "Doctor", "CA", "AI Engineer", "Data Scientist", "Data Analyst", "Full-Stack Developer", "Ethical Hacker"]
education = ["Matriculation", "Intermidiate", "BS Degree", "BE Degree", "MBBS"]
martial_status = ["Married", "Unmarried"]


def csv_generator():
    file_name = input("Please enter your file name here --> ".title()) + ".csv"
    rows = int(input("How many rows you want in your data. enter here --> ".title()))

    with open(file_name, 'w') as f:
        f.write("name,age,designation,education,martial_status")

    with open(file_name, 'a') as g:
        print('Working.......')
        time.sleep(1.5)

        for i in range(1, rows + 1):
            name = random.choice(names)
            ag = random.choice(age)
            desg = random.choice(designation)
            edu = random.choice(education)
            marsta = random.choice(martial_status)

            if desg == "Doctor" or edu == "MBBS":
                edu = "MBBS"
                desg = "Doctor"
            g.write(f"\n{name},{ag},{desg},{edu},{marsta}")

    print("Data Generated Successfully")

csv_generator()

while True:
    choice = input("Do You Want To Generate More Data? (Yes/No) : ").lower()
    if choice == "yes":
        csv_generator()
    elif choice == "no":
        print("Thanks for using CSV Generator")
        break
    else:
        print("Invalid Choice")
        csv_generator()
