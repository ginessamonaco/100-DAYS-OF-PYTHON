question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Quiz:
    
    def give_question(question):
        guess = input(f"{question} (True/False): ").capitalize()
        return guess

    def check_guess(answer, guess):
        if guess == answer:
            print(f"{guess} is correct!")
            return 1
        else:
            print(f"{guess} is wrong. {answer} was the correct answer.")
            return 0


done_playing = False

while not done_playing:
    points = 0
    plays = 0

    question_bank = []

    for q in question_data:
        text = q["text"]
        answer = q["answer"]
        new_question = (text, answer)
        question_bank.append(new_question)

    for q in question_bank:
        print(f"\nSCORE: {points}/{plays}\n")
        new_question = Question(q[0], q[1])
        user_guess = Quiz.give_question(new_question.text)
        points += Quiz.check_guess(new_question.answer, user_guess)
        plays += 1

    print(f"\nFINAL SCORE: {points}/{plays}\n")
    play_again = input("\nDo you want to play again? (Yes/No): ").capitalize()
    if play_again != "Yes":
        done_playing = True