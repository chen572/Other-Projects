import random
from players import Player


def menu():
    user_name = input("Enter UserName:\n")
    user_name = Player(user_name, 100, None)
    
    print("\n\nHello {name}, here's 100$ on the house dont lose them on the first game!\n".format(name=user_name.name))
    
    while True:    
        games = {'a':heads_or_tails, 'b':cho_han, 'c':black_jack, 'd':roulette}
        game_choice = get_game_choice(user_name)
        
        games[game_choice](user_name)
            
        if user_name.money != 0:
            restart_loop = input("\n{details}\nDo you want to play another game?   (y/n)\n".format(details=user_name))
            
            if restart_loop == 'n':
                break
            
            else:
                continue
        
        else:
            print("\nYour out of money!")
            break
    print("\nThank you for playing see you next time.")

def heads_or_tails(player):
    p_choice = get_p_choice_hot(player)
    p_bet = get_p_bet(player)
    
    num = random.randint(1, 2)
    player_result = ""
    
    p_choice = p_choice.lower()
    
    if num == 1:
        
        num = "heads"
        
        if p_choice == num:
            player_result = "Won"
        
        else:
            player_result = "Lost"
    
    if num == 2:
        
        num = "tails"
        
        if p_choice == num:
            player_result = "Won"
        
        else:
            player_result = "Lost"
    
    player_result_money(player, player_result, p_bet)
    
    print("\n{name} your choice was {player_choice}, and the coin flip was {result}\nYou have {game_result} and now have {money}$".format(name=player.name, player_choice=p_choice, result=num, game_result=player_result, money=str(player.money)))
    return player.money

def cho_han(player):
    p_choice = get_p_choice_cho(player)
    p_bet = get_p_bet(player)

    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    num_result = (dice1 + dice2)
    result = (dice1 + dice2) % 2
    player_result = ""
    
    if result == 0:
        result = "even"
        
        if p_choice == result:
            player_result = "Won"
        
        else:
            player_result = "Lost"
    
    if result == 1:
        result = "odd"
        
        if p_choice == result:
            player_result = "Won"
        
        else:
            player_result = "Lost"
    
    player_result_money(player, player_result, p_bet)
    
    print("\n{name} your choice was {player_choice}, and the sum of the 2 dices was {num_result} which is {result}\nYou have {game_result} and now have {money}$".format(name=player.name, player_choice=p_choice, num_result=num_result, result=result, game_result=player_result, money=str(player.money)))
    return player.money

