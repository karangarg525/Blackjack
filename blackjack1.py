import random



def deal_value():
    bet_value = 0
    while bet_value < 300:
        bet_value_temp = input('Enter you betting amount: 5, 10, 20, 50, 100 or "deal"\n')
        if bet_value_temp == "deal":
            break
        elif bet_value_temp == '5' or bet_value_temp == '10' or bet_value_temp == '20' or bet_value_temp == '50' or bet_value_temp == '100':
            bet_value = bet_value + int(bet_value_temp)
            print('Your betting amount is:', bet_value, "Press 'deal' to finalize this amount!")
        else:
            print("Please give a valid input!!!")
    print('Your final betting amount is:', bet_value)


def distribution1():
    sum = 0
    player_cards.append(random.randint(2, 11))
    player_cards.append(random.randint(2, 11))
    print("Your cards are:", player_cards)
    if player_cards[0] == 11 and player_cards[1] == 11:
        print("value of first card changes to 1 from 11")
        player_cards[0] = 1  # as value is exceeding 21, so value of first card(ace) would become 1
    for i in player_cards:
        sum = sum + i
    print("Sum of Cards is:", sum)
    return sum



def hit(sum):
    #game_on = True
    while True:
        player_cards.append(random.randint(1, 11))
        print(player_cards)
        for i in player_cards[(len(player_cards)-1):]:
            sum = sum + i
        if sum > 21:  # changing here
            for i in range(len(player_cards)):
                if player_cards[i] == 11:
                    player_cards[i] = 1
                    print(player_cards, '<- New values')
                    sum = sum - 10
                    break
                else:
                    continue
        print("Sum of your cards is:", sum)
        return sum


def dealer():
    d_value = random.randint(17, 26)
    return d_value

def stand(d_value, sum):
    if d_value > 21:
        print("Dealer's value is: ", d_value)
        print("You win!!! Dealer's value exceeded 21")
        game_on = False
    elif sum == d_value:
        print("Dealer's value is:", d_value)
        print('Stand-off')
    elif sum < d_value:
        print("Dealer's value is: ", d_value)
        print('You lose')
    elif sum > d_value:
        print("Dealer's value is:", d_value)
        print('You Win')


# ---------------------------------- Game Starts Here -----------------------------------------

while True:
    print("Welcome to Blackjack 21")
    player_cards = []
    d_value = dealer()
    button = ' '
    deal_value()
    s1 = distribution1()

    game_on = True

    while game_on:
        button = input("Choose your next operation (hit/stand)")
        if button == 'hit':
            s1 = hit(s1)
            if s1 > 21:
                #try:
                    #for position in range(len(player_cards)):
                        #if player_cards[position] == 11:
                            #player_cards[position] = 1
                #finally:
                print("You lose! Sum of you cards exceeded 21")
                game_on = False
        elif button == 'stand':
            stand(d_value, s1)
            game_on = False

    again = input("Do you want to play again? (y/n): ")
    if again == 'y':
        continue
    else:
        break