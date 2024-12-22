import random
fighter1 = input("enter the first fighter: ")
fighter2 = input('enter the second fighter: ')

BY_choices = ['unanimous decision', 'split decision', 'KO/TKO', 'submission', 'DQ']
BY_weights = [0.3, 0.3, 0.23, 0.16, 0.01]
BY = random.choices(BY_choices, weights=BY_weights, k=1)[0]

winner = random.choice([fighter1, fighter2])
print(f'And the winner by', BY, 'iiiissss...', winner,'!' )
