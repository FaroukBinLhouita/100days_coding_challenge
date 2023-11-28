import random
from BlackJack import logo 

def card_game(sets_cards):
    """
    :param sets_cards: list
    :return: list
    """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    if len(sets_cards) == 0:
        for i in range(2):
            sets_cards.append(random.choice(cards))
        return sets_cards
    else:
        for i in range(1):
            sets_cards.append(random.choice(cards))
        return sets_cards

def calculate_score(array):
    count = 0
    for i in array:
        count += i
    if len(array) == 2 and count == 21:
        return 0
    elif 11 in array and count > 21:
        array.remove(11)
        array.append(1)
        count = calculate_score(array)
    return count

def winner(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("you went over. You lose 😤😤")
        return True
    if user_score == computer_score:
        print("Draw 🙃")
        return True
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
        return True
    elif user_score == 0:
        print("You win with a Blackjack 😎")
        return True
    elif user_score > 21:
        print("You went over. You lose 😭")
        return True
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
        return True
    elif user_score > computer_score:
        print("You win 😃")
        return True
    else:
        print("You lose 😤")
        return True

def play_game():
    print(logo)
    cly = False

    while not cly:
        is_game_over = False
        user_cards = []
        computer_cards = []

        user_cards = card_game(user_cards)
        computer_cards = card_game(computer_cards)

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print("your cards are", user_cards, "current score", user_score)
            print("computer's first card is", computer_cards[0])

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    user_cards = card_game(user_cards)
                else:
                    is_game_over = True

            while computer_score != 0 and computer_score < 17:
                computer_cards = card_game(computer_cards)
                computer_score = calculate_score(computer_cards)

        print("your final hand: ",user_cards ," final score: ",user_score)
        print("computer's final hand: ",computer_cards, "final score: ", computer_score)
        cly = winner(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
