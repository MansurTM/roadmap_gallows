import random
import gallows

with open("words.txt", "r") as f:
    w = f.read()
words = w.split("\n")  # Список из слов



def correct_answer():
    global letter_sklad
    mask_str = ""
    letter = input("Введите букву: ").upper()
    if letter == random_word:
        return "win"
    if letter in letter_sklad or letter in random_word:
        for r in random_word:
            if letter == r:
                mask_str += r
            elif r in letter_sklad:
                mask_str += r
            else:
                mask_str += "*"
        letter_sklad += letter
        print(mask_str)
        if not "*" in mask_str:
            return "win"
        return True
    else:
        print(mask_str)
        return False


def incorrect_answer():
    global attempts, letter_sklad
    mask_str = ""
    attempts -= 1
    print(f"Осталось неудачных попыток: {attempts}")
    letter = input("Такой буквы нет, введите другую букву: ").upper()
    print(f"попыток: {attempts}")
    if letter in letter_sklad or letter in random_word:
        for r in random_word:
            if letter == r:
                mask_str += r
            elif r in letter_sklad:
                mask_str += r
            else:
                mask_str += "*"
        letter_sklad += letter
        print(mask_str)
        return True
    elif attempts < 2:
        print(gallows.hangman_steps[-attempts])
        print(f"Вы проиграли 🥲\n"
              f"Загаданное слово: {random_word}")
        return "loser"
    else:
        print(mask_str)
        return False


while True:
    random_word = random.choice(words).upper()
    right_wrong = True
    letter_sklad = ""
    attempts = 6
    game = input("Ну что, сыграем? Да(Y), Нет(N): ").upper()
    if game == "Y":
        mask = len(random_word) * "*"
        print(mask)
        while True:
            if right_wrong:  # Обработка верного ответа
                stage = correct_answer()
                right_wrong = stage
                if stage == "win":
                    print("Поздравляем, вы победили!")
                    break
            else:  #  Обработка неверного ответа
                print(gallows.hangman_steps[-attempts])
                wrong = incorrect_answer()
                right_wrong = wrong
                if wrong == "loser":  # Кончились попытки
                    break
    elif game == "N":
        print("Ну хорошо, как нибудь в другой раз")
        break
    else:
        print("Друг, нужно ввести Y или N в зависимости от того будешь играть или нет.")
        continue