def black_jack(player):
    p_bet = get_p_bet(player)
    p_cards = []
    #c_cards = []
    
    numbers = list(range(1, 14))
    drawn_cards = {num:[] for num in numbers}
    #c_drawn_cards = {}
    
    player_result = ""
    
    while True:
        card = random.randint(1, 13)
        c_card = random.randint(1, 13)
        color = get_color()
        c_color = get_color()
        
        if card == 11:
            
            if not color in drawn_cards[card]:
                p_cards.append(10)
                drawn_cards[card] += [color]
                
                if sum(p_cards) > 21:
                    print("\n{name} have drawn the Jack of {color}, and went over 21 with {sum}\nYou Lost".format(name=player.name, color=color, sum=sum(p_cards)))
                    player_result = "Lost"
                    break
                
                print("\n{name} have drawn the Jack of {color}, and now have {sum}".format(name=player.name, color=color, sum=sum(p_cards)))
                
                if sum(p_cards) == 21:
                    print("\nBlackJack!\n{name} have scored exactly 21!\nYou Win".format(name=player.name))
                    player_result = "Won"
                    break
            
            else:
                continue
        
        elif card == 12:
            
            if not color in drawn_cards[card]:
                p_cards.append(10)
                drawn_cards[card] += [color]
                
                if sum(p_cards) > 21:
                    print("\n{name} have drawn the Queen of {color}, and went over 21 with {sum}\nYou Lost".format(name=player.name, color=color, sum=sum(p_cards)))
                    player_result = "Lost"
                    break
                
                print("\n{name} have drawn the Queen of {color}, and now have {sum}".format(name=player.name, color=color, sum=sum(p_cards)))
                
                if sum(p_cards) == 21:
                    print("\nBlackJack!\n{name} have scored exactly 21!\nYou Win".format(name=player.name))
                    player_result = "Won"
                    break
            else:
                continue

        elif card == 13:
            
            if not color in drawn_cards[card]:
                p_cards.append(10)
                drawn_cards[card] += [color]
                
                if sum(p_cards) > 21:
                    print("\n{name} have drawn the King of {color}, and went over 21 with {sum}\nYou Lost".format(name=player.name, color=color, sum=sum(p_cards)))
                    player_result = "Lost"
                    break
                
                print("\n{name} have drawn the King of {color}, and now have {sum}".format(name=player.name, color=color, sum=sum(p_cards)))
                
                if sum(p_cards) == 21:
                    print("\nBlackJack!\n{name} have scored exactly 21!\nYou Win".format(name=player.name))
                    player_result = "Won"
                    break
            else:
                continue

        elif card == 1:
            
            if not color in drawn_cards[card]:
                p_cards.append(11)
                drawn_cards[card] += [color]
                
                if sum(p_cards) > 21:
                    print("\n{name} have drawn the Ace of {color}, and went over 21 with {sum}\nYou Lost".format(name=player.name, color=color, sum=sum(p_cards)))
                    player_result = "Lost"
                    break
                
                print("\n{name} have drawn the Ace of {color}, and now have {sum}".format(name=player.name, color=color, sum=sum(p_cards)))
                
                if sum(p_cards) == 21:
                    print("\nBlackJack!\n{name} have scored exactly 21!\nYou Win".format(name=player.name))
                    player_result = "Won"
                    break
            else:
                continue

        elif 2 <= card <= 10:
            
            if not color in drawn_cards[card]:
                p_cards.append(card)
                drawn_cards[card] += [color]
                
                if sum(p_cards) > 21:
                    print("\n{name} have drawn the {card} of {color}, and went over 21 with {sum}\nYou Lost".format(name=player.name, card=str(card), color=color, sum=sum(p_cards)))
                    player_result = "Lost"
                    break
                
                print("\n{name} have drawn the {card} of {color}, and now have {sum}".format(name=player.name, card=str(card), color=color, sum=sum(p_cards)))
                
                if sum(p_cards) == 21:
                    print("\nBlackJack!\n{name} have scored exactly 21!\nYou Win".format(name=player.name))
                    player_result = "Won"
                    break
            else:
                continue
            
        end_game = input("\nDo you want to draw another card?  (y/n)\n")
        if end_game == "n":
            break
        else:
            continue

    if sum(p_cards) < 21:
        c_score = random.randint(10, 28)
        
        if c_score > 21:
            print("\nThe computer went over 21!\nYou Win")
            player_result = "Won"
        
        if sum(p_cards) > c_score:
            print("\nYou have {sum}, and the computer has drawn {c_sum}\nYou Win".format(sum=sum(p_cards), c_sum=c_score))
            player_result = "Won"
        
        if sum(p_cards) < c_score < 21:
            print("\nYou have {sum}, and the computer has drawn {c_sum}\nYou Lose".format(sum=sum(p_cards), c_sum=c_score))
            player_result = "Lost"
    
    player_result_money(player, player_result, p_bet)

    print("\n{name} You have {game_result} and now have {money}$".format(name=player.name, game_result=player_result, money=str(player.money)))
    return player.money

