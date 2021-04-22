import random

def play():
    choices = ['r','p','s']
    user = input("'{}' for rock, '{}' for paper, '{}' for scissors: ".format(*choices))
    computer = random.choice(choices)

    if user == computer:
        return 'Tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

# r > s , s > p , p > r
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())