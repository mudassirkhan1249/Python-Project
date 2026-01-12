import json 
import time
import os
import webbrowser

subject = input("Enter the subject ): ").lower()
userInput = input("Enter the study topic: ").lower()

def generate_txt(subject, topic):
    with open("topic.json", "r") as f:
        data = json.load(f)

        for i in range(len(data["topics"])):
            try:
                if topic in data["topics"][i][subject]:
                    study_material = data['topics'][i][subject][topic]
                    filename = f"{topic}_study_material.txt"
                    with open (filename, "w") as file:
                        file.write(f"Study Material for {topic} in {subject}:\n\n")
                        for key, value in study_material.items():
                            file.write(f"{key.capitalize()}:\n")
                            if isinstance(value, list):
                                for item in value:
                                    file.write(f"- {item}\n")
                            else:
                                file.write(f"{value}\n")
                            file.write("\n")
                    print(f"Study material saved to {filename}")
                    break
            except KeyError:
                continue


def main():
    with open ("topic.json", "r") as f:
        data = json.load(f)

        for i in range(len(data["topics"])):
            try:
                if userInput in data["topics"][i][subject]:
                    print(f"Topic found in the database.\nGenerating study material for {userInput} in {subject}...")
                    time.sleep(1.3)
                    study_material = data['topics'][i][subject][userInput]
                    for key, value in study_material.items():
                        print(f"\n{key.capitalize()}:")
                        if isinstance(value, list):
                            for item in value:
                                print(f"- {item}")
                        else:
                            print(f"{value}")
                    print("Study material generation complete.")

                    print("If you want a txt file of this study material, please enter 'yes' else 'no'")
                    choice = input("____:-").lower()
                    if choice == 'yes':
                        generate_txt(subject, userInput)
                    else:
                        exit()
                    break
            
            except KeyError:
                continue
        else:
            print("Topic not found in the database.")
            print("Searching on Your Browser...")
            time.sleep(1.3)
            url = f"https://www.google.com/search?q=Explain+Everything+About+{userInput}+in+{subject}"
            webbrowser.open(url)
                
            

main()