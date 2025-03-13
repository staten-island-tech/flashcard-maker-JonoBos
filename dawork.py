import json 
x = open("./saturn.json", encoding="utf8")
data = json.load(x)

class Teacher:
    key_teacher = input("What word or phrase would you like to use?")
    answer_teacher = input("what is the value/answer?")

flashcard_list =[]
flashcard_data = [flashcard.to_dict() for flashcard in flashcards_list]
with open("flashcards.json", "w") as file:
    json.dump(cars_data, file, indent=4)

"""     class Student: """