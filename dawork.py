import json 

class Teacher:
    def card_creator():
        cards = {}
        finished = False 
        while finished == False:
            if input ("type YES if you would like to make a card") == 'YES':
                question = input("What da question?")
                answer = input("Gimme an answer")
                cards[question] = answer
            else: 
                finished == True
                with open("flashcard.json", "w") as file:
                    json.dump(cards,file, indent =4)


class Student:
#From Json file you want the student to find the value 
    def card_answer():
        value_student=input("What is the answer?")
        point ==0
        streak==0
        with open ("flashcard.json", "r") as file:
            student_card =json.load(file)
            for card in student_card:
                print (f'card')
                if value_student == student_card [card]: 
                    point +=1 
                    streak+=1
                if value_student != student_card [card]:
                    streak = 0
                    print (f' Sorry the correct answer was ' ,{card.value()} ,'Your streak has been reset.')
                print (f'You have finished. Your score was {point}')

while True:

    role_decided = False 

    while role_decided == False:
        teacher_student = input ("Type T if you're a teacher or type S if you're a student.")
        if teacher_student == 'T':
            Teacher.card_creator()
            role_decided == True
        elif teacher_student == 'S':
            Student.card_answer()
            role_decided ==True
        else:
            print ("No no no")
if streak>=5:
    point+=10
