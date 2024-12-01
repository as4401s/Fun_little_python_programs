import random

print("Welcome to the game of Blackjack!")

# Define the numbers and their corresponding digit values
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
digits_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 'A' defaults to 11

# Function to get a random number and its corresponding digit value
def my_rand(numbers, digits_num):
    num_me = random.choice(numbers)
    position = numbers.index(num_me)
    corresponding_value = digits_num[position]
    return num_me, corresponding_value

# Function to calculate the sum of card values
def calculate_sum(values):
    total = sum(values)
    # Adjust for Aces (11 -> 1 if total exceeds 21)
    while total > 21 and 11 in values:
        values[values.index(11)] = 1  # Convert one Ace (11) to 1
        total = sum(values)
    return total

# Player's turn logic
def player_turn(player_name, numbers, digits_num):
    print(f"\n{player_name}'s turn...")
    player_values = []
    for _ in range(2):  # Draw two cards initially
        card, value = my_rand(numbers, digits_num)
        player_values.append(value)
        print(f"{player_name} got: {card} (Value: {value})")
    
    player_total = calculate_sum(player_values)
    print(f"{player_name}'s total is: {player_total}")

    # Check if the player has Blackjack
    if player_total == 21:
        print(f"{player_name} has Blackjack!")
        return player_total, True

    # Player's decision to draw more cards
    while player_total < 21:
        decision = input(f"{player_name}, do you want to draw another card? (yes/no): ").lower()
        if decision == 'yes':
            card, value = my_rand(numbers, digits_num)
            player_values.append(value)
            player_total = calculate_sum(player_values)
            print(f"{player_name} got: {card} (Value: {value})")
            print(f"{player_name}'s total is now: {player_total}")
        elif decision == 'no':
            print(f"{player_name} chose to stand.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if player_total > 21:
        print(f"{player_name} busted with a total of {player_total}!")
    return player_total, player_total == 21

# Main game loop
print("\nStart game!")
player1_name = "Player 1"
player2_name = "Player 2"

# Player 1's turn
player1_total, player1_blackjack = player_turn(player1_name, numbers, digits_num)

# Player 2's turn
player2_total, player2_blackjack = player_turn(player2_name, numbers, digits_num)

# Determine the winner
print("\nGame Over!")
if player1_blackjack and not player2_blackjack:
    print(f"{player1_name} wins with a Blackjack!")
elif player2_blackjack and not player1_blackjack:
    print(f"{player2_name} wins with a Blackjack!")
elif player1_total > 21 and player2_total <= 21:
    print(f"{player2_name} wins! {player1_name} busted.")
elif player2_total > 21 and player1_total <= 21:
    print(f"{player1_name} wins! {player2_name} busted.")
elif player1_total > player2_total and player1_total <= 21:
    print(f"{player1_name} wins with a total of {player1_total}!")
elif player2_total > player1_total and player2_total <= 21:
    print(f"{player2_name} wins with a total of {player2_total}!")
elif player1_total == player2_total:
    print("It's a tie!")
else:
    print("Both players busted! No one wins.")




