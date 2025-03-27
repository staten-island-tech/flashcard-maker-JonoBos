import json  

class Teacher:
    def card_creator():
        cards = {}
        while True:
            da_input = input("Type YES if you would like to make a card (or anything else to stop): ")
            if da_input == 'YES':
                question = input("Enter the question: ")
                answer = input("Enter the answer: ")
                cards[question] = answer
            else: 
                break
        
        with open("FlashCards.json", "w") as file:
            json.dump(cards, file, indent=4)
        print("It saved yo")

class Student:
    def card_answer():
        with open("FlashCards.json", "r") as file:
            student_card = json.load(file)

        points = 0
        streak = 0

        for question, correct_answer in student_card.items():
            print(f"{question}")
            there_answer = input("Your answer: ")()

            if there_answer() == correct_answer():
                points += 1
                streak += 1
                print("Yep")
                if streak >= 5:
                    points += 10
                    print("U got a bonus")
            else:
                streak = 0
                print(f"Nah. The right  answer was dis: {correct_answer}. Yo streak gone now.")
        
        print(f"You done. Your final score: {points}")

def main():
    while True:
        teacher_student = input("Type 'T' if you're a teacher or 'S' if you're a student ")
        if teacher_student == 'T':
            Teacher.card_creator()
        elif teacher_student == 'S':
            Student.card_answer()
            break
        else:
            print("Only 'T' or 'S' bruh")

