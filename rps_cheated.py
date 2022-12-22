import random

winning_chance = 100
print("ROCK-PAPER-SCISSORS\n"
      "1-rock\n"
      "2-paper\n"
      "3-scissors\n"
      "0-quit")

running = True


def main():
    u = int(input("Your choice: "))
    c = random.randint(1, 3)

    """
    if (u == 1 and c == 3) or (u == 2 and c == 1) or (u == 3 and c == 2):
        print("You win!")
    elif u == c:
        print("It's a draw!")
    else:
        print("You lose!")
    print("My choice was", c)
    """

    def user_win():
        print("You win!")
        if u == 1:
            print("My choice was 3")
        elif u == 2:
            print("My choice was 1")
        elif u == 3:
            print("My choice was 2")

    def user_lose():
        print("You lose!")
        if u == 1:
            print("My choice was 2")
        elif u == 2:
            print("My choice was 3")
        elif u == 3:
            print("My choice was 1")

    win_decider = random.randint(1, 100)
    if u == 0:
        global running
        running = False
    else:
        if win_decider <= winning_chance:
            user_win()
        else:
            user_lose()


while running:
    main()