def roulette(player):
    p_choice = get_p_choice_rou(player)
    p_bet = get_p_bet(player)
    player_result = ""

    result_number = random.randint(1, 36)

    red = list(range(1, 10, 2)) + list(range(12, 19, 2)) + list(range(19, 28, 2)) + list(range(30, 37, 2))
    black = list(range(2, 11, 2)) + list(range(11, 18, 2)) + list(range(20, 29, 2)) + list(range(29, 36, 2))

    if p_choice == 'red':
        if result_number in red:    
            print("\nThe number was {num}, which is Red\nYou Won".format(num=result_number))
            player_result = "Won"
        
        else:
            print("\nThe number was {num}, which is Black\nYou Lost".format(num=result_number))
            player_result = "Lost"
    
    if p_choice == 'black':
        if result_number in black:
            print("\nThe number was {num}, which is Black\nYou Won".format(num=result_number))
            player_result = "Won"
        
        else:
            print("\nThe number was {num}, which is Red\nYou Lost".format(num=result_number))
            player_result = "Lost"
    
    if p_choice == 'even':
        if result_number % 2 == 0:
            print("\nThe number was {num}, which is an Even number\nYou Won".format(num=result_number))
            player_result = "Won"
        
        else:
            print("\nThe number was {num}, which is an Odd number\nYou Lost".format(num=result_number))
            player_result = "Lost"
    
    if p_choice == 'odd':
        if result_number % 2 == 1:
            print("\nThe number was {num}, which is an Odd number\nYou Won".format(num=result_number))
            player_result = "Won"
        
        else:
            print("\nThe number was {num}, which is an Even number\nYou Lost".format(num=result_number))
            player_result = "Lost"
    
    try:
        if 1 <= int(p_choice) <= 36:
            if p_choice == result_number:
                print("\nThe number was {num}, and you choice was {choice}!\nYou Win".format(num=result_number, choice=p_choice))
                player_result = "Wonn"
            if p_choice != result_number:
                print("\nThe number was {num}, and you choice was {choice}\nYou Lost".format(num=result_number, choice=p_choice))
                player_result = "Lost"
    except ValueError:
        pass

    player_result_money(player, player_result, p_bet)
    
    print("\n{name} You have {game_result} and now have {money}$".format(name=player.name, game_result=player_result, money=str(player.money)))
    return player.money
    
def get_p_choice_hot(player):
    p_choice = input("\nHello {0}, please choose Heads or Tails\n".format(player.name))
    p_choice = p_choice.lower()
    
    valid_input = ('heads', 'tails')
    
    if p_choice in valid_input:
        return p_choice
    
    print("\nThats not one of the 2 choices please pick again")
    
    return get_p_choice_hot(player)

def get_p_choice_cho(player):
    p_choice = input("\nHello {0}, please choose if the sum is gonna be Odd or Even\n".format(player.name))
    p_choice = p_choice.lower()
    
    valid_input = ('odd', 'even')
    
    if p_choice in valid_input:
        return p_choice
    
    print("\nThats not one of the 2 choices please pick again")
    
    return get_p_choice_cho(player)

def get_p_choice_rou(player):
    p_choice = input("\nHello {0}, you can either bet on 'Red' or 'Black', 'Odd' or 'Even' which will yield a 1 to 1 win ratio\nOr you can bet on a specific 'number' between 1 - 36 which will yield a 36 to 1 win ratio!\n".format(player.name))
    p_choice = p_choice.lower()
    
    valid_input = ('red', 'black', 'odd', 'even')
    
    try:
        if p_choice in valid_input or 1 <= int(p_choice) <= 36:
            return p_choice
    
    except ValueError:    
        print("\nYour input was invalid please type in either red, black, odd, even or a number from 1 to 36.\n")
        return get_p_choice_rou(player)

def get_p_bet(player):
    p_bet = input("\nHello {name}, You have {money}$ right now, how much would you like to bet?\n".format(name=player.name, money=str(player.money)))
    
    if int(p_bet) > player.money:
        print("\nYou dont have enough money")
        return get_p_bet(player)
    
    elif int(p_bet) == 0:
        print("\nYou have to bet higher than 0")
        return get_p_bet(player)
    
    return p_bet

def get_color():
    num = random.randint(1, 4)
    color = ""
    
    color_dic = {1:"Clubs", 2:"Diamonds", 3:"Hearts", 4:"Spades"}
    
    return color_dic.get(num)

def get_game_choice(user_name):
    game_choice = input("Hey {details}\nWhat game do you want to play?\n\n [A] Heads or Tails \n [B] Cho Han \n [C] BlackJack \n [D] Roulette\n  ".format(details=user_name))
    game_choice = game_choice.lower()
    
    valid_input = ['a', 'b', 'c', 'd']
    
    if game_choice in valid_input:
        return game_choice
    
    else:
        print("\nThat was not in the game list please input one of the letters")
        return get_game_choice(user_name)

def player_result_money(player, player_result, p_bet):
    if player_result == "Won":
        player.update_money(int(p_bet))
    
    elif player_result == "Lost":
        player.update_money(int("-"+p_bet))
    
    elif player_result == "Wonn":
        player.update_money((int(p_bet) * 36))
        player_result = "Won"
    
    return player_result



menu()