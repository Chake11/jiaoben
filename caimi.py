import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("猜一个1到100之间的数字: "))
            attempts += 1

            if guess < number_to_guess:
                print("猜小了！")
            elif guess > number_to_guess:
                print("猜大了！")
            else:
                print(f"恭喜你！你猜对了，数字是{number_to_guess}。你用了{attempts}次尝试。")
                guessed_correctly = True
        except ValueError:
            print("请输入一个有效的数字！")

    return attempts

if __name__ == "__main__":
    guess_number_game()