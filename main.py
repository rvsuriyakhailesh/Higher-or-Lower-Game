import random
from game_data import data
from logo import const_logo, const_vs

print(const_logo)

def format(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)
score = 0
game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format(account_a)}\n")
    print(const_vs)
    print(f"Against B: {format(account_b)}\n")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(const_logo)
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Better luck next time! Final score: {score}")
        game_should_continue = False
