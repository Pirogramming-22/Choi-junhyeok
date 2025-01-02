import random

num = 0

while num < 31:
    for _ in range(random.choice([1, 2, 3])):
        num += 1
        if num > 31:
            break
        print(f"computer {num}")
    if num >= 31:
        print("computer 패배!")
        break

    player_num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
    if player_num.isdigit():
        player_num = int(player_num)
        if player_num in [1, 2, 3]:
            for _ in range(player_num):
                num += 1
                if num > 31:
                    break
                print(f"player {num}")
            if num >= 31:
                print("player 패배!")
                break
        else:
            print("1, 2, 3 중 하나를 입력하세요.")
    else:
        print("정수를 입력하세요.")