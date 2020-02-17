import random

#import random for accurate sim testing

# ======Variables======
    # Every_roll is the total rolls for the entire simulation
    # sim_runs serves as a counter in the outside loop
    # dice_roll is the variable assignment of the die being rolled
    # num_of_rolls is how many rolls per sim sim_runs
    # x is how many times the sim is to be run
Every_roll = 0
sim_runs = 0
dice_roll = 0
num_of_rolls = 0
x = 100000

# ======Simulation======
    # Outside loop runs the simulation desired number of times
    # inside loop is the sim rolling the die until a "6" is rolled
        # using the random function and randint() operator
    # num_of_rolls increases by "1" until a "6" is rolled

while sim_runs < x:
    while dice_roll != 6:
        dice_roll = random.randint(1, 6)
        num_of_rolls += 1

# =====Looping variables======
    # Once inside loop condition is met, outside loops alters Variables
        # sim_runs increases by "1" for every simulation ran
        # Every_roll increases by the num_of_rolls from the most recent sim
        # dice_roll is reset to "0" otherwise inside loop will not simulate
        # num_of_rolls is reset to "0" otherwise is compounded

    sim_runs += 1
    Every_roll += num_of_rolls
    dice_roll = 0
    num_of_rolls = 0

# ======Calculation======
    # Avg is the average number of rolls for the entire to program

Avg = (Every_roll / x)

print(Avg)
