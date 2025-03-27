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
                break
                
        finished = True
        with open("FlashCards.json", "w") as file:
            json.dump(cards,file, indent =4)


class Student:
   for question, correct_answer in student_card.items():
            print(f"\n{question}")
            def card_answer():
                value_student=input("What is the answer?")
                point =0
                streak=0
                with open ("FlashCards.json", "r") as file:
                    student_card =json.load(file)
                    for card in student_card:
                        if value_student == student_card [card]: 
                            point +=1 
                            streak+=1
                            if streak>=5:
                                point+=10
                        if value_student != student_card [card]:
                            streak = 0
                            print (f' Sorry the correct answer was ' ,{student_card[card]} ,'Your streak has been reset.')
                        print (f'You have finished. Your score was {point}')
def main ():
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
if __name__ == "__main__":
    main()


