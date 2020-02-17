import random

Every_roll = 0
sim_runs = 0
dice_roll = 0
num_of_rolls = 0
x = 100000

while sim_runs < x:
    while dice_roll != 6:
        dice_roll = random.randint(1, 6)
        num_of_rolls += 1
            
    sim_runs += 1
    Every_roll += num_of_rolls
    dice_roll = 0
    num_of_rolls = 0

Avg = (Every_roll / x)
print(Avg)


#print(sim_runs)




