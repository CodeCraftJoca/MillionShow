from models.calculate import Calculate
from models.prize import consult_prize, Prize
from models.validator import Validator
def main() -> None:
    start()

def start() -> None:
    print('------------------------------------------------------------')
    print('|This game is inspired by Show do Milhão from Mega Drive 3|')
    print('------------------------------------------------------------')
    print("|             Let's meet our participant now              |")
    print('------------------------------------------------------------')
    name: str = str(input("|                  what is your name?                     |\n  "))
    print('------------------------------------------------------------')
    print('           1 - Easy | 2 - Medium | 3 - Hard               ')
    question: str = '          Please choose the difficulty level?         \n'
    difficulty = ask_difficulty(question)

    
    print('The million dollar show is about to begin')
    play(difficulty)

def play(difficulty):

    score: int = 0
    continue_or_playing = None

    while continue_or_playing != 0:
        awards = show_Awards(score, difficulty)
        calc: Calculate = Calculate(difficulty)

        print(f"Let's go to the question worth ${awards._Prize__correct},00 let's see:")
        print('What is the right answer?')
        
        question_operation = calc.show_operation()
        result = ask_question_int(question_operation)

        score = int(check_response(result, calc, awards, score))

        if score > 0:
            question: str = 'Do you want to continue? \nEnter 1 to continue and 0 to exit:\n'
            continue_or_playing = ask_question_int(question)
        else:
            question: str = "Do you start a new game? \nEnter 1 to play again 0 to end:\n"
            print('')
            continue_or_playing = ask_question_int(question)
            if(continue_or_playing == 1):
                start()

    stop(awards)
    print('To the next!')

def show_Awards(level: int, difficulty: int) -> Prize:
    awards: Prize = consult_prize(level, difficulty)
    print('Awards:')
    print(f"Getting it right: ${awards._Prize__correct},00 \nIf you get it wrong: ${awards._Prize__wrong},00 \nNot if you stop now: ${awards._Prize__stop},00")
    return awards

def wrong(score: int, awards: Prize) -> None:
    print("you lost")
    print(f'you reached the Level: {score + 1}')
    if score == 0 or score == 14:
        print('You lost everything')
        return
    else:
        print(f'You won ${awards._Prize__wrong},00')
        return

def stop(awards: Prize) -> None:
    print(f'You won ${awards._Prize__wrong},00')
    return

def win(awards: Prize) -> None:
    print("Congratulations you won")
    print(f'You won ${awards._Prize__correct},00')
    return

def ask_difficulty(question) -> int:
    print(question)
    while True:
        response = input()
        if Validator.is_valid_difficulty(response):
            return int(response)
        print("Invalid difficulty. Please enter 1, 2, or 3.")

def ask_question_int(question) -> int:
    while True:
        print(question)
        try:
            response = int(input())
            return response
        except ValueError:
            print('This field only accepts integer numbers')
def check_response(result: int, calc: Calculate, awards: Prize, score: int):
    if calc.check_result(result):
            score += 1

            print(f'You won ${awards._Prize__correct}')
            if score == 14:
                win(awards)
            return score
    else:
        wrong(score, awards)
        return score

if __name__ == '__main__':
    main()

