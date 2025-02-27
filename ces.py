import random
from io import StringIO
import sys

def simulate_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = random.randint(1, 100)  # 模拟玩家随机猜测
        attempts += 1

        if guess < number_to_guess:
            pass  # 模拟玩家看到提示后继续猜测
        elif guess > number_to_guess:
            pass  # 模拟玩家看到提示后继续猜测
        else:
            guessed_correctly = True

    return attempts

def run_tests(num_tests=100):
    results = []
    for _ in range(num_tests):
        attempts = simulate_game()
        results.append(attempts)

    average_attempts = sum(results) / num_tests
    max_attempts = max(results)
    min_attempts = min(results)

    print(f"测试结果（{num_tests}次游戏）：")
    print(f"平均尝试次数: {average_attempts:.2f}")
    print(f"最大尝试次数: {max_attempts}")
    print(f"最小尝试次数: {min_attempts}")

if __name__ == "__main__":
    run_tests()