import random

def brGame(turn, count, num):
    for _ in range(count):
        num += 1
        if num > 31:
            break
        print(f"{turn} {num}")
    return num

num = 0

while num < 31:

    num = brGame("computer", random.choice([1, 2, 3]), num)
    if num >= 31:
        print("player win!")
        break

    while True:
        player_num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

        if player_num.isdigit(): 
            player_num = int(player_num)
            if player_num in [1, 2, 3]: 
                num = brGame("player", player_num, num)
                if num >= 31:
                    print("computer win!")
                break  
            else:
                print("1, 2, 3 중 하나를 입력하세요.")
        else:
            print("정수를 입력하세요.")